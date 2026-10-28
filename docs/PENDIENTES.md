# 📌 PENDIENTES & HOJA DE RUTA, TIP DIRECCIÓN & ALIANZA N2A

Este documento mantiene el estado de verificación, roadmap y deuda técnica para la cuenta de **TIP México** y la infraestructura con **Net2Alliance (N2A)**.

---

## 🏛️ 0. Arquitectura Canónica & Directrices de Fase 1 (Septiembre 2026)

* **Fase 1 Estricta, Cero Inteligencia Artificial & Plantilla Ajustada (6 FTEs):** La operación inicial para TIP México se basa **exclusivamente en agentes humanos dedicados en piso (6 FTEs)** (5 agentes de piso + 1 supervisor/híbrido) atendiendo 2 canales: Voz (2,800 llamadas/mes) y Correo (500 tickets/mes). Queda estrictamente excluida cualquier automatización con IA en esta primera fase.
* **Exclusión de Canal WhatsApp (Acuerdo Comercial, Óscar Gómez / TIP):** El cliente TIP México determinó retener la atención del canal WhatsApp directamente en su plataforma Zenvia; **Telat NO operará WhatsApp**, concentrando el 100% de la plantilla de 6 FTEs en Voz y Correo/Salesforce.
* **Gobernanza White-Label Absoluta:** De cara a TIP México, **Telat Group es el proveedor único e integral** tanto del talento BPO como de la plataforma tecnológica y de telecomunicaciones. TIP México **NO debe tener conocimiento de la existencia de Net2Alliance (N2A)**. N2A actúa exclusivamente como carrier y partner tecnológico en back-to-back con Telat.
* **Infraestructura Requerida N2A (Voz & Telecom):** Net2Alliance provee la suite unificada en **Cloud CommServer** que abarca:
  1. Troncales SIP y softphones para telefonía de voz (2,800 llamadas/mes, 6 agentes concurrentes).
  2. Mapeo y preservación de cabeceras DNIS para las 9 líneas telefónicas (8 líneas 800 y 1 local CDMX).
  3. Call Intelligence & Analytics para grabación y auditoría de voz al 100%.
  4. *(Nota: Queda cancelado el requerimiento de broker/conector de WhatsApp Business API con N2A)*.

---

## 🔴 1. VERIFICACIONES PENDIENTES EN CALIENTE (seguras, no urgentes)

> 💡 **Validación Rápida con 1 Clic en Obsidian:** Haz clic directamente sobre la casilla `[ ]` para marcarla como `[x]` una vez probada en producción.

- [x] **P-01: Generación de Pliego Técnico para N2A (v1.3):** Actualización de `brief-tecnico-n2a.html` calibrado en 2 páginas Carta para PDF con 6 FTEs y exclusión de WhatsApp. *(✅ Validado)*
- [x] **P-02: Alineación de Alianza Estratégica:** Definición de roles (Telat BPO = 6 agentes en piso; N2A = DIDs, Cloud CommServer, Cloud IntelliNet, Call Intelligence). *(✅ Validado)*
- [x] **P-03: Gobierno de Memoria:** Registro permanente de **Óscar Gómez** (Director Comercial Telat), **Efrén Torres** (Ejecutivo de Cuenta N2A) y **Javier Jaime** (Director General N2A) en `.agents/AGENTS.md`. *(✅ Validado)*
- [x] **P-04: Pruebas de Telefonía Exitosas con TIP:** Validación de viabilidad de desvío (*call forwarding*) a través de troncales SIP hacia cabeceras de conmutador cloud. *(✅ Validado)*
- [x] **P-05: Definición de Requerimientos Técnicos para TIP México (Sept 2026):** Formulación de solicitud técnica precisa (inventario de 800 y DNIS en SIP Header). *(✅ Validado)*


---

## 🟡 2. Respuestas Oficiales del Cliente (TIP México, Sept/2026)
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
  - **Alcance Operativo TELAT:** TELAT atiende exclusivamente **Opción 1** (Siniestros queda fuera del alcance y lo atiende TIP).
  - **TELAT NO tiene que replicar ni administrar el IVR de bienvenida.** TIP coordinará el desvío directo hacia la troncal de TELAT preservando el identificador.
