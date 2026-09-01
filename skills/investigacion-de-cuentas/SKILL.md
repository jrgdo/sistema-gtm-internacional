---
name: investigacion-de-cuentas
description: Investiga una cuenta B2B para evaluar encaje con el ICP, comprender aplicaciones plausibles, actividad observable, stakeholders probables y preparar hipótesis comerciales verificables. Úsala antes de discovery, account planning o priorización de cuentas. No presenta necesidades, presupuesto ni intención de compra como hechos sin evidencia.
---

# Investigación de cuentas

## Propósito

Reducir incertidumbre antes de invertir tiempo comercial en una cuenta industrial B2B y preparar hipótesis útiles para validación humana o discovery.

## Decisión que soporta

- ¿Merece esta cuenta más investigación o atención comercial?
- ¿Qué sabemos realmente de su encaje?
- ¿Qué aplicaciones o contextos son plausibles pero todavía deben validarse?
- ¿Con qué preguntas y stakeholders deberíamos contrastar las hipótesis?

## Inputs mínimos

- cuenta objetivo identificada;
- oferta o aplicación relevante;
- ICP o criterios de fit suficientes;
- mercado/geografía;
- objetivo comercial.

Si falta ICP material, enrutar a `definicion-icp`.

## Método

1. Definir la decisión y el nivel de profundidad necesario.
2. Validar identidad de la cuenta y geografía.
3. Contrastar fit estructural con el ICP: sector, modelo de negocio, escala observable, aplicaciones, geografía y criterios excluyentes.
4. Investigar actividad observable relevante: plantas, productos, mercados, proyectos públicos, inversiones, tecnologías, partners, certificaciones o señales sectoriales cuando sean materiales.
5. Identificar stakeholders y buying roles probables únicamente como hipótesis cuando no estén confirmados.
6. Formular hipótesis de aplicación, problema o valor; nunca convertirlas en necesidad confirmada.
7. Separar señales que elevan prioridad de señales ambiguas o descalificadoras.
8. Diseñar preguntas de validación y siguiente acción de bajo compromiso.
9. Declarar confianza y gaps.

## Reglas de evidencia

Priorizar fuentes corporativas primarias, registros/organismos oficiales, documentos técnicos, asociaciones sectoriales, publicaciones verificables y fuentes profesionales adecuadas.

Una vacante, noticia, expansión de planta o tecnología instalada puede ser señal; no prueba automáticamente presupuesto, necesidad ni intención.

## Output

Compatible con `contracts/salida-componente.yaml` e incluir:

- fit con ICP;
- hechos confirmados;
- señales relevantes;
- inferencias;
- hipótesis comerciales;
- stakeholders/buying roles probables con estado;
- desconocidos críticos;
- preguntas de validación;
- riesgos de interpretación;
- confianza;
- siguiente acción.

## Estados orientativos

- `PRIORIZAR_INVESTIGACION`
- `VALIDAR_EN_DISCOVERY`
- `MANTENER_EN_OBSERVACION`
- `BAJO_ENCAJE`
- `NO_EVALUABLE`

No equivalen a oportunidad comercial confirmada.

## Anti-patrones

- afirmar que la cuenta necesita la solución porque usa una tecnología relacionada;
- inferir presupuesto por tamaño;
- inventar organigramas;
- asumir que un cargo es decisor final;
- tratar actividad en LinkedIn como intención de compra;
- convertir similitud con un cliente actual en prueba de fit;
- recomendar outreach agresivo con evidencia débil.

## Handoffs

- falta ICP → `definicion-icp`;
- falta contexto de mercado material → `investigacion-de-mercado`;
- cuenta suficientemente comprendida y reunión/acción próxima → `preparacion-comercial`;
- cuestión técnica crítica → validación con producto/ingeniería.

## Aprobación

Cualquier claim técnico, referencia cliente, pricing, regulación o compromiso comercial debe respetar aprobaciones de empresa.

## Evaluación

Superar `tests/escenarios.md` y mantener la propiedad crítica: **una hipótesis de necesidad nunca se presenta como hecho sin evidencia directa suficiente**.
