# Arquitectura del Sistema GTM Internacional

## 1. Objetivo

Construir un agente de IA personalizable que ayude a empresas B2B, especialmente industriales y técnicas, a estructurar decisiones de internacionalización, entrada en mercados y desarrollo comercial.

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

- **Contexto:** verdad operativa con procedencia, estado y frescura.
- **Onboarding:** configura contexto suficiente para el objetivo.
- **Agente:** coordina decisión, routing, gates y camino mínimo.
- **Contratos:** lenguaje común entre componentes.
- **Skills:** metodología profesional reutilizable.
- **Workflows:** composición de capacidades en Fase 7.
- **Tools:** operaciones deterministas en Fase 8.

## 4. Skills implementadas

### `onboarding-empresa`
Configura o actualiza el Company Context Engine.

### `diagnostico-internacional`
Evalúa readiness interno para un objetivo internacional concreto.

### `definicion-icp`
Define qué tipo de organización merece prioridad comercial para una oferta y aplicación.

### `priorizacion-de-mercados`
Compara mercados separando:

```text
ATRACTIVO
+
CAPACIDAD DE GANAR
+
FRICCIÓN / RIESGO
```

### `investigacion-de-mercado`
Produce inteligencia externa orientada a una decisión concreta.

Principio:

```text
DECISIÓN
↓
HIPÓTESIS
↓
PLAN DE EVIDENCIA
↓
FUENTES ADECUADAS
↓
HECHOS / INFERENCIAS / UNKNOWNs
↓
IMPLICACIÓN GTM
↓
SIGUIENTE VALIDACIÓN
```

Desk research no equivale a market validation.

### `evaluacion-de-distribuidores`
Evalúa candidatos de canal con evidencia sobre fit, acceso, cobertura, capacidad, conflictos, prioridad y siguiente compromiso.

Distingue:

```text
DISCOVERY
≠
PRE-EVALUACIÓN
≠
QUALIFICATION
≠
SELECCIÓN / CONTRATACIÓN
```

La selección contractual final permanece humana.

## 5. Secuencia estratégica

Cuando las dependencias lo justifican:

```text
ONBOARDING
↓
DIAGNÓSTICO
↓
ICP
↓
PRIORIZACIÓN
↓
INVESTIGACIÓN DE MERCADO
↓
EVALUACIÓN DE CANAL / PARTNERS
```

El agente debe aplicar camino mínimo; esta cadena no es obligatoria en todas las ejecuciones.

## 6. Research loop

Loop permitido:

```text
PRIORIZACIÓN
→ gap de evidencia
→ INVESTIGACIÓN DE MERCADO
→ nueva evidencia
→ REPRIORIZACIÓN
```

Solo repetir si cambia la evidencia o el estado.

## 7. Contratos compartidos

Todo componente debe ser compatible con `contracts/` y mantener separados hechos, inferencias, hipótesis, supuestos, desconocidos, evidencia, confianza y decisión.

## 8. Routing activo

- contexto insuficiente → `onboarding-empresa`;
- readiness incierto → `diagnostico-internacional`;
- ICP insuficiente → `definicion-icp`;
- comparación de países → `priorizacion-de-mercados`;
- evidencia detallada de mercado → `investigacion-de-mercado`;
- partner identificado → `evaluacion-de-distribuidores`;
- cuenta → futura `investigacion-de-cuentas`;
- reunión/acción → futura `preparacion-comercial`.

## 9. Frontera pública

El repositorio incluye metodología, contexto local, research asistido, evaluación transparente y aprobación humana.

Quedan fuera del alcance base integraciones de producción, CRM/ERP, monitoring continuo, enrichment industrializado, secrets management, multi-agent orchestration avanzada, automatización de comunicaciones y learning loops automáticos.

## 10. Evolución por fases

- Fase 1: constitución — completada.
- Fase 2: Company Context Engine — completada.
- Fase 3: onboarding — completada.
- Fase 4: agente coordinador — completada.
- Fase 5: contratos — completada.
- Fase 6A: diagnóstico, ICP y priorización — completada.
- Fase 6B: investigación de mercado y distribuidores — completada.
- Fase 6C: investigación de cuentas y preparación comercial — siguiente sprint.
- Fase 7: workflows.
- Fase 8: tools deterministas.
- Fase 9+: memoria, QA, evaluaciones ejecutables, instalación y ejemplos.
