# 📌 PENDIENTES & HOJA DE RUTA, TIP DIRECCIÓN & TELEFONÍA CLOUD

Este documento mantiene el estado de verificación, roadmap, acuerdos y deuda técnica para la cuenta corporativa de **TIP México** y la infraestructura de telecomunicaciones cloud.

---

## 🏛️ 0. Arquitectura Canónica & Directrices de Fase 1 (Septiembre - Octubre 2026)

* **Fase 1 Estricta, Cero Inteligencia Artificial & Plantilla Ajustada (6 FTEs):** La operación inicial para TIP México se basa **exclusivamente en agentes humanos dedicados en piso (6 FTEs)** (5 agentes de piso + 1 supervisor/híbrido) atendiendo 2 canales: Voz (2,800 llamadas/mes) y Correo (500 tickets/mes). Queda estrictamente excluida cualquier automatización con IA en esta primera fase.
* **Exclusión de Canal WhatsApp (Acuerdo Comercial TIP):** El cliente TIP México determinó retener la atención del canal WhatsApp directamente en su plataforma Zenvia; **Telat NO operará WhatsApp**, concentrando el 100% de la plantilla de 6 FTEs en Voz y Correo/Salesforce.
* **Gobernanza White-Label Absoluta:** De cara a TIP México, **Telat Group es el proveedor único e integral** tanto del talento BPO como de la plataforma tecnológica y de telecomunicaciones. TIP México no debe tener conocimiento de la existencia del carrier tecnológico. El carrier actúa exclusivamente como partner tecnológico back-to-back con Telat.
* **Gobernanza Comercial y de Operaciones:** La dirección comercial y operativa del proyecto está a cargo de **Mauricio Cruz** (Director de Operaciones, en funciones de Dirección Comercial). La subdirección operativa está a cargo de **Ricardo García** (Subdirector de Operaciones). Enlace tecnológico y telecomunicaciones liderado por **Ricardo Morales** (Gerente de TI, Enlace y Comunicaciones).
* **Infraestructura de Telecomunicaciones Cloud (Voz & Telecom):** Se provee la suite unificada en conmutador cloud que abarca:
  1. Troncales SIP y softphones para telefonía de voz (2,800 llamadas/mes, 6 agentes concurrentes).
  2. Mapeo y preservación de cabeceras DNIS para las 9 líneas telefónicas (8 líneas 800 y 1 local CDMX).
  3. Call Intelligence & Analytics para grabación y auditoría de voz al 100%.
  4. (Nota: Queda cancelado el requerimiento de broker/conector de WhatsApp Business API).

---

## 🔴 1. VERIFICACIONES PENDIENTES EN CALIENTE (seguras, no urgentes)

> 💡 **Validación Rápida con 1 Clic en Obsidian:** Haz clic directamente sobre la casilla `[ ]` para marcarla como `[x]` una vez probada en producción.

- [x] **P-01: Generación de Pliego Técnico para Telefonía Cloud (v1.3):** Documento `docs/interno/brief-tecnico-telefonia.html` calibrado en 2 páginas Carta para PDF con 6 FTEs y exclusión de WhatsApp. (Validado)
- [x] **P-02: Alineación de Alianza Estratégica:** Definición de roles (Telat BPO = 6 agentes en piso; Telecomunicaciones Cloud = DIDs, Cloud CommServer, Call Intelligence). (Validado)
- [x] **P-03: Gobierno de Memoria:** Registro permanente de **Mauricio Cruz** (Director de Operaciones, en funciones de Dirección Comercial), **Ricardo García** (Subdirector de Operaciones), **Ricardo Morales** (Gerente de TI, Enlace y Comunicaciones) y contrapartes de carrier en gobernanza interna. (Validado)
- [x] **P-04: Pruebas de Telefonía Exitosas con TIP:** Validación de viabilidad de desvío (call forwarding) a través de troncales SIP hacia cabeceras de conmutador cloud. (Validado)
- [x] **P-05: Definición de Requerimientos Técnicos para TIP México:** Formulación de solicitud técnica precisa (inventario de 800 y DNIS en SIP Header). (Validado)

---

