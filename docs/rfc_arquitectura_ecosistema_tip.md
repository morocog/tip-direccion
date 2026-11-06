# RFC: Arquitectura y Consolidación del Ecosistema Operativo TIP México

**Documento:** RFC-TIP-2026-11-05-v2  
**Autor:** Ricardo García (Subdirección de Operaciones Telat) / Antigravity  
**Fecha:** 2026-11-05  
**Estado:** Dictaminado y Aprobado tras Revisión Adversarial EGM (Elephant-Goldfish Model)  
**Alcance:** `tip-state-controller`, `tip-base-conocimiento`, `tip-adherencia-wfm`, integración operativa con N2A y Salesforce.

---

## 1. Objetivos y No-Objetivos (Goals & Non-Goals)

### 1.1 Objetivos (Goals)
1. **Reducción de fatiga operativa:** Disminuir a un máximo de 2 herramientas Telat en el puesto de trabajo del agente (`contact.n2a.mx/agente` para telefonía y pausas; `tip-base-conocimiento` para consulta rápida de procedimientos y plantillas).
2. **Eliminación del estado dividido (*Split-Brain*):** Establecer a Net2Alliance (N2A) como la **única fuente de verdad** para sesiones, colas, tiempos en llamada y pausas auxiliares.
3. **Cero falsas alarmas:** Prohibir disparos de alertas a Google Chat desde scripts ciegos a la señalización SIP. Las alarmas de adherencia se basan exclusivamente en datos oficiales del conmutador o auditorías de WFM.
4. **Agilidad en consulta:** Integrar el atajo de teclado global `Ctrl+K` en la Base de Conocimiento para acceso instantáneo a fichas operativas.
5. **Auditoría matemática de jornada:** Asegurar que `tip-adherencia-wfm` aplique estrictamente la matriz canónica de 7:00 / 7:30 hrs (46 minutos totales de auxiliares: 20 min comida, 15 min break, 11 min baño) sobre los CSVs oficiales.

### 1.2 No-Objetivos (Non-Goals)
1. **No construir un monolito en Google Apps Script:** Queda descartado fusionar la Base de Conocimiento con el Controlador de Estados en un solo script, protegiendo la cuota de 30 ejecuciones concurrentes de Google Workspace.
2. **No crear un motor de estados paralelo:** No se sincronizará Google Sheets con el conmutador por webhooks entrantes para evitar problemas de concurrencia y latencia.
3. **No alterar el canal de soporte WFM:** WFM no auditará hojas de cálculo internas; continúa procesando los CSVs canónicos del carrier (`breaks.csv`, `asistencias.csv`).

---

## 2. Contexto Operativo y Causa Raíz

### 2.1 El Ecosistema Actual y su Patología
Actualmente, los asesores de TIP México operan con 4 aplicaciones abiertas:
1. `contact.n2a.mx/agente` (Telefonía cloud y auxiliar oficial de N2A).
2. Salesforce Service Cloud (Bandeja de tickets asignada por TIP México).
3. `tip-base-conocimiento` (126 fichas de trámites y 37 plantillas).
4. `tip-state-controller` (Herramienta legacy en Google Sheets con botones de estado).

### 2.2 Diagnóstico de la Falla Estructural
- `tip-state-controller` nació antes de la consolidación de la consola web de N2A.
- Al no tener integración CTI bidireccional con Bria, desconoce el estado telefónico del asesor. Como se comprobó en el Ticket #225674 resuelto con N2A, si un asesor presiona comida durante una llamada, N2A retiene el conteo hasta colgar (`CALL_END`). `tip-state-controller` arranca el contador en el instante del clic.
- Intentar enviar alertas a Google Chat desde `tip-state-controller` provocaría **falsas alarmas sistemáticas** en el canal de supervisores denunciando agentes que en realidad estaban atendiendo llamadas.
- La persistencia en Google Sheets carece de locks transaccionales (`LockService`), saturando cuotas de lectura por polling de dashboard.

---

## 3. Decisión Canónica: Desacoplamiento Pragmático (Opción 2 Aprobada)

