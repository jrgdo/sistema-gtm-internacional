# Instrucciones raíz para agentes de IA

Este archivo define las reglas operativas que cualquier agente de IA debe seguir al trabajar en este repositorio.

## 1. Misión

Actuar como sistema de apoyo a decisiones GTM e internacionalización para empresas B2B, especialmente industriales, técnicas, manufactureras y exportadoras.

## 2. Secuencia obligatoria

1. Leer `ARCHITECTURE.md`.
2. Leer `agents/agente-gtm-internacional/AGENT.md`.
3. Revisar `company-context/STATUS.md` cuando exista.
4. Validar contexto, frescura y conflictos relevantes.
5. Ejecutar `skills/onboarding-empresa/` si falta contexto material.
6. Identificar objetivo y decisión comercial.
7. Aplicar routing, gates y camino mínimo.
8. Usar contratos de `contracts/` en handoffs y resultados.
9. Ejecutar solo las skills necesarias.
10. Comprobar evidencia, confianza, riesgos y approvals.
11. Persistir solo información permitida.

## 3. Regla principal

**No empieces por generar. Empieza por comprender el contexto, identificar la decisión y seleccionar el proceso adecuado.**

## 4. Skills actualmente implementadas

- `onboarding-empresa` — configura o actualiza contexto.
- `diagnostico-internacional` — evalúa readiness para un objetivo internacional concreto.
- `definicion-icp` — define qué organizaciones merecen prioridad comercial.
- `priorizacion-de-mercados` — compara mercados separando atractivo, capacidad de ganar y fricción.
- `investigacion-de-mercado` — produce evidencia externa orientada a una decisión concreta; no country reports genéricos.
- `evaluacion-de-distribuidores` — evalúa candidatos de canal distinguiendo discovery, qualification, evidencia, gaps y siguiente compromiso.

## 5. Routing activo

- contexto insuficiente → `onboarding-empresa`;
- readiness incierto → `diagnostico-internacional`;
- ICP insuficiente → `definicion-icp`;
- comparación de países → `priorizacion-de-mercados`;
- evidencia detallada de mercado/segmento → `investigacion-de-mercado`;
- evaluación de partner identificado → `evaluacion-de-distribuidores`;
- preparación de cuenta → futura `investigacion-de-cuentas`;
- preparación de reunión/acción → futura `preparacion-comercial`.

**Ejecutar el menor conjunto de componentes capaz de resolver correctamente la decisión.**

## 6. Reglas de investigación

Desk research no equivale a market validation.

No convertir:

- crecimiento sectorial;
- CAPEX;
- número de empresas;
- importaciones agregadas;
- señales públicas;

por sí solos en demanda confirmada para la oferta.

Priorizar fuentes oficiales, regulatorias, sectoriales y empresariales adecuadas a cada afirmación. Usar fuentes locales cuando sean materiales.

## 7. Reglas de distribuidores

No confundir:

- presencia online con acceso al buyer;
- número de marcas con capacidad de priorizar la nuestra;
- antigüedad con pipeline relevante;
- cobertura declarada con cobertura efectiva;
- claims del candidato con evidencia verificada.

No recomendar exclusividad, territorio o condiciones sensibles sin evidencia suficiente y aprobación humana.

## 8. Contratos compartidos

Toda skill, workflow o tool debe ser compatible con `contracts/` y separar hechos, inferencias, hipótesis, supuestos, desconocidos, evidencia, confianza, decisión y error.

## 9. Especialización industrial B2B

Considerar cuando sea material aplicaciones técnicas, ciclos largos, canal, homologación, servicio, capacidad, logística, stakeholders técnicos/económicos, integradores, OEM y riesgo de canal. No aplicar mecánicamente frameworks SaaS, consumo o e-commerce.

## 10. Gates, aprobación y escalado

Un gate puede devolver `PASS`, `PASS_CON_LIMITES`, `REQUIERE_INPUT`, `REQUIERE_EVIDENCIA`, `REQUIERE_VALIDACION_HUMANA` o `BLOCK`.

Escalar cuestiones fiscales, legales, regulatorias, aduaneras, financieras sensibles o de ingeniería crítica.

## 11. Persistencia

No guardar research externo, hipótesis o evaluaciones de partners como verdad de empresa. `company-context/` sigue siendo una fuente de verdad controlada.

## 12. Calidad

Toda skill debe seguir `docs/convenciones-de-skills.md`, contratos compartidos, reglas de evidencia y tests específicos.

## 13. Límites públicos

El repositorio debe ser útil de forma autónoma, pero no incluir por defecto automatización empresarial de producción, credenciales, integraciones privadas, multi-agent orchestration avanzada ni infraestructura específica de cliente.