## 🟡 2. Respuestas Oficiales del Cliente (TIP México)
- [x] **Inventario de Líneas 800 & Locales Recibido:** Mapeo de 9 líneas de entrada oficiales (8 líneas 800 y 1 línea local directa CDMX):
  - `Bitcar`: **800 999 2136**
  - `OFS`: **55 5093 7300** (Línea local CDMX)
  - `CARNOT`: **800 122 7668**
  - `CHIREY`: **800 649 0084**
  - `JAC`: **800 649 0751**
  - `MG`: **800 999 2057**
  - `KIA`: **800 999 1151**
  - `TIP MÉXICO`: **800 908 6700** (Conmutador General)
  - `GCO`: **800 967 0527**
- [x] **Gobernanza de IVR Aclarada (TIP México administra su IVR):**
  - TIP aloja y gestiona su propio IVR de bienvenida (Menú: *Opción 1: Atención a Clientes* / *Opción 9: Cabina de Siniestros*).
  - **Alcance Operativo TELAT:** TELAT atiende exclusivamente **Opción 1** (Siniestros queda fuera del alcance y lo atiende TIP vía transferencia a Cabina).
  - **TELAT NO tiene que replicar ni administrar el IVR de bienvenida.** TIP coordina el desvío directo hacia la troncal de TELAT preservando el identificador.
- [x] **Confirmación de Mapeo de 9 Líneas 800 & Locales:** Inventario de las 9 líneas canónicas totalmente confirmado y acordado para aprovisionamiento.
- [x] **Exclusión de WhatsApp Acordada con TIP:** TIP retiene el canal WhatsApp en su plataforma Zenvia; Telat no lo operará ni aprovisionará licencias.
- [x] **Gestión de Correo Electrónico (Salesforce Service Cloud):**
  - La atención de `contactcenter@tipmexico.com` NO se gestiona en bandeja de correo tradicional, sino mediante tickets en **Salesforce Service Cloud** provisto por TIP con accesos y plantillas tras capacitación.
  - **Estatus Operativo:** Laura Mercado y el equipo directivo de TIP México auditan y gestionan directamente los correos/casos dentro de Salesforce; Telat NO requiere generar ni entregar reportes de tickets por este canal.
- [x] **Contratación y Formalización Operativa de Plantilla (Completado 20-Oct-2026):** La formalización y firma de contratos de los agentes en piso quedó completada desde el segundo día de operaciones (20 de octubre).
- [x] **Dimensionamiento Económico Consolidado (6 FTEs):** Ajuste de estructura comercial a 6 posiciones humanas en vivo acordado con Dirección de Operaciones y Comercial.
- [x] **Arranque Oficial de Capacitación Presencial (Lunes 5 de Octubre, 10:00 a.m.):**
  - **Instructora:** Laura Mercado (`laura.mercado@tipmexico.com`) de TIP México impartió el curso presencial en instalaciones de TELAT.
  - **Horario Oficial:** Lunes a Viernes de 10:00 a.m. a 5:00 p.m.
  - **Gobernanza Operativa:** Alineación directa liderada por **Mauricio Cruz** (Operations Director) en coordinación con Ricardo García (Subdirector de Operaciones), Ricardo Morales (TI) y Lic. Julio Torres (Legal).
- [x] **Estrategia y Contingencia de Talento: Arranque con 7 Candidatos TELAT:**
  - Capacitación arrancó con 7 candidatos nuevos contratados directamente por TELAT bajo acuerdo de Mauricio Cruz y Laura Mercado.

---

