# Arquitectura del Sistema GTM Internacional

## 1. Objetivo

Construir un agente de IA personalizable que ayude a empresas B2B, especialmente industriales y técnicas, a estructurar decisiones de internacionalización, entrada en mercados y desarrollo comercial.

El sistema público debe ser útil por sí mismo, fácil de instalar y comprender, y suficientemente riguroso para producir trabajo real. No pretende sustituir una implementación empresarial conectada a CRM, ERP, fuentes de datos, automatización y governance avanzados.

## 2. Arquitectura lógica

```text
USUARIO
  ↓
AGENTS.md + CLAUDE.md / CODEX.md
  ↓
COMPANY CONTEXT ENGINE
  ↓
ONBOARDING-EMPRESA CUANDO SEA NECESARIO
  ↓
AGENTE GTM INTERNACIONAL
  ↓
CONTRATOS COMPARTIDOS
  ↓
ROUTING + ESTADOS + GATES + HANDOFFS
  ↓
WORKFLOW / SKILL / TOOL
  ↓
CONTROL DE EVIDENCIA / CONFIANZA / APROBACIÓN
  ↓
DECISIÓN HUMANA
  ↓
CIERRE Y PERSISTENCIA VALIDADA
```

## 3. Responsabilidad de cada capa

### Instrucciones raíz
Definen el comportamiento obligatorio del sistema.

### Company Context Engine
Mantiene contexto operativo con procedencia, frescura, conflictos y reglas de actualización.

### Onboarding de empresa
Construye o actualiza contexto suficiente para un objetivo concreto sin inventar huecos.

### Agente GTM Internacional
Coordina el sistema. Identifica la decisión, comprueba contexto y dependencias, aplica routing, gates, stops y handoffs.

### Contratos compartidos
Definen el lenguaje común entre agente, workflows, skills y tools. Separan estructura operativa de presentación al usuario.

### Workflow
Define la secuencia de una tarea completa.

### Skill
Contiene metodología especializada reutilizable.

### Tool
Ejecuta cálculo, validación, persistencia o transformación determinista.

### Memoria
Conservará decisiones, hipótesis y aprendizajes en una fase posterior, separada de la verdad de empresa.

## 4. Company Context Engine

Las plantillas públicas viven en `templates/contexto-empresa/`. Una implementación concreta utiliza `company-context/`.

`company-context/STATUS.md` es el punto de entrada y resume cobertura, gaps, conflictos y frescura.

El agente debe cargar solo los dominios relevantes para la decisión.

Estados de dominio:

- `PENDIENTE`;
- `PARCIAL`;
- `VALIDADO`;
- `OBSOLETO`;
- `CONFLICTO`.

## 5. Skill de onboarding

La referencia inicial de calidad es `skills/onboarding-empresa/SKILL.md`.

Resultados:

- `CONTEXTO_VALIDADO_PARA_OBJETIVO`;
- `CONTEXTO_PARCIAL_UTILIZABLE`;
- `REQUIERE_VALIDACION`;
- `CONFLICTO_MATERIAL`;
- `INPUT_INSUFICIENTE`.

El onboarding se valida para un objetivo, no por porcentaje de plantillas completadas.

## 6. Agente GTM Internacional

El coordinador oficial vive en `agents/agente-gtm-internacional/AGENT.md`.

Debe responder:

> ¿Qué debe hacerse ahora, qué no debe hacerse todavía y por qué?

Estados operativos principales:

- `SIN_CONFIGURAR`;
- `CONTEXTUALIZANDO`;
- `CONTEXTO_PARCIAL`;
- `LISTO_PARA_ROUTING`;
- `REQUIERE_CLARIFICACION`;
- `REQUIERE_EVIDENCIA`;
- `EN_EJECUCION`;
- `REQUIERE_VALIDACION_HUMANA`;
- `LISTO_PARA_DECISION`;
- `BLOQUEADO`;
- `CERRADO`.

