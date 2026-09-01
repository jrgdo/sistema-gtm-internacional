---
name: priorizacion-de-mercados
description: Compara y prioriza mercados internacionales para una oferta e ICP concretos utilizando criterios explícitos de atractivo, capacidad de ganar, fricción y evidencia. Úsala cuando una empresa necesite decidir dónde investigar, validar o invertir primero entre varios países o segmentos geográficos.
---

# Priorización de mercados

## 1. Propósito

Ayudar a dirección y equipos comerciales a decidir qué mercados merecen atención primero, evitando rankings basados únicamente en tamaño, intuición o datos macro.

La salida es una priorización para decidir dónde profundizar o validar, no una garantía de market entry.

## 2. Pregunta de decisión

> Entre los mercados considerados, ¿cuáles merecen prioridad para esta oferta, ICP y objetivo, y qué evidencia falta antes de comprometer más recursos?

## 3. Inputs requeridos

- oferta/aplicación prioritaria;
- ICP suficientemente definido;
- objetivo internacional;
- lista o universo de mercados a comparar;
- restricciones materiales;
- evidencia disponible por mercado.

Usar `contracts/entrada-componente.yaml`.

## 4. Preconditions

No ejecutar con alta confianza si faltan oferta, aplicación o ICP.

Si el readiness de la empresa es materialmente incierto, enrutar primero a `diagnostico-internacional`.

## 5. Método

### Paso 1 — Definir decisión y horizonte

Aclarar si se prioriza para:

- investigación;
- prospección;
- búsqueda de canal;
- inversión comercial;
- feria/evento;
- entrada formal.

### Paso 2 — Definir criterios antes de mirar el ranking

Separar al menos tres bloques:

1. **Atractivo del mercado**
2. **Capacidad de ganar**
3. **Fricción/riesgo de entrada**

Los criterios deben adaptarse al producto y situación.

### Paso 3 — Evaluar atractivo

Puede incluir:

- demanda/importaciones relevantes;
- crecimiento o inversión;
- densidad de ICP/aplicación;
- proyectos/señales sectoriales;
- estructura competitiva;
- potencial económico.

### Paso 4 — Evaluar capacidad de ganar

Puede incluir:

- referencias transferibles;
- acceso a clientes;
- canal existente;
- fit de producto/aplicación;
- capacidad de servicio;
- idioma/conocimiento local;
- proximidad logística;
- diferenciación defendible.

### Paso 5 — Evaluar fricción

Puede incluir:

- regulación/certificación;
- aranceles y barreras;
- logística;
- lead times;
- coste de servicio;
- complejidad de canal;
- riesgo de pago/contratación;
- intensidad competitiva.

### Paso 6 — Documentar evidencia y gaps

No asignar scores sin explicar qué evidencia los sostiene.

Cuando la evidencia sea débil, marcar `NO_EVALUABLE` o reducir confianza.

### Paso 7 — Ponderación

Los pesos deben ser explícitos y sumar 100 cuando se utilice scoring cuantitativo.

No presentar pesos estándar como verdad universal. Registrar por qué se usan.

### Paso 8 — Sensibilidad cualitativa

Comprobar si pequeños cambios razonables en criterios/pesos cambian radicalmente el ranking.

Si lo hacen, declarar ranking inestable y priorizar investigación adicional.

### Paso 9 — Clasificación

Resultado recomendado por mercado:

- `PRIORIZAR`
- `INVESTIGAR`
- `MANTENER_EN_OBSERVACION`
- `POSPONER`
- `NO_GO`
- `NO_EVALUABLE`

### Paso 10 — Definir siguiente validación

Para mercados prioritarios indicar qué hipótesis debe comprobarse antes de aumentar inversión.

## 6. Reglas de decisión

- tamaño de mercado nunca es suficiente por sí solo;
- atractivo alto + capacidad de ganar baja no equivale a prioridad automática;
- un mercado pequeño puede ser prioritario si existe fuerte acceso y fit;
- no penalizar una incógnita como si fuera evidencia negativa: marcarla como gap;
- no convertir un ranking de escritorio en decisión irreversible.

## 7. Evidencia

Aplicar `contracts/evidencia.yaml`.

Preferir fuentes primarias/estadísticas/sectoriales adecuadas al criterio y registrar fecha y alcance cuando sea material.

## 8. Salida

Usar `contracts/salida-componente.yaml` y `contracts/decision.yaml`.

Debe incluir:

- mercados comparados;
- criterios y pesos;
- atractivo;
- capacidad de ganar;
- fricción;
- evidencia;
- gaps;
- clasificación;
- confianza;
- sensibilidad/riesgos;
- recomendación de siguiente validación.

## 9. Handoffs

- contexto insuficiente → onboarding;
- readiness incierto → diagnostico-internacional;
- ICP insuficiente → definicion-icp;
- mercado priorizado → futura investigacion-de-mercado;
- canal como hipótesis clave → futura evaluacion-de-distribuidores.

## 10. Failure modes

- datos incomparables entre países → reducir confianza;
- falta de datos para un mercado → `NO_EVALUABLE`, no cero;
- criterios definidos después de ver resultados → advertir riesgo de cherry-picking;
- ranking dominado por un criterio → mostrar dependencia;
- mercados demasiado heterogéneos → segmentar análisis si procede.

## 11. Anti-patrones

- ranking por PIB/TAM;
- “top 10 countries” genérico;
- score sin fuentes;
- precisión falsa con decimales innecesarios;
- weights ocultos;
- confundir facilidad de exportación con demanda;
- confundir imports con mercado accesible para la empresa.

## 12. Referencias

- `references/marco-de-criterios.md`
- `references/scoring-y-sensibilidad.md`

## 13. Evaluación

- `tests/escenarios.md`
- `tests/criterios-de-evaluacion.md`
