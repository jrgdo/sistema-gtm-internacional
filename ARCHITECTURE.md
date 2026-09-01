# Arquitectura del Sistema GTM Internacional

## 1. Objetivo

Construir un agente de IA personalizable que ayude a empresas B2B, especialmente industriales y técnicas, a estructurar decisiones de internacionalización, entrada en mercados y desarrollo comercial.

El sistema público debe ser útil por sí mismo, fácil de instalar y comprender, y suficientemente riguroso para producir trabajo real. Al mismo tiempo, no pretende sustituir una implementación empresarial conectada a CRM, ERP, fuentes de datos, automatización y governance avanzados.

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
ROUTING + ESTADOS + GATES + HANDOFFS
  ↓
WORKFLOW
  ↓
SKILLS
  ↓
TOOLS DETERMINISTAS CUANDO APLIQUE
  ↓
CONTROL DE EVIDENCIA / APROBACIÓN
  ↓
DECISIÓN HUMANA
  ↓
PERSISTENCIA VALIDADA
```

## 3. Responsabilidad de cada capa

### Instrucciones raíz
Definen cómo debe comportarse cualquier asistente que opere el repositorio.

### Company Context Engine
Mantiene contexto operativo de empresa con estados, procedencia, frescura, conflictos y reglas de actualización. No es una memoria indiscriminada del modelo.

### Onboarding de empresa
Convierte información proporcionada, documentación y contexto existente en una configuración GTM estructurada y validada para un objetivo concreto. No crea estrategia por defecto ni rellena huecos mediante inferencias.

### Agente GTM Internacional
Coordina el sistema. Identifica la decisión, comprueba contexto y dependencias, selecciona el camino mínimo, aplica gates y stops, gestiona handoffs y determina cuándo continuar, bloquear o escalar.

No debe duplicar la metodología que corresponde a skills especializadas.

### Workflow
Define la secuencia operativa y los gates de una tarea completa.

### Skill
Contiene metodología especializada reutilizable para una responsabilidad concreta.

### Tool
Ejecuta trabajo determinista: cálculos, schemas, persistencia, validación, transformación o integración.

### Memoria
Conserva decisiones, hipótesis y aprendizajes con estado y trazabilidad adecuados. Se implementará en una fase posterior y debe mantenerse separada de la verdad de empresa.

## 4. Company Context Engine

Las plantillas públicas del motor viven en `templates/contexto-empresa/`.

Una implementación concreta deberá crear un workspace local equivalente en `company-context/`.

Ese workspace no forma parte del repositorio público con datos reales de cliente.

### 4.1 Punto de entrada

`company-context/STATUS.md` debe leerse antes de cualquier trabajo GTM sustantivo.

Resume estado general, cobertura por dominio, última revisión, gaps materiales, conflictos abiertos e información que requiere actualización.

### 4.2 Dominios

El modelo inicial contempla empresa, productos y servicios, aplicaciones, ICP y clientes, mercados, estrategia, objetivo actual, ventas y canales, restricciones, aprobaciones, claims aprobados, marca y voz, y terminología.

El agente debe cargar solo los dominios relevantes para la decisión.

### 4.3 Estados de dominio

- `PENDIENTE`;
- `PARCIAL`;
- `VALIDADO`;
- `OBSOLETO`;
- `CONFLICTO`.

Estos estados resumen la salud de un dominio y no sustituyen la clasificación conceptual de cada afirmación.

### 4.4 Principios de persistencia

- No convertir investigación externa en verdad interna sin validación.
- No sobrescribir silenciosamente información confirmada.
- Tratar frescura según naturaleza del dato y decisión.
- Hacer visibles contradicciones materiales.
- Minimizar datos y no almacenar secretos.
- Mantener marca y voz separadas de hechos técnicos y estratégicos.
- Mantener el objetivo actual separado de verdad estable de empresa.

## 5. Skill de onboarding de empresa

La primera skill implementada y referencia inicial de calidad es `skills/onboarding-empresa/SKILL.md`.

### 5.1 Responsabilidad

Determinar si existe contexto suficiente para un objetivo GTM y, cuando no exista, construirlo mediante inspección documental, extracción de afirmaciones soportadas, preguntas adaptativas, detección de conflictos, validación humana y persistencia controlada.

### 5.2 Resultados operativos

- `CONTEXTO_VALIDADO_PARA_OBJETIVO`;
- `CONTEXTO_PARCIAL_UTILIZABLE`;
- `REQUIERE_VALIDACION`;
- `CONFLICTO_MATERIAL`;
- `INPUT_INSUFICIENTE`.

### 5.3 Principio de suficiencia

El onboarding se valida para un objetivo, no por porcentaje de plantillas completadas.

## 6. Agente GTM Internacional

El coordinador oficial vive en `agents/agente-gtm-internacional/AGENT.md`.

### 6.1 Responsabilidad

Debe poder responder correctamente:

> ¿Qué debe hacerse ahora, qué no debe hacerse todavía y por qué?

Su secuencia conceptual es:

```text
PETICIÓN
  ↓
IDENTIFICAR OBJETIVO / DECISIÓN
  ↓
VALIDAR CONTEXTO
  ↓
COMPROBAR DEPENDENCIAS
  ↓
ROUTING
  ↓
GATES
  ↓