## 📞 3. Implementación PBX, Telecomunicaciones & Ventana de Corte (Octubre 2026)
- [x] **Interconexión PBX y Troncal a Servidor Propio (14-Oct-2026):** Ricardo Morales confirmó la migración exitosa de la troncal SIP a servidor propio con IP definitiva (mismas credenciales). Cero pendientes de interconexión física/red.
- [x] **Aprovisionamiento y Prueba de 9 Desvíos PBX de Cola (9001 a 9009):** Desvíos y transferencias de colas operativas y probadas en ambos sentidos: saliente Telat -> TIP y entrante TIP -> Telat recibida exitosamente en el desvío 9005 (KIA). Las extensiones físicas de softphone Bria asignadas a los asesores corresponden a la serie 2000 (Supervisor: 2001; Asesores: 2002 a 2007).
- [x] **Migración Total de las 9 Líneas Telefónicas (Completado 30-Oct-2026, 18:40 h):** Las 8 líneas secundarias (Bitcar, OFS, CARNOT, CHIREY, JAC, MG, KIA, GCO) migraron inicialmente a la troncal Telat, y la migración definitiva del Conmutador General de TIP México (800 908 6700) se completó con éxito el viernes 30 de octubre a las 18:40 h aproximadamente. El 100% de las 9 líneas canónicas opera en producción bajo la troncal Telat.
- [x] **Resolución y Captura de Caller ID / DNIS (Resuelto en Operación Semanas 1 y 2):** Se validó que el conmutador captura e inyecta en los registros CDR el número de origen del cliente (columna Número) y la cola de entrada específica (8002, 8003, etc.). Se mantiene monitoreo en softphones Bria para asegurar que el agente reconozca la marca y el speech adecuado.
- [x] **Horario de Operación Oficial (Lunes a Viernes / Sábados Descartados):** Laura Mercado y la dirección de Operaciones confirmaron que el servicio opera exclusivamente de Lunes a Viernes en sus horarios establecidos. Los sábados quedan formalmente descartados (tráfico residual de ~10 llamadas y áreas resolutivas de TIP cerradas; carece de lógica operativa). WFM y todas las áreas internas de Telat ya fueron debidamente actualizadas.
- [x] **Música y Audio Institucional en Espera Operativo (Resuelto 16-Oct-2026):** El audio y música de espera quedó configurado y activo desde las pruebas iniciales del 16 de octubre y validado en el arranque de producción. Cero pendientes en este rubro.
- [x] **Activación de Cuentas de Plataforma y Protocolo 2FA (Resuelto 28-Oct-2026):** Cuentas de agentes activas en Salesforce Service Cloud. El protocolo 2FA quedó formalmente resuelto mediante la entrega de una tablet física corporativa dedicada entregada por Ricardo Morales (TI), eliminando el uso de celulares personales en piso de operaciones.
- [x] **Entrega de Dispositivo Físico 2FA por Ricardo Morales (Resuelto 28-Oct-2026):** Jatzyri Yepez (Gerente de Capacitación) notificó la necesidad de hardware para la autenticación 2FA de los agentes en TIP. Se entregó una tablet dedicada específicamente para la campaña de TIP México (liberando el equipo en préstamo de Carvana).
- [ ] **Homologación de Marcación Interna (Serie 7100+):** Confirmar regla general de extensiones de cuatro dígitos que inicien con 7 propuesta por Telat.

---

## 🔵 4. Siguientes Pasos de Telecomunicaciones & Conmutador Cloud
- [x] **Mapeo de 9 Líneas Integrado:** Cabeceras y DIDs listos para aprovisionamiento de troncal SIP con preservación de DNIS.
- [ ] **Aprovisionamiento Final de Troncal y DIDs:** Ejecutar la configuración de softphones adicionales una vez formalizada la firma del contrato con TIP.
- [ ] **Requerimiento 1: Blaster Interactivo de Llamadas Salientes (Ticket Abierto, En Espera de Base TIP):**
  - **Estatus:** Ticket técnico abierto en soporte del conmutador cloud.
  - **Bloqueante / Próximo Paso:** En espera de que Laura Mercado (TIP Corporativo) proporcione la base de datos de clientes e información de la campaña de trámites de tenencias.
  - **Mecanismo:** El blaster ejecutará las llamadas automáticas con un mensaje informativo pregrabado y opción DTMF ("Presione 1") para transferir en caliente a la cola de agentes de Telat.
  - **Objetivo Operativo:** Filtrar la base para evitar que los agentes en piso desgasten su jornada en llamadas infructuosas (buzones, tonos ocupados o números no contestados).
- [ ] **Requerimiento 2: Exploración de Monitoreo en Vivo de Llamadas:**
  - **Objetivo:** Consultar la factibilidad técnica y operativa para habilitar monitoreo en tiempo real sobre conmutador cloud (escucha silenciosa / *silent monitoring*, susurro / *whisper* para coaching en vivo, o intervención / *barge-in* para supervisores y calidad).
- [x] **Requerimiento 3: Habilitación y Reporte CDR de Marcación Saliente Manual a 10 Dígitos (Outbound):**
  - **Ticket Oficial en Soporte:** **`#225590`** (`[TIP México] Registro y reporte CDR de llamadas salientes manuales (Outbound)`), creado el 22-Oct-2026, 4:46 p. m.
  - **Estado:** Completado y validado en producción.
  - **Alcance formalizado:** Marcación manual directa a 10 dígitos desde softphone/panel exclusiva para seguimiento de tickets y siniestros por los agentes de piso. En Semana 2 se validaron 88 llamadas manuales salientes con reporte diario entregado.
