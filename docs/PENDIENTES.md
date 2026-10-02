# 📌 PENDIENTES & HOJA DE RUTA — TIP DIRECCIÓN & ALIANZA N2A

Este documento mantiene el estado de verificación, roadmap y deuda técnica para la cuenta de **TIP México** y la infraestructura con **Net2Alliance (N2A)**.

---

## 🏛️ 0. Arquitectura Canónica & Directrices de Fase 1 (Septiembre 2026)

* **Fase 1 Estricta — Cero Inteligencia Artificial & Plantilla Ajustada (6 FTEs):** La operación inicial para TIP México se basa **exclusivamente en agentes humanos dedicados en piso (6 FTEs)** (5 agentes de piso + 1 supervisor/híbrido) atendiendo 2 canales: Voz (2,800 llamadas/mes) y Correo (500 tickets/mes). Queda estrictamente excluida cualquier automatización con IA en esta primera fase.
* **Exclusión de Canal WhatsApp (Acuerdo Comercial — Óscar Gómez / TIP):** El cliente TIP México determinó retener la atención del canal WhatsApp directamente en su plataforma Zenvia; **Telat NO operará WhatsApp**, concentrando el 100% de la plantilla de 6 FTEs en Voz y Correo/Salesforce.
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

## 🟡 2. Respuestas Oficiales del Cliente (TIP México — Sept/2026)
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
- [ ] **Preservación de Cabeceras DNIS / SIP en Forwarding (Acuerdo Técnico en Memoria):** Solicitar formalmente al área de Telecomunicaciones de TIP la preservación obligatoria del identificador/cabecera en el desvío hacia TELAT/N2A.
- [x] **Exclusión de WhatsApp Acordada con TIP (Óscar Gómez / TIP):** TIP retiene el canal WhatsApp en su plataforma Zenvia; Telat no lo operará ni aprovisionará licencias.
- [x] **Gestión de Correo Electrónico (Salesforce Service Cloud):**
  - La atención de `contactcenter@tipmexico.com` NO se gestiona en bandeja de correo tradicional, sino mediante tickets en **Salesforce Service Cloud** provisto por TIP con accesos y plantillas tras capacitación.
- [ ] **Firma y Formalización de Contrato por TIP:** En espera de la entrega y firma del contrato formal por parte de la Dirección de TIP México ajustado a **6 FTEs**.
- [x] **Dimensionamiento Económico Consolidado (6 FTEs):** Ajuste de estructura comercial a 6 posiciones humanas en vivo acordado con Dirección Comercial.
- [x] **Arranque Oficial de Capacitación Presencial (Lunes 5 de Octubre, 10:00 a.m.):**
  - **Instructora:** Laura Mercado (`laura.mercado@...`) de TIP México impartirá el curso presencial en instalaciones de TELAT.
  - **Horario Oficial:** Lunes a Viernes de 10:00 a.m. a 5:00 p.m.
  - **Gobernanza Operativa:** Alineación directa liderada por **Mauricio Cruz** (Operations Director) en coordinación con Ricardo García (Subdirector de Operaciones), Ricardo Morales (TI) y Lic. Julio Torres (Legal).
- [x] **Estrategia y Contingencia de Talento — Arranque con 7 Candidatos TELAT:**
  - **Situación Colaboradores Transferidos:** Los ~4 agentes del proveedor anterior que TIP contemplaba transferir no contaban con datos ni expedientes listos para el lunes 5.
  - **Acuerdo Telefónico y Escrito (Mauricio Cruz ➔ Laura Mercado, 02/Oct/2026):** Se arranca la capacitación el lunes 5 a las 10:00 a.m. con **7 candidatos nuevos contratados directamente por TELAT**.
  - **Ventana de Sustitución:** La transferencia del personal de TIP se pospone para revisión en la semana (agendados tentativamente para el miércoles 7 de octubre). Si se integran, se sustituirán durante la semana aquellos candidatos de TELAT con menor desempeño en capacitación.

---

## 🔵 3. Siguientes Pasos con Net2Alliance (N2A)
- [x] **Mapeo de 9 Líneas Integrado:** Cabeceras y DIDs listos para aprovisionamiento de troncal SIP con preservación de DNIS.
- [ ] **Aprovisionamiento Final de Troncal y DIDs N2A:** Ejecutar la configuración de Cloud CommServer (6 softphones) una vez formalizada la firma del contrato con TIP.

---

## 🔴 4. Deuda Técnica & Backlog
- [ ] **Simulador de Tráfico en Tiempo Real:** Interconectar el dashboard ejecutivo (`index.html` / `dashboard.html`) con APIs de prueba de N2A una vez formalizado el contrato.
- [ ] **Sincronización con Repositorio de Presentaciones:** Homologar `brief-tecnico-n2a.html` dentro de `presentaciones-ejecutivas/Direccion-General/TIP/` si Dirección General requiere acceso centralizado.

---

## 🔗 5. Enlaces de Referencia Documental (RFQs Oficiales TIP)
> *Nota: Enlaces guardados exclusivamente para consulta y referencia futura. El contexto operativo vigente se rige por los acuerdos de Fase 1 en la Sección 0.*
- 📄 **RFQ Inicial (Sin IA — Atención Tradicional Humana):** [Google Drive — Archivo Original](https://drive.google.com/file/d/1cksp1mvkVlPeUK5Sw5rgm-FMFvlSx9ZJ/view?usp=drive_link)
- 🤖 **RFQ Secundario (Con IA & Herramientas Operativas):** [Google Docs — Documento con IA y Ecosistema](https://docs.google.com/document/d/12GegljllArpjdFR3eRtZrH7RVJDmL1eFrONFKLCQHvY/edit?usp=drive_link)

