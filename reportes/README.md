# 📊 Histórico de Reportes Semanales de Operaciones | TIP México

Este repositorio mantiene el archivo histórico de los reportes oficiales compartidos con **Laura Mercado (TIP México)** y su respectivo soporte documental de conmutador y telefonía.

---

## 🗂️ Estructura del Módulo de Reportes

```text
tip-direccion/reportes/
├── README.md
├── plantilla/
│   └── layout_data_repli.xlsx                <- Plantilla oficial de operaciones requerida por TIP
│
├── Semana-01_19-al-23-Oct-2026/
│   ├── entregables/
│   │   ├── layout_data_repli_19_al_23_oct_2026.xlsx  <- Reporte oficial compilado (167 llamadas únicas, 90 franjas)
│   │   ├── slide_semanal_tip_19_al_23_oct_2026.pdf   <- Lámina ejecutiva semanal (PDF)
│   │   └── slide_semanal_tip_19_al_23_oct_2026.html  <- Código fuente HTML de la lámina ejecutiva
│   └── soporte_origen/
│       ├── llamadas_19_al_21_oct.xlsx                <- CDR inicial de llamadas (19 al 21 de octubre)
│       ├── llamadas_22_al_27_oct.csv                 <- CDR de llamadas entrantes (22 al 27 de octubre)
│       ├── llamadas-salientes.csv                    <- Detalle de llamadas outbound de seguimiento
│       ├── agentes_corte_27_oct.csv                  <- Métricas de agentes
│       └── breaks_corte_27_oct.csv                   <- Auxiliares de WFM
│
├── Semana-02_26-al-30-Oct-2026/
│   ├── entregables/
│   │   └── layout_data_repli_26_al_30_oct_2026.xlsx  <- Reporte oficial compilado (139 llamadas únicas, 86 franjas)
│   └── soporte_origen/
│       ├── llamadas.csv                              <- CDR consolidado de llamadas entrantes (Fuente de verdad)
│       ├── llamadas-salientes.csv                    <- 88 llamadas salientes de seguimiento (Salesforce / Siniestros)
│       ├── trafico.csv                               <- Consolidado diario de tráfico y SLA del conmutador
│       ├── no-contesto-llamadas.csv                  <- Detalle de eventos RONA en colas
│       ├── no-contesto-agentes.csv                   <- Resumen de desatención / auto-pausa por asesor
│       ├── agentes.csv                               <- Ocupación, productividad y AHT por asesor
│       ├── breaks.csv                                <- 108 pausas auxiliares (Lunch, Break, Restroom)
│       └── sesiones.csv                              <- Inicios, cierres de sesión e IPs de agentes
│
└── Semana-03_02-al-06-Nov-2026/
    ├── entregables/
    │   └── layout_data_repli_02_al_06_nov_2026.xlsx  <- Reporte oficial compilado (568 llamadas únicas, 152 franjas, 82.0% atención)
    └── soporte_origen/
        ├── llamadas.csv                              <- CDR consolidado de llamadas entrantes (Fuente de verdad, 568 reg.)
        ├── llamadas-salientes.csv                    <- 140 llamadas salientes de seguimiento (Salesforce / Siniestros / Callbacks)
        ├── trafico.csv                               <- Consolidado diario de tráfico y SLA del conmutador
        ├── no-contesto-llamadas.csv                  <- Detalle de eventos RONA en colas
        ├── no-contesto-agentes.csv                   <- Resumen de desatención / auto-pausa por asesor
        ├── agentes.csv                               <- Ocupación, productividad y AHT por asesor
        ├── breaks.csv                                <- Pausas auxiliares
        └── sesiones.csv                              <- Inicios, cierres de sesión e IPs de agentes
```

---

## ⚙️ Reglas de Generación y Compilador ETL

* **Motor ETL:** `tip-direccion/scripts/convertir_layout_tip.py`
* **Lanzador PowerShell:** `tip-direccion/scripts/ejecutar_compilador_tip.ps1`
* **Catálogo Oficial Homologado de Colas y Desvíos PBX:**
  * `8001` / `9001`: `tip_general` ([TIP General] | 800 908 6700)
  * `8002` / `9002`: `tip_bitcar` ([Bitcar] | 800 999 2136)
  * `8003` / `9003`: `tip_ofs` ([OFS] | 55 5093 7300)
  * `8004` / `9004`: `tip_jac` ([JAC] | 800 649 0751)
  * `8005` / `9005`: `tip_kia` ([KIA] | 800 999 1151)
  * `8006` / `9006`: `tip_mg` ([MG] | 800 999 2057)
  * `8007` / `9007`: `tip_gco` ([GCO] | 800 967 0527)
  * `8008` / `9008`: `tip_chirey` ([Chirey] | 800 649 0084)
  * `8009` / `9009`: `tip_carnot` ([Carnot] | 800 122 7668)
* **Entregables para Laura Mercado:** Únicamente los archivos contenidos dentro de las carpetas `entregables/`. Los archivos dentro de `soporte_origen/` son de control, auditoría interna de Telat y gobernanza técnica.
