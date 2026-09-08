# 📌 PENDIENTES & HOJA DE RUTA — TIP DIRECCIÓN & ALIANZA N2A

Este documento mantiene el estado de verificación, roadmap y deuda técnica para la cuenta de **TIP México** y la infraestructura con **Net2Alliance (N2A)**.

---

## 🏛️ 0. Arquitectura Canónica & Directrices de Fase 1 (Septiembre 2026)

* **Fase 1 Estricta — Cero Inteligencia Artificial:** La operación inicial para TIP México se basa **exclusivamente en agentes humanos dedicados en piso (8 FTEs)** atendiendo los 3 canales: Voz (2,800 llamadas/mes), WhatsApp (1,000 chats/mes) y Correo (500 tickets/mes). Queda estrictamente excluida cualquier automatización con IA en esta primera fase comercial y operativa, apegándonos a la exigencia del cliente.
* **Gobernanza White-Label Absoluta:** De cara a TIP México, **Telat Group es el proveedor único e integral** tanto del talento BPO como de la plataforma tecnológica y de telecomunicaciones. TIP México **NO debe tener conocimiento de la existencia de Net2Alliance (N2A)**. N2A actúa exclusivamente como carrier y partner tecnológico en back-to-back con Telat.
* **Infraestructura Completa N2A (3 Canales):** Net2Alliance provee la suite unificada en **Cloud CommServer** que abarca:
  1. Troncales SIP y softphones para telefonía de voz (2,800 llamadas/mes, 8 agentes concurrentes).
  2. Broker y conector oficial de WhatsApp Business API (1,000 chats/mes).
  3. Módulo de gestión y enrutamiento de Correo Electrónico (500 tickets/mes).
  4. Call Intelligence & Analytics para grabación y auditoría de voz al 100%.

---

## 🔴 1. VERIFICACIONES PENDIENTES EN CALIENTE (seguras, no urgentes)

> 💡 **Validación Rápida con 1 Clic en Obsidian:** Haz clic directamente sobre la casilla `[ ]` para marcarla como `[x]` una vez probada en producción.

- [x] **P-01: Generación de Pliego Técnico para N2A (v1.2):** Creación de `brief-tecnico-n2a.html` calibrado en exactamente 2 páginas Carta para PDF con branding oficial Telat (*The Voice of Your Company*). *(✅ Validado)*
- [x] **P-02: Alineación de Alianza Estratégica:** Definición de roles (Telat BPO = 8 agentes en piso; N2A = DIDs, Cloud CommServer, Cloud IntelliNet, Call Intelligence). *(✅ Validado)*
- [x] **P-03: Gobierno de Memoria:** Registro permanente de **Efrén Torres** (Ejecutivo de Cuenta N2A) y **Javier Jaime** (Director General N2A) en `.agents/AGENTS.md`. *(✅ Validado)*
- [x] **P-04: Pruebas de Telefonía Exitosas con TIP:** Validación de viabilidad de desvío (*call forwarding*) a través de troncales SIP hacia cabeceras de conmutador cloud. *(✅ Validado)*
- [x] **P-05: Definición de Requerimientos Técnicos para TIP México (Sept 2026):** Formulación de solicitud técnica precisa (inventario de 800, DNIS en SIP Header, y lógica/árbol de WhatsApp actual). *(✅ Validado)*


---

## 🟡 2. En Espera de Respuesta del Cliente (TIP México)
- [ ] **Inventario de Líneas 800:** Recepción del desglose de números 800 y líneas locales de TIP con su tema/departamento asignado (Siniestros, Mantenimiento, Gestorías, Facturación, Conmutador General).
- [ ] **Confirmación de DNIS / SIP Header en Forwarding:** Validación por el equipo de telecomunicaciones de TIP de que las llamadas desviadas transmitirán el identificador original del 800 marcado para auto-enrutamiento en el conmutador.
- [ ] **Lógica & Flujo de WhatsApp de Proveedor Actual:** Recepción del árbol de decisiones, menú de bienvenida y reglas de asignación de su proveedor actual (inConcert) para replicarlo de forma nativa en la infraestructura provista por Telat.

---

## 🔵 3. Siguientes Pasos con Net2Alliance (N2A)
- [ ] **Recepción y Análisis de Cotización N2A:** Comparar la propuesta económica y técnica integral de N2A (Voz + WhatsApp + Correo) contra los SLAs (85% SL, ASA $\le$ 20s, AHT 7:00 min).
- [ ] **Integración de Costo de Telefonía en Oferta Final:** Sumar el costo de DIDs, troncales y módulos N2A a la tarifa de posición de los 8 FTEs para la entrega formal del RFQ a TIP México.
- [ ] **Aprovisionamiento y Réplica de WhatsApp:** Una vez recibida la lógica de TIP, montar el árbol de atención en el broker WABA de N2A.

---

## 🔴 4. Deuda Técnica & Backlog
- [ ] **Simulador de Tráfico en Tiempo Real:** Interconectar el dashboard ejecutivo (`index.html` / `dashboard.html`) con APIs de prueba de N2A una vez formalizado el contrato.
- [ ] **Sincronización con Repositorio de Presentaciones:** Homologar `brief-tecnico-n2a.html` dentro de `presentaciones-ejecutivas/Direccion-General/TIP/` si Dirección General requiere acceso centralizado.

---

## 🔗 5. Enlaces de Referencia Documental (RFQs Oficiales TIP)
> *Nota: Enlaces guardados exclusivamente para consulta y referencia futura. El contexto operativo vigente se rige por los acuerdos de Fase 1 en la Sección 0.*
- 📄 **RFQ Inicial (Sin IA — Atención Tradicional Humana):** [Google Drive — Archivo Original](https://drive.google.com/file/d/1cksp1mvkVlPeUK5Sw5rgm-FMFvlSx9ZJ/view?usp=drive_link)
- 🤖 **RFQ Secundario (Con IA & Herramientas Operativas):** [Google Docs — Documento con IA y Ecosistema](https://docs.google.com/document/d/12GegljllArpjdFR3eRtZrH7RVJDmL1eFrONFKLCQHvY/edit?usp=drive_link)