- [x] **Confirmación de Mapeo de 9 Líneas 800 & Locales:** Inventario de las 9 líneas canónicas totalmente confirmado y acordado para aprovisionamiento.
- [x] **Exclusión de WhatsApp Acordada con TIP (Óscar Gómez / TIP):** TIP retiene el canal WhatsApp en su plataforma Zenvia; Telat no lo operará ni aprovisionará licencias.
- [x] **Gestión de Correo Electrónico (Salesforce Service Cloud):**
  - La atención de `contactcenter@tipmexico.com` NO se gestiona en bandeja de correo tradicional, sino mediante tickets en **Salesforce Service Cloud** provisto por TIP con accesos y plantillas tras capacitación.
- [ ] **Firma y Formalización de Contrato por TIP:** En espera de la entrega y firma del contrato formal por parte de la Dirección de TIP México ajustado a **6 FTEs**.
- [x] **Dimensionamiento Económico Consolidado (6 FTEs):** Ajuste de estructura comercial a 6 posiciones humanas en vivo acordado con Dirección Comercial.
- [x] **Arranque Oficial de Capacitación Presencial (Lunes 5 de Octubre, 10:00 a.m.):**
  - **Instructora:** Laura Mercado (`laura.mercado@...`) de TIP México impartirá el curso presencial en instalaciones de TELAT.
  - **Horario Oficial:** Lunes a Viernes de 10:00 a.m. a 5:00 p.m.
  - **Gobernanza Operativa:** Alineación directa liderada por **Mauricio Cruz** (Operations Director) en coordinación con Ricardo García (Subdirector de Operaciones), Ricardo Morales (TI) y Lic. Julio Torres (Legal).
- [x] **Estrategia y Contingencia de Talento: Arranque con 7 Candidatos TELAT:**
  - Capacitación arrancó con 7 candidatos nuevos contratados directamente por TELAT bajo acuerdo de Mauricio Cruz y Laura Mercado.

---

## 📞 3. Implementación PBX, Telecomunicaciones & Ventana de Corte (Octubre 2026)
- [x] **Interconexión PBX y Troncal a Servidor Propio (14-Oct-2026):** Ricardo Morales confirmó la migración exitosa de la troncal SIP a servidor propio con IP definitiva (mismas credenciales). Cero pendientes de interconexión física/red.
- [x] **Aprovisionamiento y Prueba de 9 Extensiones (9001 a 9009):** Extensiones operativas y probadas en ambos sentidos: saliente Telat ➔ TIP y entrante TIP ➔ Telat recibida exitosamente en extensión 9005.
- [x] **Calendario de Corte y Redirección de 8 IVR (Viernes 18:00 h):** Se acordó migrar este viernes al cierre de turno las 8 líneas secundarias (Bitcar, OFS, CARNOT, CHIREY, JAC, MG, KIA, GCO) a la troncal Telat. El conmutador general de TIP México (800 908 6700) se migrará en fecha posterior definida por Laura Mercado. Regla de fuera de horario activa hasta el lunes por la mañana.
- [ ] **Resolución Urgente de Caller ID / DNIS (Llamadas como "Desconocido"):** Sesión técnica urgente solicitada con Iván Ramírez y Rafael Quintero (TIP) para inyectar cabecera DNIS / Caller ID en pantalla del agente antes del viernes, asegurando que el agente reconozca la marca y el speech adecuado.
- [x] **Horario de Operación Oficial (Lunes a Viernes / Sábados Descartados):** Laura Mercado y la dirección de Operaciones confirmaron que el servicio opera exclusivamente de Lunes a Viernes en sus horarios establecidos. Los sábados quedan formalmente descartados (tráfico residual de ~10 llamadas y áreas resolutivas de TIP cerradas; carece de lógica operativa). WFM y todas las áreas internas de Telat ya fueron debidamente actualizadas.
- [ ] **Selección de Audio y Música Institucional en Espera:** En espera de la definición final por parte de Laura Mercado para la música/audio de espera.
- [ ] **Activación de Cuentas de Plataforma y Protocolo 2FA:** Envío de cuentas de agentes a Laura Mercado para plataformas TIP (Salesforce); acordar esquema de contraseñas y doble factor de autenticación que evite celulares personales en piso.
- [ ] **Solicitud de Dispositivo Físico 2FA a Ricardo Morales (Fecha límite 26-Oct-2026):** Jatzyri Yepez (Gerente de Capacitación) notificó la necesidad de una tablet o smartphone corporativo para la autenticación 2FA de los agentes en TIP. Durante las semanas del 12 y 19 de octubre se operará en préstamo con la tablet asignada a Carvana. Se debe solicitar a Ricardo Morales (TI/Enlaces) un dispositivo dedicado disponible a partir del lunes 26 de octubre.
- [ ] **Homologación de Marcación Interna (Serie 7100+):** Confirmar regla general de extensiones de cuatro dígitos que inicien con 7 propuesta por Telat.

