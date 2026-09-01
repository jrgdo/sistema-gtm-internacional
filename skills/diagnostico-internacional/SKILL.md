---
name: diagnostico-internacional
description: Evalúa si una empresa está suficientemente preparada para iniciar, ampliar o profesionalizar su expansión internacional y qué capacidades, decisiones o gaps deben resolverse antes de invertir más recursos. Úsala cuando la dirección necesite saber si está preparada para exportar, entrar en nuevos mercados o escalar una actividad internacional existente.
---

# Diagnóstico internacional

## 1. Propósito

Evaluar la preparación real de una empresa para una decisión de expansión internacional concreta y transformar un objetivo amplio como “queremos exportar más” en una lectura accionable de fortalezas, gaps, dependencias y siguientes validaciones.

La skill no decide automáticamente qué país elegir ni crea una estrategia internacional completa.

## 2. Pregunta de decisión

> ¿Qué tan preparada está la empresa para ejecutar el objetivo internacional definido, qué podría bloquearlo y qué debe resolverse primero?

## 3. Cuándo usarla

- primera expansión internacional;
- exportación reactiva que se quiere profesionalizar;
- apertura de nuevos países o regiones;
- lanzamiento internacional de una nueva línea o aplicación;
- dudas sobre capacidad interna para sostener crecimiento exterior;
- revisión previa a dedicar presupuesto relevante a market entry.

## 4. Cuándo no usarla

No usar para:

- seleccionar directamente entre países;
- estimar demanda de un mercado concreto;
- buscar distribuidores;
- investigar cuentas;
- diseñar contratos, fiscalidad o compliance regulatorio específico.

## 5. Inputs requeridos

Usar `contracts/entrada-componente.yaml`.

Como mínimo, cuando sean materiales para el objetivo:

- oferta prioritaria;
- aplicaciones principales;
- ICP/clientes actuales o candidatos;
- mercados actuales;
- objetivo internacional;
- modelo comercial/canales;
- restricciones relevantes;
- capacidad interna conocida.

Si faltan inputs críticos, devolver `REQUIERE_INPUT` o enrutar a `onboarding-empresa`.

## 6. Método

### Paso 1 — Precisar objetivo y horizonte

Distinguir entre:

- primera exportación;
- crecimiento en mercados existentes;
- selección de nuevos mercados;
- expansión de canal;
- nueva aplicación/producto;
- profesionalización operativa.

### Paso 2 — Evaluar readiness por dimensiones

Evaluar únicamente las dimensiones relevantes:

1. **Claridad de oferta y aplicación** — qué se vende, para qué aplicación y con qué límites.
2. **Cliente objetivo** — quién compra, quién influye y qué señales de fit existen.
3. **Evidencia comercial** — referencias, ventas, pilotos, casos o señales reales.
4. **Capacidad comercial internacional** — personas, idiomas, disciplina comercial y ownership.
5. **Modelo de canal** — directo, distribuidor, agente, integrador, OEM u otro.
6. **Capacidad técnica y de soporte** — preventa, instalación, formación, posventa y troubleshooting cuando aplique.
7. **Capacidad operativa** — producción, lead times, logística, documentación y servicio.
8. **Preparación regulatoria/técnica** — certificaciones, homologaciones o requisitos conocidos, sin asumir cumplimiento.
9. **Economía y recursos** — capacidad para financiar ciclos largos, viajes, muestras, ferias, canal o adaptación.
10. **Governance y aprendizaje** — responsables, aprobaciones, KPIs y revisión de decisiones.

### Paso 3 — Distinguir capacidad de oportunidad

No confundir:

- “el mercado parece atractivo” con “la empresa está preparada para capturarlo”;
- “tenemos interés de distribuidores” con “tenemos un canal gestionable”;
- “el producto funciona en España” con “está validado para la aplicación y condiciones de otro mercado”.

### Paso 4 — Clasificar gaps

Para cada gap material indicar:

- impacto sobre el objetivo;
- evidencia disponible;
- si bloquea o solo reduce confianza;
- responsable recomendado;
- validación o acción mínima necesaria.

### Paso 5 — Priorizar por secuencia

No generar una lista larga de mejoras. Priorizar:

1. bloqueos críticos;
2. gaps que invalidarían análisis downstream;
3. mejoras con impacto alto y esfuerzo razonable;
4. cuestiones que pueden aprenderse mediante experimentos de mercado.

### Paso 6 — Determinar estado

Estados recomendados:

- `PREPARADO_PARA_AVANZAR`
- `PREPARADO_CON_CONDICIONES`
- `REQUIERE_PREPARACION`
- `NO_EVALUABLE`

Estos son resultados de la skill, no estados globales del agente.

## 7. Reglas de decisión

No declarar `PREPARADO_PARA_AVANZAR` si existe un bloqueo material no resuelto en oferta/aplicación, capacidad de entrega, aprobación técnica/regulatoria necesaria o ownership comercial.

No exigir perfección. En market entry es válido avanzar con incertidumbre si ésta puede convertirse en un experimento controlado y el riesgo es aceptable.

## 8. Evidencia

Aplicar `contracts/evidencia.yaml` y `docs/modelo-de-evidencia.md`.

Distinguir evidencia interna de capacidad de evidencia externa de oportunidad.

## 9. Contrato de salida

Usar `contracts/salida-componente.yaml` y, cuando aplique, `contracts/decision.yaml`.

El resultado debe incluir:

- objetivo evaluado;
- dimensiones relevantes;
- fortalezas comprobadas;
- gaps materiales;
- bloqueos;
- supuestos;
- nivel de confianza;
- readiness resultante;
- condiciones para avanzar;
- siguientes 1–3 acciones.

## 10. Handoffs

- contexto insuficiente → `onboarding-empresa`;
- readiness suficiente + ICP débil → `definicion-icp`;
- readiness suficiente + decisión entre mercados → `priorizacion-de-mercados`;
- cuestión legal/técnica/regulatoria crítica → especialista humano adecuado.

Usar `contracts/handoff.yaml`.

## 11. Failure modes

- empresa confunde exportación oportunista con estrategia → explicitar diferencia;
- solo existe opinión de dirección → baja confianza y validar con evidencia;
- no hay ventas internacionales → no asumir falta de readiness; evaluar fundamentos;
- hay ventas internacionales pero dependencia total de una persona → señalar riesgo operativo;
- certificación o suitability incierta → no inferir; escalar;
- objetivo demasiado amplio → devolver `REQUIERE_CLARIFICACION`.

## 12. Anti-patrones

- checklist universal con puntuación arbitraria;
- declarar “export ready” por tener web en inglés;
- equiparar facturación actual con capacidad internacional;
- asumir que más países = más crecimiento;
- recomendar contratar equipo sin demostrar el cuello de botella;
- generar plan de 50 acciones sin priorización.

## 13. Referencias

Consultar:

- `references/dimensiones-readiness.md`
- `references/madurez-exportadora.md`

## 14. Evaluación

Debe superar:

- `tests/escenarios.md`
- `tests/criterios-de-evaluacion.md`