WORKFLOW / SKILL / TOOL
  ↓
INTERPRETAR RESULTADO
  ↓
CONTINUAR / BLOQUEAR / ESCALAR / CERRAR
```

### 6.2 Estados operativos

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

No confundir estos estados con los estados de contexto ni con los resultados propios de cada skill.

### 6.3 Routing

El routing se basa en objetivo, decisión, contexto y dependencias, no únicamente en palabras clave.

Si no existe workflow formalizado, el agente puede invocar una skill directa cuando ésta resuelva correctamente el trabajo. Si tampoco existe capacidad formalizada, no debe simular que existe.

### 6.4 Camino mínimo

**Ejecutar el menor conjunto de componentes capaz de resolver correctamente la decisión.**

La sobreorquestación se considera un fallo de arquitectura.

### 6.5 Gates

Antes de avanzar downstream, comprobar prerequisites específicos.

Un gate puede devolver:

- `PASS`;
- `PASS_CON_LIMITES`;
- `REQUIERE_INPUT`;
- `REQUIERE_EVIDENCIA`;
- `REQUIERE_VALIDACION_HUMANA`;
- `BLOCK`.

### 6.6 Stops

Un stop puede ser la respuesta profesional correcta. El sistema debe detenerse ante contexto bloqueante, conflictos materiales, evidencia insuficiente, falta de aprobación o cuestiones fuera de su autoridad.

### 6.7 Handoffs

Los handoffs deben transportar la decisión, contexto relevante, restricciones, gaps, evidencia y criterio de finalización. En Fase 5 se formalizarán schemas compartidos.

### 6.8 Loops

Solo repetir componentes cuando exista nueva evidencia o cambio material de estado. Si no hay progreso, detener y revisar routing o escalar.

### 6.9 Escalado profesional

El agente debe escalar cuando la cuestión material exija expertise fiscal, legal, regulatorio, aduanero, financiero sensible o de ingeniería crítica.

Puede preparar un briefing útil, pero no sustituir a ese especialista.

### 6.10 Referencias y evaluación

Metodología de orquestación:

- `agents/agente-gtm-internacional/references/routing.md`;
- `agents/agente-gtm-internacional/references/estados.md`;
- `agents/agente-gtm-internacional/references/gates-de-decision.md`;
- `agents/agente-gtm-internacional/references/politica-de-handoffs.md`;
- `agents/agente-gtm-internacional/references/limites-operativos.md`.

Evaluación:

- `agents/agente-gtm-internacional/tests/escenarios.md`;
- `agents/agente-gtm-internacional/tests/criterios-de-evaluacion.md`.

## 7. Principio WAT aplicado

La arquitectura adopta el patrón conceptual Workflows–Agents–Tools sin convertir el acrónimo en la propuesta de valor.

- **Workflow:** proceso operativo.
- **Agent:** coordinación y juicio contextual.
- **Tool:** ejecución determinista.

Las skills complementan este patrón como módulos metodológicos especializados.

## 8. Frontera público / implementación profesional

### Público

- plantillas de contexto;
- onboarding manual/adaptativo;
- agente coordinador;
- contexto local;
- skills GTM seleccionadas;
- workflows manuales/asistidos;
- scorecards transparentes;
- tools locales sencillas;
- memoria básica futura;
- aprobación humana.

### Fuera del alcance base

- integraciones CRM/ERP;
- scheduling y monitoring continuo;
- scraping/enrichment de producción;
- colas, retries y observabilidad;
- credenciales y secrets management;
- multi-agent orchestration avanzada;
- políticas de permisos empresariales;
- data warehouse / analytics operativos;
- learning loops automáticos;
- automatización de comunicaciones externas.

## 9. Dependencias y routing

El sistema debe preferir el menor conjunto de componentes capaz de resolver correctamente la decisión.

No se permite construir un entregable downstream si faltan fundamentos upstream materiales.

Un contexto incompleto no bloquea automáticamente toda tarea: bloquea o reduce confianza únicamente cuando falta información material para la decisión concreta.

Cuando el contexto sea el bloqueo, enrutar primero a `onboarding-empresa`.

## 10. Criterios de calidad de arquitectura

Una nueva capacidad solo se añade cuando:

1. resuelve una responsabilidad diferenciada;
2. tiene contrato claro;
3. tiene dependencias explícitas;
4. puede evaluarse;
5. evita duplicar lógica;
6. respeta evidencia y aprobación;
7. encaja con empresas industriales B2B e internacionalización;
8. mantiene separada la lógica pública de una implementación privada de producción;
9. respeta las políticas del Company Context Engine;
10. puede integrarse limpiamente con el Agente GTM Internacional.

## 11. Evolución por fases

- **Fase 1:** constitución, arquitectura y convenciones. Completada.
- **Fase 2:** modelo y plantillas de contexto de empresa. Completada.
- **Fase 3:** skill de onboarding. Completada.
- **Fase 4:** agente GTM internacional, routing, estados, gates, handoffs, límites y evaluación. Completada.
- **Fase 5:** contratos compartidos.
- **Fase 6:** skills especializadas.
- **Fase 7:** workflows.
- **Fase 8:** tools deterministas.
- **Fase 9+:** memoria, QA, evaluaciones ejecutables, instalación y ejemplos.

No adelantar fases si las dependencias arquitectónicas no están cerradas.
