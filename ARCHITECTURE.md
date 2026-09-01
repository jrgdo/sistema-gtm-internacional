# Arquitectura del Sistema GTM Internacional

## 1. Objetivo

Construir un agente de IA personalizable que ayude a empresas B2B, especialmente industriales y técnicas, a estructurar decisiones de internacionalización, entrada en mercados y desarrollo comercial.

El sistema público debe ser útil por sí mismo y riguroso para trabajo real, sin sustituir una implementación empresarial conectada a CRM, ERP, fuentes de datos y automatización avanzada.

## 2. Arquitectura lógica

```text
USUARIO
  ↓
AGENTS.md + CLAUDE.md / CODEX.md
  ↓
COMPANY CONTEXT ENGINE
  ↓
ONBOARDING CUANDO SEA NECESARIO
  ↓
AGENTE GTM INTERNACIONAL
  ↓
CONTRATOS + ROUTING + GATES + HANDOFFS
  ↓
WORKFLOW / SKILL
  ↓
TOOLS DETERMINISTAS CUANDO APLIQUE
  ↓
EVIDENCIA + APROBACIÓN
  ↓
DECISIÓN HUMANA
  ↓
PERSISTENCIA VALIDADA
```

## 3. Capas

### Instrucciones raíz
Definen comportamiento y límites.

### Company Context Engine
Mantiene verdad operativa con estado, procedencia, frescura y conflictos.

### Onboarding
Configura o actualiza contexto para un objetivo concreto.

### Agente GTM Internacional
Coordina objetivo, routing, gates, stops y handoffs.

### Contratos compartidos
`contracts/` define el lenguaje común de entrada, salida, evidencia, decisión, confianza, error, estados y handoffs.

### Skills
Contienen metodología profesional reutilizable.

### Workflows
Compondrán varias capacidades en procesos completos en Fase 7.

### Tools
Ejecutarán cálculos, validaciones y transformaciones deterministas en Fase 8.

## 4. Skills implementadas

### `onboarding-empresa`
Construye contexto validado de empresa.

### `diagnostico-internacional`
Evalúa preparación para ejecutar un objetivo internacional concreto.

Marco clave:

```text
OBJETIVO
↓
OFERTA / APLICACIÓN
↓
CLIENTE
↓
EVIDENCIA
↓
CAPACIDAD COMERCIAL / CANAL / SOPORTE / OPERACIONES
↓
RESTRICCIONES
↓
READINESS + GAPS + CONDICIONES
```

No confunde oportunidad de mercado con capacidad interna.

### `definicion-icp`
Define qué organizaciones merecen prioridad para una oferta/aplicación.

Debe incluir criterios de inclusión, disqualifiers, señales observables y nivel de evidencia.

No confundir ICP con buying roles.

### `priorizacion-de-mercados`
Compara países mediante tres bloques separados:

```text
ATRACTIVO
+
CAPACIDAD DE GANAR
+
FRICCIÓN / RIESGO
```

Los criterios y pesos deben ser explícitos. Unknowns no se convierten automáticamente en scores negativos. El ranking sirve para decidir dónde investigar o validar primero.

## 5. Secuencia estratégica inicial

Cuando la petición requiere toda la cadena y las dependencias lo justifican:

```text
ONBOARDING
  ↓
DIAGNÓSTICO INTERNACIONAL
  ↓
DEFINICIÓN DE ICP
  ↓
PRIORIZACIÓN DE MERCADOS
```

Pero el Agente GTM debe aplicar camino mínimo. No ejecutar toda la cadena cuando una sola skill basta.

## 6. Company Context Engine

Las plantillas públicas viven en `templates/contexto-empresa/`; los datos de una empresa concreta viven localmente en `company-context/`.

`STATUS.md` es el punto de entrada obligatorio.

## 7. Contratos compartidos

Todo componente futuro debe ser compatible con:

- `contracts/entrada-componente.yaml`;
- `contracts/salida-componente.yaml`;
- `contracts/handoff.yaml`;
- `contracts/evidencia.yaml`;
- `contracts/decision.yaml`;
- `contracts/confianza.yaml`;
- `contracts/error-operativo.yaml`;
- `contracts/estados.yaml`;
- `contracts/cierre-ejecucion.yaml`.

Los contratos son semántica interna; no obligan a mostrar YAML al usuario.

## 8. Routing activo

- contexto insuficiente → `onboarding-empresa`;
- readiness incierto → `diagnostico-internacional`;
- ICP insuficiente → `definicion-icp`;
- comparación de países → `priorizacion-de-mercados`;
- investigación detallada de mercado → futura `investigacion-de-mercado`;
- partner → futura `evaluacion-de-distribuidores`;
- cuenta → futura `investigacion-de-cuentas`;
- reunión/acción → futura `preparacion-comercial`.

## 9. Principio WAT

- Workflow: proceso operativo.
- Agent: coordinación y juicio contextual.
- Tool: ejecución determinista.
- Skills: metodología especializada reutilizable.

## 10. Frontera pública

### Público

- contexto y onboarding;
- agente coordinador;
- contratos;
- skills GTM seleccionadas;
- workflows asistidos futuros;
- scorecards transparentes;
- tools locales sencillas;
- aprobación humana.

### Fuera del alcance base

- CRM/ERP de producción;
- monitoring continuo;
- scraping/enrichment industrializado;
- queues/retries/observabilidad;
- secrets management;
- multi-agent orchestration avanzada;
- permisos empresariales;
- learning loops automáticos;
- automatización de comunicaciones externas.

## 11. Criterios de calidad

Una nueva capacidad solo se añade cuando tiene responsabilidad diferenciada, contrato claro, dependencias, evaluación, evidencia, límites y compatibilidad con el agente y los contratos.

## 12. Evolución por fases

- Fase 1: constitución y convenciones — completada.
- Fase 2: Company Context Engine — completada.
- Fase 3: onboarding — completada.
- Fase 4: agente coordinador — completada.
- Fase 5: contratos compartidos — completada.
- Fase 6A: diagnóstico internacional, ICP y priorización de mercados — completada.
- Fase 6B: investigación de mercado y distribuidores — siguiente sprint.
- Fase 6C: investigación de cuentas y preparación comercial — posterior.
- Fase 7: workflows.
- Fase 8: tools deterministas.
- Fase 9+: memoria, QA, evaluaciones ejecutables, instalación y ejemplos.
