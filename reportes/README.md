# 📊 Histórico de Reportes Semanales de Operaciones | TIP México

Este repositorio mantiene el archivo histórico de los reportes oficiales compartidos con **Laura Mercado (TIP México)** y su respectivo soporte documental de conmutador y telefonía.

---

## 🗂️ Estructura del Repositorio

```text
tip-direccion/reportes/
├── plantilla/
│   └── layout_data_repli.xlsx                <- Plantilla oficial inConcert requerida por TIP
│
├── Semana-01_19-al-23-Oct-2026/
│   ├── entregables/
│   │   ├── layout_data_repli_19_al_23_oct_2026.xlsx  <- Reporte en formato inConcert entregado
│   │   └── slide_semanal_tip_19_al_23_oct_2026.pdf   <- Slide ejecutivo semanal (PDF)
│   └── soporte_origen/
│       ├── Llamdas 19-21 oct TIP.xlsx                <- CDR inicial de llamadas
│       ├── llamadas_22_al_27_oct.csv                 <- CDR de llamadas entrantes
│       ├── llamadas-salientes.csv                    <- Detalle de llamadas outbound
│       ├── agentes_corte_27_oct.csv                  <- Métricas de agentes
│       └── breaks_corte_27_oct.csv                   <- Auxiliares de WFM
│
└── Semana-02_26-al-30-Oct-2026/
    ├── entregables/
    │   └── layout_data_repli_26_al_30_oct_2026.xlsx  <- Reporte oficial en formato inConcert (139 llamadas)
    └── soporte_origen/
        ├── llamadas.csv                              <- CDR bruto llamadas entrantes (Fuente de verdad)
        ├── llamadas-salientes.csv                    <- 88 llamadas salientes de seguimiento (Salesforce/Siniestros)
        ├── trafico.csv                               <- Consolidado diario de tráfico y SLA del conmutador
        ├── no-contesto-llamadas.csv                  <- Detalle de eventos RONA en colas
        ├── no-contesto-agentes.csv                   <- Resumen de desatención / auto-pausa por asesor
        ├── agentes.csv                               <- Ocupación, productividad y AHT por asesor
        ├── breaks.csv                                <- 108 pausas auxiliares (Lunch, Break, Restroom)
        └── sesiones.csv                              <- Inicios, cierres de sesión e IPs de agentes
```

---

## ⚙️ Reglas de Generación y Compilador ETL

* **Motor ETL:** `tip-direccion/scripts/convertir_layout_tip.py`
* **Mapeo Oficial Canónico de Colas:**
  * `8001` (PBX 9001): `tip_general` ([TIP General] · 800 908 6700)
  * `8002` (PBX 9002): `tip_bitcar` ([Bitcar] · 800 999 2136)
  * `8003` (PBX 9003): `tip_ofs` ([OFS] · 55 5093 7300)
  * `8004` (PBX 9004): `tip_jac` ([JAC] · 800 649 0751)
  * `8005` (PBX 9005): `tip_kia` ([KIA] · 800 999 1151)
  * `8006` (PBX 9006): `tip_mg` ([MG] · 800 999 2057)
  * `8007` (PBX 9007): `tip_gco` ([GCO] · 800 967 0527)
  * `8008` (PBX 9008): `tip_chirey` ([Chirey] · 800 649 0084)
  * `8009` (PBX 9009): `tip_carnot` ([Carnot] · 800 122 7668)
* **Entregables para Laura Mercado:** Únicamente los archivos contenidos dentro de las carpetas `entregables/`. Los archivos dentro de `soporte_origen/` son de control, auditoría interna de Telat y gobernanza técnica.