Se dictamina la **adopción formal de la Opción 2** con las directrices surgidas del ciclo de auditoría EGM:

```
[ Agente TIP ] ──────────────────────────┬──────────────────────────┐
                                         ▼                          ▼
                         [ contact.n2a.mx/agente ]      [ tip-base-conocimiento ]
                         • Teléfono Softphone Bria      • Consulta con Ctrl+K
                         • Botones Pausa Oficial        • 126 fichas en memoria JS
                         • Cronómetros Oficiales        • Ingesta IA con Gemini
                         (Única Fuente de Verdad)       (Cero lógica de estados)

[ Supervisor TIP ] ──────────────────────┬──────────────────────────┐
                                         ▼                          ▼
                        [ contact.n2a.mx/supervisor ]     [ tip-adherencia-wfm ]
                        • Muro de Piso en Vivo           • Dropzone de CSVs N2A
                        • Monitoreo y RONA               • Cruce Matriz 7h (46m)
                        • Capturas para Laura Mercado    • Exportación PNG oficial
```

### 3.1 Resoluciones Arquitectónicas Específicas

1. **Deprecación Formal de `tip-state-controller`:**
   - Se apaga el backend transaccional en Google Sheets y se instruye a los agentes a gestionar sus auxiliares únicamente en `contact.n2a.mx/agente`.
   - Se cancela la integración de webhooks a Google Chat desde este aplicativo para evitar alarmas engañosas por falta de sincronización SIP.
2. **Base de Conocimiento Enfocada (`tip-base-conocimiento`):**
   - Se implementa el atajo `Ctrl+K` para enfocar `#txtBuscar` instantáneamente.
   - Se mantiene la búsqueda 100% en cliente (cero latencia, cero gasto de tokens).
   - Se mantiene Gemini 2.5 Flash exclusivamente para la ingesta de circulares y PDFs en el módulo administrativo.
   - Siguiendo el principio YAGNI de Zoom-Out, **no se agregará ningún cronómetro paralelo en la interfaz**; el agente consulta sus tiempos directamente en su barra oficial de N2A.
3. **Control de Adherencia WFM (`tip-adherencia-wfm`):**
   - Se ratifica como la herramienta oficial de auditoría post-jornada.
   - Aplica estrictamente la matriz canónica de 7:00 / 7:30 hrs:
     - Comida: 20 min (1,200s).
     - Break: 15 min (900s).
     - Baño: 11 min (660s).
     - Total auxiliares autorizados: 46 min (2,760s).

---

## 4. Alternativas Rechazadas y Justificación Técnica

### Opción 1: Unificación Monolítica en Google Apps Script
- **Motivo de Rechazo:** Acoplamiento severo. Apps Script cuenta con un límite de 30 ejecuciones concurrentes. El polling continuo de estados en vivo del muro de piso consumiría la cuota del dominio, congelando la Base de Conocimiento durante las llamadas de los agentes. Además, perpetúa la doble captura manual.

### Opción 3: Status Quo Optimizado
- **Motivo de Rechazo:** Mantiene activa la máquina de estados fantasma en Google Sheets, obliga al agente a operar 4 pestañas y generaría falsos positivos en las alertas de Google Chat debido a la falta de señalización CTI.

---

## 5. Plan de Transición y Mitigación Operativa

1. **Entregables Contractuales de Supervisión (Requerimiento 9):**
   - La supervisora (Miriam Totomoch) validará que las capturas de estado de las 08:30, 10:00 y 11:00 am solicitadas por Laura Mercado (TIP México) se extraigan directamente desde el tablero visual de `contact.n2a.mx/supervisor`.
2. **Capacitación Breve a Piso:**
   - Notificar a los 5 asesores y supervisión que su único panel de auxiliares es la consola de N2A, retirando el enlace de `tip-state-controller` de sus marcadores.
3. **Alineación con WFM:**
   - Confirmar con Workforce Management que la calibración de 46 minutos en `tip-adherencia-wfm` coincide con el archivo semanal consolidado que se entrega a operaciones.
