#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Conversión y Compilación ETL para TIP México.
Transforma los reportes de llamadas de Net2Alliance (N2A Cloud CommServer)
al layout oficial de inConcert (layout_data_repli.xlsx) requerido por Laura Mercado (TIP México).

Uso:
    python convertir_layout_tip.py [--inputs FILE1 FILE2 ...] [--template TEMPLATE.xlsx] [--output OUTPUT.xlsx]
"""

import os
import sys
import argparse
import datetime
from copy import copy
import pandas as pd
import openpyxl

# Umbral contractual de Nivel de Servicio (SLA) en segundos (ASA <= 20s)
SLA_THRESHOLD_SECONDS = 20

# Mapeo oficial de colas N2A -> Campaña / Skill TIP México
QUEUE_MAPPING = {
    "8001": "tip_general",
    "8002": "tip_bitcar",
    "8003": "tip_arrendamiento",
    "8004": "tip_siniestros",
    "8005": "tip_mantenimiento",
    "8006": "tip_documentacion",
    "8007": "tip_facturacion",
    "8008": "tip_telemetria",
    "8009": "tip_atencion_clientes"
}

def parse_call_record(row, schema_type):
    """
    Normaliza un registro de llamada de N2A según el esquema del archivo CSV.
    Retorna un diccionario estructurado o None si la fila es inválida.
    """
    try:
        if schema_type == 'schema_a':
            # Archivo antiguo (ej. llamadas_2026-10-19_a_2026-10-20.csv)
            raw_fecha = row['entrada_cola']
            if isinstance(raw_fecha, (datetime.datetime, pd.Timestamp)):
                dt = raw_fecha.to_pydatetime() if hasattr(raw_fecha, 'to_pydatetime') else raw_fecha
            else:
                raw_str = str(raw_fecha).strip()
                try:
                    dt = datetime.datetime.strptime(raw_str, '%d/%m/%Y %H:%M')
                except ValueError:
                    dt = datetime.datetime.strptime(raw_str, '%Y-%m-%d %H:%M:%S')
                    
            cola = str(row['cola']).strip()
            espera = float(row['espera_seg']) if pd.notnull(row['espera_seg']) else 0.0
            conversacion = float(row['conversacion_seg']) if pd.notnull(row['conversacion_seg']) else 0.0
            resultado = str(row['resultado']).strip().upper()
            
            is_aten = (resultado == 'CONTESTADA')
            is_ab = not is_aten
            numero = str(row.get('numero_origen', '')).strip()
            
            return {
                'fecha': dt.date(),
                'hora': dt.hour,
                'fin_ts': dt,
                'cola': cola,
                'espera': espera,
                'conversacion': conversacion,
                'is_aten': is_aten,
                'is_ab': is_ab,
                'numero': numero
            }
            
        elif schema_type == 'schema_b':
            # Archivo nuevo (ej. llamadas (3).csv o Llamdas 19-21 oct TIP.xlsx)
            raw_fin = row['Fin']
            if isinstance(raw_fin, (datetime.datetime, pd.Timestamp)):
                dt_fin = raw_fin.to_pydatetime() if hasattr(raw_fin, 'to_pydatetime') else raw_fin
            else:
                raw_str = str(raw_fin).strip()
                dt_fin = datetime.datetime.strptime(raw_str, '%Y-%m-%d %H:%M:%S')
                
            cola = str(row['Cola']).strip()
            espera = float(row['Espera (s)']) if pd.notnull(row['Espera (s)']) else 0.0
            conversacion = float(row['Conversación (s)']) if pd.notnull(row['Conversación (s)']) else 0.0
            
            # Hora de llegada a cola aproximada
            dt_start = dt_fin - datetime.timedelta(seconds=(espera + conversacion))
            
            cat = str(row.get('Categoría', '')).strip().upper()
            res = str(row.get('Resultado', '')).strip().upper()
            numero = str(row.get('Número', '')).strip()
            
            is_aten = (cat == 'CONTESTADA' or res == 'FINALIZADA')
            is_ab = not is_aten
            
            return {
                'fecha': dt_start.date(),
                'hora': dt_start.hour,
                'fin_ts': dt_fin,
                'cola': cola,
                'espera': espera,
                'conversacion': conversacion,
                'is_aten': is_aten,
                'is_ab': is_ab,
                'numero': numero
            }
    except Exception as e:
        return None

def detect_schema(file_path):
    """Detecta si el archivo CSV o XLSX corresponde a Schema A o Schema B."""
    if file_path.lower().endswith('.xlsx'):
        df_sample = pd.read_excel(file_path, nrows=3)
    else:
        df_sample = pd.read_csv(file_path, nrows=3)
    cols = [c.strip() for c in df_sample.columns]
    if 'entrada_cola' in cols:
        return 'schema_a'
    elif 'Fin' in cols and 'Cola' in cols:
        return 'schema_b'
    else:
        raise ValueError(f"Esquema no reconocido para {file_path}. Columnas: {cols}")

def load_all_calls(file_paths, start_date=None, end_date=None):
    """Carga y consolida todas las llamadas de los archivos CSV/XLSX con deduplicación."""
    calls = []
    seen = set()
    for path in file_paths:
        if not os.path.exists(path):
            print(f"[ADVERTENCIA] Archivo no encontrado: {path}")
            continue
        schema = detect_schema(path)
        print(f"[INFO] Procesando {os.path.basename(path)} con esquema '{schema}'...")
        if path.lower().endswith('.xlsx'):
            df = pd.read_excel(path)
        else:
            df = pd.read_csv(path)
            
        for _, row in df.iterrows():
            rec = parse_call_record(row, schema)
            if rec:
                # Filtrado por rango de fecha si aplica
                if start_date and rec['fecha'] < start_date:
                    continue
                if end_date and rec['fecha'] > end_date:
                    continue
                    
                # Deduplicación por firma única de llamada con timestamp exacto
                sig = (rec['fecha'], rec['fin_ts'], rec['cola'], rec['espera'], rec['conversacion'], rec.get('numero', ''), rec['is_aten'])
                if sig in seen:
                    continue
                seen.add(sig)
                calls.append(rec)
                
    print(f"[OK] Total de llamadas válidas únicas importadas: {len(calls)}")
    return calls

def aggregate_by_interval(calls):
    """
    Agrupa las llamadas por (fecha, franja, campaña).
    Calcula todas las métricas de tráfico, SLA, duración y promedios.
    """
    groups = {}
    for c in calls:
        fecha = c['fecha']
        hora = c['hora']
        franja = f"{hora:02d}:00 - {hora+1:02d}:00"
        cola = c['cola']
        campana = QUEUE_MAPPING.get(cola, f"tip_cola_{cola}")
        
        key = (fecha, franja, campana)
        if key not in groups:
            groups[key] = []
        groups[key].append(c)
        
    aggregated = []
    # Ordenar por fecha, franja y campana
    for key in sorted(groups.keys()):
        fecha, franja, campana = key
        c_list = groups[key]
        
        total = len(c_list)
        aten_list = [c for c in c_list if c['is_aten']]
        ab_list = [c for c in c_list if c['is_ab']]
        
        aten = len(aten_list)
        ab = len(ab_list)
        acd = total
        fuera_hora = 0
        canc = 0
        canc_vm = 0
        
        # Nivel de Servicio (SLA <= 20s)
        aten_sl_plus = len([c for c in aten_list if c['espera'] <= SLA_THRESHOLD_SECONDS])
        aten_sl_minus = aten - aten_sl_plus
        ab_sl_plus = len([c for c in ab_list if c['espera'] <= SLA_THRESHOLD_SECONDS])
        ab_sl_minus = ab - ab_sl_plus
        
        sl_pct = (aten_sl_plus / total) if total > 0 else 1.0
        pct_aten = (aten / total) if total > 0 else 0.0
        pct_ab = (ab / total) if total > 0 else 0.0
        fuera_hora_pct = 0.0
        
        # Tiempos en segundos
        dur_tot_s = sum(c['espera'] + c['conversacion'] for c in c_list)
        aten_tot_s = sum(c['conversacion'] for c in aten_list)
        esp_tot_s = sum(c['espera'] for c in c_list)
        resp_tot_s = sum(c['espera'] for c in aten_list)
        ab_tot_s = sum(c['espera'] for c in ab_list)
        
        asa_s = (resp_tot_s / aten) if aten > 0 else 0.0
        prom_dur_s = (dur_tot_s / total) if total > 0 else 0.0
        prom_esp_s = (esp_tot_s / total) if total > 0 else 0.0
        prom_resp_s = (resp_tot_s / aten) if aten > 0 else 0.0
        prom_aten_s = (aten_tot_s / aten) if aten > 0 else 0.0
        prom_ab_s = (ab_tot_s / ab) if ab > 0 else 0.0
        
        max_dur_s = max([c['espera'] + c['conversacion'] for c in c_list], default=0.0)
        max_resp_s = max([c['espera'] for c in aten_list], default=0.0)
        max_timb_s = max([c['espera'] for c in c_list], default=0.0)
        max_aten_s = max([c['conversacion'] for c in aten_list], default=0.0)
        
        # Conversión a fracción de día para formato Excel h:mm:ss
        def to_excel_time(seconds):
            return seconds / 86400.0
            
        row_dict = {
            1: fecha,                                    # Corte
            2: franja,                                   # franja
            3: campana,                                  # Campaña
            4: total,                                    # Total
            5: None,                                     # Tot. Web
            6: fuera_hora,                               # Fuera Hora
            7: aten,                                     # Aten.
            8: ab,                                       # Ab.
            9: canc,                                     # Canc.
            10: canc_vm,                                 # Canc. VM
            11: None,                                    # Espera Virtual
            12: acd,                                     # ACD
            13: 0,                                       # IVR
            14: 0,                                       # Pura IVR
            15: 0,                                       # Fuera Hora S/ IVR
            16: 0,                                       # Corta
            17: 0,                                       # Larga
            18: 0,                                       # Fant.
            19: 0,                                       # Atend. C/ Agenda
            20: 0,                                       # Ab. C/ Agenda
            21: sl_pct,                                  # % SL
            22: fuera_hora_pct,                          # Fuera Hora %
            23: pct_aten,                                # % atención
            24: pct_ab,                                  # % Ab.
            25: to_excel_time(asa_s),                    # ASA
            26: 0,                                       # LPH
            27: 0,                                       # GPH
            28: to_excel_time(dur_tot_s),                # Tiempo Dur.
            29: 0.0,                                     # Tiempo fuera hora
            30: 0.0,                                     # Tiempo IVR
            31: to_excel_time(esp_tot_s),                # Tiempo Esp.
            32: to_excel_time(resp_tot_s),               # Tiempo Resp.
            33: 0.0,                                     # Tiempo ACD
            34: to_excel_time(esp_tot_s),                # Tiempo Timb.
            35: to_excel_time(aten_tot_s),               # Tiempo atención
            36: 0.0,                                     # Tiempo Conc.
            37: to_excel_time(ab_tot_s),                 # Tiempo Ab.
            38: 0.0,                                     # Tiempo Fant.
            39: 0.0,                                     # Tiempo Ret.
            40: 0.0,                                     # Tiempo Tr.
            41: 0.0,                                     # Tiempo Conf.
            42: to_excel_time(prom_dur_s),               # Promedio tiempo Dur.
            43: 0.0,                                     # Promedio tiempo fuera hora
            44: to_excel_time(prom_esp_s),               # Promedio tiempo espera
            45: to_excel_time(prom_resp_s),              # Promedio tiempo respuesta
            46: 0.0,                                     # Promedio tiempo ACD
            47: to_excel_time(prom_esp_s),               # Promedio tiempo Timb.
            48: to_excel_time(prom_aten_s),              # Promedio tiempo atención
            49: 0.0,                                     # Promedio tiempo Conc.
            50: to_excel_time(prom_ab_s),                # Promedio tiempo Ab.
            51: 0.0,                                     # Promedio tiempo Ret.
            52: to_excel_time(max_dur_s),                # Máx tiempo Dur.
            53: 0.0,                                     # Máx tiempo IVR
            54: to_excel_time(max_resp_s),               # Máx tiempo respuesta
            55: to_excel_time(max_timb_s),               # Máx tiempo Timb.
            56: to_excel_time(max_aten_s),               # Máx. tiempo atención
            57: 0.0,                                     # Máx tiempo Conc.
            58: 0.0,                                     # Máx tiempo Ret.
            59: aten_sl_plus,                            # Aten. SL+
            60: ab_sl_plus,                              # Ab. SL+
            61: 0,                                       # Canc. SL+
            62: aten_sl_minus,                           # Aten. SL-
            63: ab_sl_minus,                             # Ab. SL-
            64: 0,                                       # Canc. SL-
            65: 0.0,                                     # % Busy Ag.
            66: 0.0,                                     # % Att. Ag.
            67: 0.0,                                     # Tiempo Log.
            68: 0.0,                                     # Tiempo Act.
            69: 0.0,                                     # Tiempo Agtes
            70: 0,                                       # Ag./h
            71: 0,                                       # C/ Ret.
            72: 0,                                       # Promedio C/ Ret.
            73: 0,                                       # C/ Conf.
            74: 0,                                       # Promedio C/ Conf.
            75: 0,                                       # Tr.
            76: 0,                                       # Tr. Ag.
            77: 0,                                       # Tr. Camp.
            78: 0,                                       # Tr. Cola
            79: 0,                                       # Tr. Num.
            80: 0,                                       # Promedio Tr.
            81: 0,                                       # Avg Tr. Ag.
            82: 0,                                       # Pro. Tr. Camp.
            83: 0,                                       # Promedio Tr. Cola
            84: 0,                                       # Promedio Tr. Num.
            85: None                                     # Máx agentes Logueados
        }
        aggregated.append(row_dict)
        
    return aggregated

def generate_excel(aggregated_data, template_path, output_path):
    """
    Carga la plantilla Excel oficial preservando encabezados y estilos,
    y escribe los datos agregados.
    """
    print(f"[INFO] Cargando plantilla Excel: {template_path}")
    wb = openpyxl.load_workbook(template_path)
    ws = wb.active
    
    # Extraer estilos del renglón muestra (fila 2)
    sample_styles = []
    for col_idx in range(1, 86):
        c = ws.cell(2, col_idx)
        sample_styles.append({
            'font': copy(c.font),
            'border': copy(c.border),
            'fill': copy(c.fill),
            'number_format': c.number_format,
            'alignment': copy(c.alignment)
        })
        
    # Limpiar filas existentes a partir de la fila 2
    max_row = ws.max_row
    if max_row >= 2:
        ws.delete_rows(2, max_row - 1)
        
    print(f"[INFO] Escribiendo {len(aggregated_data)} registros agregados en el layout...")
    
    for row_num, row_data in enumerate(aggregated_data, start=2):
        for col_idx in range(1, 86):
            val = row_data.get(col_idx, None)
            cell = ws.cell(row=row_num, column=col_idx, value=val)
            
            # Aplicar estilo de plantilla
            st = sample_styles[col_idx - 1]
            if st['font']: cell.font = st['font']
            if st['border']: cell.border = st['border']
            if st['fill']: cell.fill = st['fill']
            if st['number_format']: cell.number_format = st['number_format']
            if st['alignment']: cell.alignment = st['alignment']
            
    # Guardar archivo compilado
    wb.save(output_path)
    print(f"[EXITO] Archivo generado correctamente en: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Conversor ETL de llamadas N2A a Layout inConcert TIP México")
    parser.add_argument('--inputs', nargs='*', help="Rutas a los archivos CSV/XLSX de llamadas de N2A")
    parser.add_argument('--template', help="Ruta al archivo plantilla layout_data_repli.xlsx")
    parser.add_argument('--output', help="Ruta de destino para el archivo compilado")
    parser.add_argument('--start-date', help="Fecha de inicio (YYYY-MM-DD), ej. 2026-10-19")
    parser.add_argument('--end-date', help="Fecha de fin (YYYY-MM-DD), ej. 2026-10-23")
    
    args = parser.parse_args()
    
    # Rutas por omisión inteligentes en el entorno del usuario
    downloads = os.path.expanduser(r"~\Downloads")
    
    if args.inputs:
        csv_files = args.inputs
    else:
        # Detectar automáticamente los archivos de corte en Descargas
        default_files = [
            os.path.join(downloads, "Llamdas 19-21 oct TIP.xlsx"),
            os.path.join(downloads, "llamadas (3).csv"),
            os.path.join(downloads, "llamadas_2026-10-19_a_2026-10-20.csv"),
            os.path.join(downloads, "llamadas.csv")
        ]
        csv_files = [f for f in default_files if os.path.exists(f)]
        if not csv_files:
            print("[ERROR] No se encontraron archivos de llamadas predeterminados en Descargas.")
            sys.exit(1)
            
    template_file = args.template or os.path.join(downloads, "layout_data_repli.xlsx")
    if not os.path.exists(template_file):
        print(f"[ERROR] No se encontró la plantilla en: {template_file}")
        sys.exit(1)
        
    output_file = args.output or os.path.join(downloads, "layout_data_repli_19_al_23_oct_2026.xlsx")
    
    start_d = datetime.date.fromisoformat(args.start_date) if args.start_date else datetime.date(2026, 10, 19)
    end_d = datetime.date.fromisoformat(args.end_date) if args.end_date else datetime.date(2026, 10, 23)
    
    print(f"[INFO] Compilando rango semanal: {start_d} al {end_d}")
    
    # 1. Cargar y normalizar llamadas con deduplicación y filtro de fecha
    calls = load_all_calls(csv_files, start_date=start_d, end_date=end_d)
    if not calls:
        print("[ERROR] No se recuperaron llamadas válidas para procesar.")
        sys.exit(1)
        
    # 2. Agregar por franja horaria y campaña
    aggregated = aggregate_by_interval(calls)
    print(f"[OK] Se generaron {len(aggregated)} franjas horarias x campaña.")
    
    # 3. Escribir en Excel oficial
    generate_excel(aggregated, template_file, output_file)

if __name__ == "__main__":
    main()
