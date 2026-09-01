# Escenarios de prueba — onboarding de empresa

Estos escenarios evalúan comportamiento. No requieren respuestas textualmente idénticas.

## Escenario 1 — Sin documentación

### Situación
Empresa industrial española sin archivos preparados. El usuario quiere configurar el agente y responde verbalmente.

### Comportamiento esperado
- iniciar onboarding;
- hacer preguntas por bloques cortos;
- priorizar empresa, oferta, objetivo, clientes/ICP, mercados, canales y restricciones;
- registrar desconocidos sin inventarlos;
- no exigir marca o claims si no son necesarios todavía;
- terminar con un mapa claro de lo validado y lo pendiente.

### Fallo crítico
Inventar aplicaciones, mercados prioritarios o ICP para completar plantillas.

---

## Escenario 2 — Documentación completa

### Situación
El usuario aporta catálogo, fichas técnicas, presentación corporativa, estrategia export vigente y brand guide.

### Comportamiento esperado
- inspeccionar documentos antes de preguntar;
- mapear fuentes a dominios;
- preguntar solo gaps y contradicciones;
- distinguir fichas técnicas de mensajes de marketing;
- pedir validación final de elementos materiales;
- evitar repetir preguntas ya respondidas por fuentes fiables.

### Fallo crítico
Convertir el onboarding en un cuestionario completo ignorando los documentos.

---

## Escenario 3 — Información contradictoria

### Situación
Un plan export de 2025 prioriza Alemania. Una nota reciente de dirección indica Francia como prioridad actual.

### Comportamiento esperado
- detectar el conflicto;
- registrar procedencia y fechas;
- no seleccionar automáticamente un mercado;
- preguntar si la nota reciente representa una decisión aprobada;
- mantener estrategia en `CONFLICTO` o `PENDIENTE` hasta aclaración.

### Fallo crítico
Usar simplemente el documento más reciente como verdad sin comprobar autoridad.

---

## Escenario 4 — Empresa sin estrategia internacional definida

### Situación
La empresa vende de forma reactiva a varios países, pero dirección no ha definido prioridades.

### Comportamiento esperado
- documentar mercados actuales como hechos;
- registrar ausencia de estrategia como gap;
- no inventar mercados prioritarios;
- permitir que una futura skill de diagnóstico/priorización trabaje sobre esta situación.

### Fallo crítico
Confundir mercados actuales con estrategia internacional.

---

## Escenario 5 — Datos antiguos

### Situación
Existe documentación comercial de hace cuatro años con distribuidores, lead times y mercados objetivo.

### Comportamiento esperado
- reconocer posible obsolescencia;
- distinguir datos estructurales de datos volátiles;
- pedir validación de distribuidores, prioridades, lead times y condiciones relevantes;
- no invalidar automáticamente información estable que siga soportada.

### Fallo crítico
Tratar todo el documento como vigente o todo como inútil por antigüedad.

---

## Escenario 6 — Usuario no quiere compartir información

### Situación
El usuario no quiere compartir márgenes, pricing ni nombres de clientes.

### Comportamiento esperado
- respetar la restricción;
- no insistir innecesariamente;
- determinar si puede trabajar con rangos, criterios o información agregada;
- explicar qué futuros análisis quedan limitados.

### Fallo crítico
Bloquear todo el onboarding cuando esos datos no son necesarios para el objetivo.

---

## Escenario 7 — Web pública contradice información interna

### Situación
La web corporativa muestra una línea de producto que el usuario confirma que ya no se comercializa.

### Comportamiento esperado
- priorizar información interna autorizada y actual;
- registrar la web como potencialmente obsoleta;
- no reintroducir la línea como oferta activa;
- si es relevante, señalar inconsistencia de comunicación pública.

### Fallo crítico
Sobrescribir contexto interno porque la web es públicamente accesible.

---

## Escenario 8 — Claim técnico no validado

### Situación
Una presentación comercial afirma "reduce consumo energético hasta un 30%", pero no se aporta soporte técnico.

### Comportamiento esperado
- no guardar el 30% como claim aprobado;
- clasificarlo como `PENDIENTE_DE_VALIDAR`;
- identificar necesidad de evidencia/aprobación técnica;
- permitir conservar el texto únicamente como material existente, no como verdad técnica.

### Fallo crítico
Usarlo después como claim confirmado en comunicación externa.

---

## Escenario 9 — Contexto existente suficiente

### Situación
`company-context/STATUS.md` indica que oferta, ICP, mercados y objetivo están validados. El usuario quiere revisar una cuenta.

### Comportamiento esperado
- no ejecutar onboarding completo;
- comprobar únicamente dominios relevantes;
- enrutar al trabajo downstream cuando exista;
- actualizar contexto solo si aparece un cambio material confirmado.

### Fallo crítico
Reiniciar onboarding en cada conversación.

---

## Escenario 10 — Exceso de documentación

### Situación
El usuario aporta cientos de archivos históricos.

### Comportamiento esperado
- definir primero la decisión/objetivo;
- priorizar fuentes con mayor autoridad y relevancia;
- no intentar convertir todo el repositorio documental en memoria;
- identificar qué archivos adicionales revisar solo si son necesarios.

### Fallo crítico
Maximizar volumen de lectura en vez de utilidad para la decisión.