- [x] **Requerimiento 4: Transferencia Crítica de Llamadas a Cabina de Siniestros (Marcación Rápida `237` Validada):**
  - **Solicitante Cliente:** Alejandrina Sánchez (`alejandrina.sanchez@tipmexico.com`, Analista de Experiencia del Cliente) con copia a Laura Mercado.
  - **Destino Crítico:** Cabina de Siniestros de TIP México: **`55 4195 6614`**.
  - **Resolución y Pruebas (28-Oct-2026):** En coordinación entre telecomunicaciones y Ricardo Morales (TI Telat), se configuró y validó la marcación rápida con el código **`237`** en softphone Bria, confirmando que las llamadas se enlazan correctamente hacia el número `55 4195 6614`.
- [x] **Requerimiento 5: RONA y Auto-pausa por Llamada no Contestada (Liberado y Validado en Producción, 29-Oct-2026):**
  - **Origen:** Gestión telefónica directa de Ricardo García con soporte del conmutador (Javier Jaime / Rosario Sacramento).
  - **Entrega en Producción:** Javier Jaime confirmó liberación el jueves 29-Oct-2026 (1:41 a.m.).
  - **Reglas Validadas en Operación:**
    1. *Auto-pausa:* Si al agente le suena una llamada y no contesta, el conmutador lo pausa al momento en todas sus colas para que la llamada brinque de inmediato a otro agente y el cliente no quede atrapado. En pantalla visualiza «Auto-pausa · No contestó».
    2. *Despausa:* El agente presiona «Estoy disponible» o el supervisor presiona «Liberar» en el tablero (con alerta en tiempo real).
    3. *Módulo de Supervisión:* Pestaña «No contestó» en supervisión activa, generando los reportes `no-contesto-llamadas.csv` y `no-contesto-agentes.csv`.
  - **Validación Operativa:** Rosario Sacramento y Ricardo García confirmaron la visibilidad completa del panel y su funcionamiento en producción.
- [ ] **Requerimiento 6: Campos adicionales en CDR para homologación de layout (En Standby):**
  - **Contexto:** Campos necesarios para alimentar automáticamente las columnas del layout de Laura Mercado (Timestamp de entrada real `Fecha_Inicio`, estatus `Fuera de Horario` en troncal, etiquetado de abandono corto `< 5s`, y volumen de entrada en menú IVR).
  - **Directriz de Operaciones:** **En espera (Standby).** No se solicitará nada a soporte hasta que Laura Mercado valide formalmente el archivo consolidado del 19 al 23 de octubre (`layout_data_repli_19_al_23_oct_2026.xlsx`) y exprese si requiere columnas adicionales.