---

## 🔵 4. Siguientes Pasos con Net2Alliance (N2A) & Telecomunicaciones
- [x] **Mapeo de 9 Líneas Integrado:** Cabeceras y DIDs listos para aprovisionamiento de troncal SIP con preservación de DNIS.
- [ ] **Aprovisionamiento Final de Troncal y DIDs N2A:** Ejecutar la configuración de Cloud CommServer (6 softphones) una vez formalizada la firma del contrato con TIP.
- [ ] **Requerimiento 1: Blaster Interactivo de Llamadas Salientes (Voice Broadcasting con Transferencia):**
  - **Origen:** Laura Mercado (TIP Corporativo) proporcionará la base de datos de clientes que ningún humano ha contactado.
  - **Mecanismo:** El blaster ejecuta las llamadas automáticas con un mensaje informativo pregrabado (ej. inicio de temporada de trámites de tenencias).
  - **Opciones de Menú (DTMF):** Configurar "Presione 1 para ser transferido con un asesor" (transfiere la llamada en caliente a la cola de agentes de Telat) o mensaje de cierre indicando números y correo oficial para seguimiento.
  - **Objetivo Operativo:** Filtrar la base para evitar que los agentes en piso desgasten su jornada en llamadas infructuosas (buzones, tonos ocupados o números no contestados).
- [ ] **Requerimiento 2: Exploración de Monitoreo en Vivo de Llamadas con N2A:**
  - **Objetivo:** Consultar con Efrén Torres / N2A la factibilidad técnica y operativa para habilitar monitoreo en tiempo real sobre Cloud CommServer (escucha silenciosa / *silent monitoring*, susurro / *whisper* para coaching en vivo, o intervención / *barge-in* para supervisores y calidad).
- [x] **Requerimiento 3: Habilitación y Reporte CDR de Marcación Saliente Manual a 10 Dígitos (Outbound):**
  - **Ticket Oficial en Freshdesk:** **`#225590`** (`[TIP México] Registro y reporte CDR de llamadas salientes manuales (Outbound)`), creado el 22-Oct-2026, 4:46 p. m.
  - **Estado:** En proceso en N2A.
  - **Alcance formalizado:** Marcación manual directa a 10 dígitos desde softphone/panel exclusiva para seguimiento de tickets y siniestros por los agentes de piso. Se exigió la entrega diaria del reporte con marcas de tiempo con segundos, duración de timbrado, duración de conversación y clasificación (`CONTESTADA`, `NO_CONTESTA`, `OCUPADO`, `FALLIDA`).
- [ ] **Requerimiento 4: Transferencia Crítica de Llamadas a Cabina de Siniestros:**
  - **Solicitante Cliente:** Alejandrina Sánchez (`alejandrina.sanchez@tipmexico.com`, Analista de Experiencia del Cliente) con copia a Laura Mercado.
  - **Destino Crítico:** Cabina de Siniestros de TIP México: **`55 4195 6614`**.
  - **Objetivo:** Cuando un usuario llame por contingencia o siniestro vehicular a los números atendidos por Telat, el agente debe poder transferir la llamada de forma inmediata, limpia y rápida hacia la cabina externa (55 4195 6614) desde Bria o Cloud CommServer.
