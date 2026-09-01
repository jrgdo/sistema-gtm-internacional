# Arquitectura del Sistema GTM Internacional

## 1. Objetivo

Construir un sistema agentic GTM personalizable para empresas B2B, especialmente industriales y técnicas, que conecte contexto, decisiones, workflows, skills, tools, QA y memoria sin sustituir autoridad humana ni fingir certeza.

## 2. Arquitectura lógica

```text
USUARIO
  ↓
AGENTS.md / CLAUDE.md / CODEX.md
  ↓
SISTEMA-GTM-INTERNACIONAL (bootstrap instalable)
  ↓
COMPANY CONTEXT ENGINE
  ↓
AGENTE GTM INTERNACIONAL
  ↓
ROUTING + GATES + CONTRATOS
  ↓
WORKFLOW / SKILL
  ↓
TOOLS DETERMINISTAS
  ↓
QUALITY GUARD
  ↓
DECISIÓN HUMANA
  ↓
MEMORIA VALIDADA
```

## 3. Capas

### Instrucciones raíz
Definen misión, límites, tests y comportamiento global.

### Skill de entrada instalable
`skills/sistema-gtm-internacional/` permite una experiencia de Agent Skills sin depender de que el CLI copie todos los archivos del root. Incluye bootstrap de `company-context/`.

### Company Context Engine
`company-context/` mantiene verdad operativa validada de una implementación concreta. `templates/contexto-empresa/` contiene plantillas públicas para el repositorio completo.

### Agente GTM Internacional
Coordina objetivo, routing, prerequisites, gates, stops, handoffs, loops y escalado.

### Contratos
`contracts/` define entrada, salida, evidencia, decisión, confianza, error, estados, handoff y cierre.

### Workflows
`workflows/` compone varias capacidades en procesos completos. Controla secuencia y gates, no metodología especialista.

### Skills
`skills/` contiene metodología profesional reusable para responsabilidades concretas.

### Tools
`tools/` ejecuta validación, cálculo y persistencia determinista.

### Quality Guard
`qa/QUALITY-GUARD.md` revisa propiedades críticas antes de considerar un resultado listo para decisión.

### Memoria
`memory/` separa decisiones, hipótesis y aprendizajes de la verdad estable de empresa.

## 4. Skills implementadas

1. `sistema-gtm-internacional`
2. `onboarding-empresa`
3. `diagnostico-internacional`
4. `definicion-icp`
5. `priorizacion-de-mercados`
6. `investigacion-de-mercado`
7. `evaluacion-de-distribuidores`
8. `investigacion-de-cuentas`
9. `preparacion-comercial`

## 5. Workflows implementados

1. configurar agente;
2. diagnosticar expansión;
3. comparar mercados;
4. explorar nuevo mercado;
5. evaluar distribuidor;
6. investigar cuenta;
7. preparar reunión.

## 6. Cadena estratégica

Cuando el objetivo lo requiere:

```text
CONTEXTO
  ↓
READINESS
  ↓
ICP
  ↓
PRIORIZACIÓN
  ↓
INVESTIGACIÓN
  ↓
PARTNER / CUENTA
  ↓
PREPARACIÓN COMERCIAL
```

No ejecutar toda la cadena por defecto. El Agente GTM aplica camino mínimo.

## 7. Modelo de verdad

Todo el sistema debe poder distinguir:

- hecho confirmado;
- evidencia externa;
- inferencia;
- hipótesis;
- supuesto;
- desconocido;
- conflicto;
- información obsoleta.

La fluidez del modelo nunca aumenta por sí sola la confianza.

## 8. Principios de decisión

- mercado atractivo != mercado ganable;
- research != validación de mercado;
- discovery de distribuidor != qualification;
- cuenta con fit != oportunidad confirmada;
- cargo != autoridad;
- señal != intención;
- unknown != cero;
- score != decisión;
- aprendizaje != causalidad.

## 9. Tools y determinismo

Código cuando una operación debe ser reproducible:

- estructura de contexto;
- scorecards con criterios/pesos explícitos;
- cobertura/unknowns;
- registros de decisión;
- validación de contratos.

Los pesos y criterios no se inventan en código.

## 10. Governance

Requieren validación humana o expertise adecuado, según impacto:

- claims técnicos;
- certificaciones/regulación;
- pricing/descuentos;
- garantías;
- exclusividad;
- contratos;
- capacidad/lead times comprometidos;
- ROI/resultados cliente;
- comunicaciones externas sensibles.

## 11. Frontera público / implementación profesional

### Público

- contexto y onboarding;
- agente coordinador;
- skills GTM;
- workflows asistidos;
- contratos;
- scorecards transparentes;
- tools locales;
- QA ligero;
- memoria local;
- tests y CI;
- documentación y ejemplos.

### Fuera del alcance base

- CRM/ERP sync de producción;
- monitoring/scheduling continuo;
- enrichment masivo;
- queues/retries/observabilidad empresarial;
- secrets/permissions de producción;
- multi-agent orchestration avanzada;
- scoring propietario avanzado;
- analytics operativos de cliente;
- learning loops automáticos;
- ejecución autónoma de comunicaciones externas.

## 12. Instalación

### Agent Skills

`skills/sistema-gtm-internacional/` es la capa de bootstrap instalable. El CLI de skills distribuye las carpetas de skill, no necesariamente la arquitectura completa del root.

### Clone completo

El repositorio completo es la opción para builders y equipos que necesitan workflows, tools, QA, tests y documentación de arquitectura.

## 13. Calidad y CI

GitHub Actions ejecuta comprobaciones de sintaxis y estructura. Además, cada skill/agente contiene escenarios de evaluación documental y el sistema define properties críticas en Quality Guard.

## 14. Evolución

La primera arquitectura pública está implementada. Las siguientes capacidades deben añadirse por evidencia de uso real, no por volumen de agentes o skills.

Consultar `ROADMAP.md`.