- [x] **Requerimiento 7: Corrección de inicio anticipado de break durante timbrado/llamada (Ticket Oficial #225674 Resuelto y Cerrado, 04-Nov-2026):**
  - **Plataforma afectada:** Consola web de agentes (`contact.n2a.mx/agente`) y módulo de supervisión (`contact.n2a.mx/supervisor`).
  - **Falla detectada (03-Nov-2026):** Al dar clic en Comida/Break durante el ring o llamada activa, el contador arrancaba de inmediato desde el clic sin esperar al colgado (`CALL_END`).
  - **Causa Raíz Diagnosticada por N2A:** Durante el ring, el sistema interpretaba que la llamada aún no iniciaba; por ello, el break arrancaba desde la solicitud aunque la agente contestara después.
  - **Solución Implementada en Producción (04-Nov-2026, 01:31 hrs por Javier Jaime):**
    1. *Break solicitado durante ring y llamada contestada:* El break queda en espera («Break pendiente: Comida») y comienza a correr en ceros al colgar.
    2. *Break solicitado durante ring y llamada no contestada:* El break inicia en ese instante y la llamada salta al siguiente agente por RONA.
  - **Ajuste Retroactivo en Base de Datos e Historial:**
    - N2A auditó 204 breaks contra 366 llamadas (22-Oct al 03-Nov-2026), detectando solo los 2 casos reportados por Telat y corrigiendo los reportes oficiales:
      * *Paola Morales (Ext. 2003):* Comida solicitada 11:01:47, contestó 11:01:57, colgó 11:15:29. Duración ajustada de 32:02 a 18:20 (inicio real 11:15:29, fin 11:33:49).
      * *Paula González (Ext. 2002):* Comida solicitada 11:25:48, contestó 11:25:57, colgó 11:36:48. Duración ajustada de 20:15 a 09:15 (inicio real 11:36:48, fin 11:46:03).
    - El tiempo en llamada ya no se computa como comida y los totales diarios de break del 03-Nov quedaron saneados en pantalla de agente y reportes de supervisión.
  - **Ticket Oficial en Soporte:** **`#225674`** (`https://net2alliance.freshdesk.com/helpdesk/tickets/225674`) — **Cerrado formalmente el 04-Nov-2026 a la 01:56 hrs** con confirmación de Ricardo García y Javier Jaime.
- [ ] **Requerimiento 8: Integración de Webhooks en tiempo real de llamadas y agentes (Requerimiento de Arquitectura N2A):**
  - **Objetivo:** Recibir pings HTTP automáticos de eventos de llamada (entradas, fin, abandonos, timeouts) y estados de agente en `tip-state-controller`.
  - **Aplicación operativa:** Habilitar el semáforo de *Callback Tracker* (cero llamadas perdidas sin devolución) y automatizar reportes diarios/semanales sin descargas manuales de CSV.
  - **Canal de gestión:** Solicitud formal de requerimiento ante Rosario Sacramento (TAM) y Efrén Torres (Ejecutivo de Cuenta).
- [ ] **Requerimiento 9: Protocolo de los 3 Entregables Diarios Solicitados por TIP:**
  1. *Capturas de Agentes Disponibles:* 08:30 am, 10:00 am y 11:00 am (vía WhatsApp).
  2. *Capturas de Reporte de Tráfico:* 12:00 pm, 15:00 pm y 18:00 pm (vía WhatsApp).
  3. *Verificación Matutina de 9 Líneas a 10 Dígitos:* Script `tip-direccion/scripts/Verificar-Lineas-TIP.bat` con protocolo `sip:` creado para Miriam en Bria (Ext. 2001, cuenta `b245@n2a.com.mx`), pendiente de validación en su máquina.
- [x] **Directorio y Gobernanza de Canales Oficiales, TI & TIP México:**
  - **Gerente de TI, Enlace y Comunicaciones Telat:** Ricardo Morales (`rmorales@telat-group.com`).
  - **Subdirector de Operaciones Telat:** Ricardo García (`rgarcia@telat-group.com`).
  - **Director de Operaciones Telat:** Mauricio Cruz (`mcruz@telat-group.com`).
  - **Contrapartes Operativas TIP México:** Laura Mercado (`laura.mercado@tipmexico.com`) y Alejandrina Sánchez (`alejandrina.sanchez@tipmexico.com`, T: 55 5093 7200 ext. 7649, C: 55 2764 6811).
  - **Línea Directa Cabina de Siniestros TIP:** `55 4195 6614` (Marcación rápida Bria: `237`).

---

## 🔴 5. Deuda Técnica & Backlog
- [ ] **Simulador de Tráfico en Tiempo Real:** Interconectar el dashboard ejecutivo (`index.html`) con APIs de conmutador una vez formalizado el contrato.
- [ ] **Sincronización con Repositorio de Presentaciones:** Homologar documentación en repositorios centralizados de presentaciones si Dirección General requiere acceso.

---

## 🔗 6. Enlaces de Referencia Documental (RFQs Oficiales TIP)
> *Nota: Enlaces guardados exclusivamente para consulta y referencia futura. El contexto operativo vigente se rige por los acuerdos de Fase 1 en la Sección 0.*
- 📄 **RFQ Inicial (Sin IA, Atención Tradicional Humana):** [Google Drive, Archivo Original](https://drive.google.com/file/d/1cksp1mvkVlPeUK5Sw5rgm-FMFvlSx9ZJ/view?usp=drive_link)
- 🤖 **RFQ Secundario (Con IA & Herramientas Operativas):** [Google Docs, Documento con IA y Ecosistema](https://docs.google.com/document/d/12GegljllArpjdFR3eRtZrH7RVJDmL1eFrONFKLCQHvY/edit?usp=drive_link)