- [ ] **Requerimiento 5: Calibración de Hunting en Colas y Salvaguarda contra Bucles RONA (Auto-pausa):**
  - **Fecha de reporte verbal:** 26-Oct-2026 (Ricardo García gestionó directamente por teléfono con soporte N2A).
  - **Problema detectado en piso:** El balanceo de colas por menor carga (`fewestcalls`) cayó en un bucle ciego (*black hole*) enviando llamadas repetidamente a un mismo agente rezagado que no descolgaba (41 timbrados RONA a Jorge Michel Cano), reteniendo a clientes en espera más de 300 segundos y provocando abandonos.
  - **Solución solicitada a N2A:** Mantener el principio de hunting para evitar trampas y evasión de llamadas en piso (*round-robin evasion*), pero implementar la salvaguarda de descarte inmediato ante el 1er RONA (activar parámetro de cola `autopause = yes` o salto forzado al siguiente asesor disponible) para que el conmutador no secuestre la llamada del cliente y ponga en auto-pausa al asesor omiso.
  - **Estatus:** En revisión técnica por parte de N2A tras llamada telefónica.
- [ ] **Requerimiento 6: Campos adicionales en CDR para homologación inConcert (En Standby):**
  - **Contexto:** Campos necesarios para alimentar automáticamente las 20 columnas del layout de Laura Mercado (Timestamp de entrada real `Fecha_Inicio`, estatus `Fuera de Horario` en troncal, etiquetado de abandono corto `< 5s`, y volumen de entrada en menú IVR).
  - **Directriz de Operaciones:** **En espera (Standby).** No se solicitará nada a N2A hasta que Laura Mercado valide formalmente el archivo consolidado del 19 al 23 de octubre (`layout_data_repli_19_al_23_oct_2026.xlsx`) y exprese si requiere columnas adicionales.
- [x] **Directorio y Gobernanza de Canales Oficiales N2A, TI & TIP México:**
  - **Mesa de Ayuda & Tickets N2A:** `support@net2alliance.freshdesk.com` (asunto con prefijo `[TIP México]`).
  - **Tickets Oficiales en Freshdesk (Net2Alliance):**
    * **`#225549`** (19-Oct, 4:42 P. M.): *Campaña de avisos automáticos salientes (Blaster con transferencia)* | Estatus: Esperando respuesta N2A.
    * **`#225563`** (20-Oct, 6:41 P. M.): *Ajuste de parámetros en colas CommServer y reporte completo CDR* | Estatus: En proceso (canalizado a Desarrollo).
    * **`#225578`** (21-Oct, 5:56 P. M.): *Mapeo de nombres y alias de colas (Skills) en Cloud CommServer* | Estatus: Esperando respuesta N2A.
    * **`#225590`** (22-Oct, 4:46 P. M.): *Registro y reporte CDR de llamadas salientes manuales (Outbound)* | Estatus: En proceso.
  - **Ejecutivo de Cuenta N2A:** Efrén Torres (`efren.torres@net2alliance.com`).
  - **Gerente de TI, Enlace y Comunicaciones Telat:** Ricardo Morales (`rmorales@telat-group.com`).
  - **Contrapartes Operativas TIP México:** Laura Mercado (`laura.mercado@tipmexico.com`) y Alejandrina Sánchez (`alejandrina.sanchez@tipmexico.com`, T: 55 5093 7200 ext. 7649, C: 55 2764 6811).
  - **Línea de Emergencia Cabina de Siniestros TIP:** `55 4195 6614`.

---

## 🔴 5. Deuda Técnica & Backlog
- [ ] **Simulador de Tráfico en Tiempo Real:** Interconectar el dashboard ejecutivo (`index.html` / `dashboard.html`) con APIs de prueba de N2A una vez formalizado el contrato.
- [ ] **Sincronización con Repositorio de Presentaciones:** Homologar `brief-tecnico-n2a.html` dentro de `presentaciones-ejecutivas/Direccion-General/TIP/` si Dirección General requiere acceso centralizado.

---

## 🔗 6. Enlaces de Referencia Documental (RFQs Oficiales TIP)
> *Nota: Enlaces guardados exclusivamente para consulta y referencia futura. El contexto operativo vigente se rige por los acuerdos de Fase 1 en la Sección 0.*
- 📄 **RFQ Inicial (Sin IA, Atención Tradicional Humana):** [Google Drive, Archivo Original](https://drive.google.com/file/d/1cksp1mvkVlPeUK5Sw5rgm-FMFvlSx9ZJ/view?usp=drive_link)
- 🤖 **RFQ Secundario (Con IA & Herramientas Operativas):** [Google Docs, Documento con IA y Ecosistema](https://docs.google.com/document/d/12GegljllArpjdFR3eRtZrH7RVJDmL1eFrONFKLCQHvY/edit?usp=drive_link)