El routing se basa en objetivo, decisión, contexto y dependencias. La sobreorquestación se considera un fallo de arquitectura.

## 7. Contratos compartidos

La Fase 5 formaliza la interoperabilidad en `contracts/`.

### 7.1 Entrada de componente

`contracts/entrada-componente.yaml`

Transporta objetivo, decisión, contexto relevante, inputs confirmados, restricciones, gaps, evidencia disponible, destino y criterio de finalización.

### 7.2 Salida de componente

`contracts/salida-componente.yaml`

Separa resultado, hechos, inferencias, hipótesis, supuestos, desconocidos, evidencia, confianza, riesgos, validación, siguiente acción y persistencia.

### 7.3 Evidencia

`contracts/evidencia.yaml`

Conserva relación entre una afirmación y su fuente, fecha, alcance, calidad, limitaciones y conflictos.

### 7.4 Decisión

`contracts/decision.yaml`

Representa una decisión preparada para revisión humana. Una recomendación no equivale a una decisión aprobada.

### 7.5 Handoff

`contracts/handoff.yaml`

Permite transferir trabajo sin reabrir todo el contexto. Debe conservar gaps y conflictos.

### 7.6 Errores y bloqueos

`contracts/error-operativo.yaml`

Formaliza bloqueos por contexto, evidencia, conflicto, approval, scope o ejecución.

### 7.7 Estados y confianza

`contracts/estados.yaml` mantiene vocabularios separados por capa.

`contracts/confianza.yaml` define `ALTA`, `MEDIA`, `BAJA` y `NO_EVALUABLE` basándose en contexto y evidencia, nunca en fluidez del modelo.

### 7.8 Cierre

`contracts/cierre-ejecucion.yaml`

Resume el resultado coordinado y prepara la futura capa de memoria y decision logging.

Los contratos son internos y no obligan a mostrar YAML al usuario.

## 8. Principio WAT aplicado

- **Workflow:** proceso operativo.
- **Agent:** coordinación y juicio contextual.
- **Tool:** ejecución determinista.

Las skills complementan el patrón como módulos metodológicos especializados.

## 9. Frontera público / implementación profesional

### Público

- contexto local;
- onboarding adaptativo;
- agente coordinador;
- contratos compartidos;
- skills GTM seleccionadas;
- workflows asistidos;
- scorecards transparentes;
- tools locales sencillas;
- aprobación humana.

### Fuera del alcance base

- CRM/ERP;
- scheduling y monitoring continuo;
- scraping/enrichment de producción;
- colas, retries y observabilidad;
- secrets management;
- multi-agent orchestration avanzada;
- permisos empresariales;
- data warehouse;
- learning loops automáticos;
- automatización de comunicaciones externas.

## 10. Criterios de calidad

Una nueva capacidad solo se añade cuando:

1. resuelve una responsabilidad diferenciada;
2. tiene contrato claro;
3. tiene dependencias explícitas;
4. puede evaluarse;
5. evita duplicación;
6. respeta evidencia y aprobación;
7. encaja con industrial B2B e internacionalización;
8. respeta Company Context Engine;
9. se integra con el Agente GTM Internacional;
10. consume y produce contratos compartidos de forma coherente.

## 11. Evolución por fases

- **Fase 1:** constitución, arquitectura y convenciones. Completada.
- **Fase 2:** Company Context Engine. Completada.
- **Fase 3:** onboarding de empresa. Completada.
- **Fase 4:** Agente GTM Internacional. Completada.
- **Fase 5:** contratos compartidos. Completada a nivel declarativo.
- **Fase 6:** skills especializadas.
- **Fase 7:** workflows.
- **Fase 8:** tools deterministas y validación ejecutable de contratos.
- **Fase 9+:** memoria, QA, evaluaciones ejecutables, instalación y ejemplos.

No adelantar fases si las dependencias arquitectónicas no están cerradas.
