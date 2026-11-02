# Telat Group | Operaciones TIP México (`tip-direccion`)

Repositorio central de control operativo, inteligencia de tráfico telefónico, entregables ejecutivos y herramientas ETL para la cuenta corporativa de **TIP México**.

---

## 🏛️ 1. Arquitectura del Repositorio

El proyecto se encuentra organizado bajo una estructura modular que separa la presentación ejecutiva, la documentación técnica, los activos gráficos, el histórico de reportes y las herramientas de procesamiento:

```text
tip-direccion/
├── .gitignore                                   # Filtros y exclusiones de control de versiones
├── README.md                                    # Guía canónica del repositorio y arquitectura operativa
├── index.html                                   # Dashboard ejecutivo institucional para Dirección de TIP
│
├── assets/
│   └── img/
│       └── mapa_hubs.png                        # Infografía oficial de sedes binacionales de Telat
│
├── docs/
│   ├── PENDIENTES.md                            # Bitácora de acuerdos, pendientes y hoja de ruta
│   └── interno/
│       └── brief-tecnico-telefonia.html         # Pliego técnico y alineación de telefonía cloud
│
├── reportes/
│   ├── README.md                                # Documentación de entregables y datos fuente
│   ├── plantilla/
│   │   └── layout_data_repli.xlsx               # Plantilla oficial requerida por TIP México (85 columnas)
│   ├── Semana-01_19-al-23-Oct-2026/
│   │   ├── entregables/                         # Excel oficial compilado y lámina ejecutiva semanal
│   │   └── soporte_origen/                      # Archivos CDR brutos y auxiliares de la primera semana
│   └── Semana-02_26-al-30-Oct-2026/
│       ├── entregables/                         # Excel oficial compilado de la segunda semana
│       └── soporte_origen/                      # Archivos CDR consolidados, RONA y sesiones de conmutador
│
└── scripts/
    ├── convertir_layout_tip.py                  # Motor ETL en Python para compilación de franjas horarias
    └── ejecutar_compilador_tip.ps1              # Lanzador interactivo y tolerante en PowerShell
```

---

## 📞 2. Catálogo Oficial Homologado de Telefonía

La cuenta opera con 9 líneas telefónicas (8 líneas 800 de acceso nacional y 1 línea local directa CDMX). Cada línea está asociada a una cola del conmutador cloud (serie 8000) y a un desvío o transferencia PBX (serie 9000):

| Cola Conmutador | Desvío PBX | Identificador Canónico | Nombre de Marca / Cuenta | Número de Contacto |
| :---: | :---: | :--- | :--- | :---: |
| **8001** | **9001** | `tip_general` | TIP General (Conmutador Principal) | 800 908 6700 |
| **8002** | **9002** | `tip_bitcar` | Bitcar | 800 999 2136 |
| **8003** | **9003** | `tip_ofs` | OFS (Línea Local CDMX) | 55 5093 7300 |
| **8004** | **9004** | `tip_jac` | JAC | 800 649 0751 |
| **8005** | **9005** | `tip_kia` | KIA | 800 999 1151 |
| **8006** | **9006** | `tip_mg` | MG | 800 999 2057 |
| **8007** | **9007** | `tip_gco` | GCO | 800 967 0527 |
| **8008** | **9008** | `tip_chirey` | Chirey | 800 649 0084 |
| **8009** | **9009** | `tip_carnot` | Carnot | 800 122 7668 |

*Extensiones de Asesores:* Las extensiones físicas de softphone Bria en el piso de operaciones corresponden a la serie 2000 (Supervisor: 2001; Asesores en piso: 2002 a 2007).

*Transferencia a Siniestros:* Ante llamadas canalizadas a siniestros, el procedimiento estandarizado es la marcación rápida **`237`** en softphone o la transferencia directa a Cabina de Siniestros al número **`55 4195 6614`**.

---

## ⚙️ 3. Ejecución del Motor ETL (`scripts/`)

El motor ETL procesa los registros CDR brutos provenientes del conmutador y genera el archivo Excel en formato homologado de 85 columnas (`layout_data_repli.xlsx`), agrupado por fecha, franja horaria de 60 minutos y campaña.

### 3.1 Uso con el lanzador PowerShell (`ejecutar_compilador_tip.ps1`)

El lanzador detecta automáticamente el intérprete de Python en el sistema y aplica codificación UTF-8:

```powershell
# Compilar Semana 2 por omisión (último corte cerrado)
.\scripts\ejecutar_compilador_tip.ps1

# Compilar Semana 1 (19 al 23 de octubre)
.\scripts\ejecutar_compilador_tip.ps1 -Semana 1

# Compilar archivos específicos
.\scripts\ejecutar_compilador_tip.ps1 -Inputs "reportes\Semana-02_26-al-30-Oct-2026\soporte_origen\llamadas.csv" -Output "reportes\Semana-02_26-al-30-Oct-2026\entregables\layout_data_repli_26_al_30_oct_2026.xlsx"
```

### 3.2 Uso directo con Python (`convertir_layout_tip.py`)

```powershell
# Compilación rápida de Semana 1
python scripts/convertir_layout_tip.py --semana 1

# Compilación rápida de Semana 2
python scripts/convertir_layout_tip.py --semana 2

# Compilación personalizada con argumentos
python scripts/convertir_layout_tip.py --inputs "ruta/archivo_llamadas.csv" --template "reportes/plantilla/layout_data_repli.xlsx" --output "ruta/salida.xlsx" --start-date 2026-10-26 --end-date 2026-10-30
```

---

## 🔗 4. Repositorios Vinculados en el Workspace

La operación integral de TIP México se articula a través de cuatro proyectos interconectados:

1. **`tip-direccion`** (este repositorio): Dirección de operaciones, informes ejecutivos, reportería semanal y ETL de telefonía.
2. **`tip-adherencia-wfm`**: Sistema de control y monitoreo de adherencia WFM para turnos de 7 horas en Google Apps Script y web frontend (20 min comida, 15 min break, 11 min baño, 46 min auxiliares totales).
3. **`tip-base-conocimiento`**: Portal operativo y catálogo de 126 casos de uso y 37 plantillas para asesores en atención al cliente y transferencias críticas (Salesforce / ATC).
4. **`tip-state-controller`**: Tablero de control de estados en tiempo real con integración a Google Sheets para supervisión en piso, métricas de ocupación y control de pausas.

---

## 🛡️ 5. Gobernanza Corporativa y Política de Marca Blanca

De acuerdo con las políticas corporativas de Telat Group:
* **Proveedor único ante el cliente:** Telat Group es el responsable integral ante TIP México. Las plataformas de telecomunicaciones y carrier tecnológico operan bajo esquema estricto de marca blanca (white-label).
* **Gobernanza de Operaciones:** La dirección y seguimiento del proyecto está a cargo de **Mauricio Cruz** (Director de Operaciones, en funciones de Dirección Comercial) y **Ricardo García** (Subdirector de Operaciones). Enlace y telecomunicaciones a cargo de **Ricardo Morales** (Gerente de TI, Enlace y Comunicaciones).
* **Contactos del Cliente:** Laura Lizbeth Mercado Zepeda y Alejandrina Sánchez (Atención y Experiencia del Cliente TIP México).
