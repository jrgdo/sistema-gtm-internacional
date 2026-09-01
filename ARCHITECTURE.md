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
VALIDACIÓN DE CONTEXTO
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

### Agente
Decide qué proceso ejecutar, qué información falta, qué skill necesita y cuándo detenerse o pedir validación.

### Workflow
Define la secuencia operativa y los gates de una tarea completa.

### Skill
Contiene metodología especializada reutilizable para una responsabilidad concreta.

### Tool
Ejecuta trabajo determinista: cálculos, schemas, persistencia, validación, transformación o integración.

### Memoria
Conserva decisiones, hipótesis y aprendizajes con estado y trazabilidad adecuados. Se implementará en una fase posterior y debe mantenerse separada de la verdad de empresa.

## 4. Company Context Engine

Las plantillas públicas del motor viven en:

`templates/contexto-empresa/`

Una implementación concreta deberá crear un workspace local equivalente en:

`company-context/`

Ese workspace no forma parte del repositorio público con datos reales de cliente.

### 4.1 Punto de entrada

`company-context/STATUS.md` debe leerse antes de cualquier trabajo GTM sustantivo.

Resume:

- estado general;
- cobertura por dominio;
- última revisión;
- gaps materiales;
- conflictos abiertos;
- información que requiere actualización.

### 4.2 Dominios

El modelo inicial contempla:

- empresa;
- productos y servicios;
- aplicaciones;
- ICP y clientes;
- mercados;
- estrategia;
- objetivo actual;
- ventas y canales;
- restricciones;
- aprobaciones;
- claims aprobados;
- marca y voz;
- terminología.

El agente debe cargar solo los dominios relevantes para la decisión.

### 4.3 Estados de dominio

- `PENDIENTE`;
- `PARCIAL`;
- `VALIDADO`;
- `OBSOLETO`;
- `CONFLICTO`.

Estos estados resumen la salud de un dominio y no sustituyen la clasificación conceptual de cada afirmación como confirmada, inferida, hipótesis, pendiente de validación, obsoleta o conflictiva.

### 4.4 Principios de persistencia

- No convertir investigación externa en verdad interna sin validación.
- No sobrescribir silenciosamente información confirmada.
- Tratar frescura según naturaleza del dato y decisión, no con una caducidad universal.
- Hacer visibles contradicciones materiales.
- Minimizar datos y no almacenar secretos.
- Mantener la marca y voz separadas de hechos técnicos y estratégicos.
- Mantener el objetivo actual separado de verdad estable de empresa.

Las políticas están documentadas en:

- `docs/politica-de-escritura-de-contexto.md`;
- `docs/politica-de-frescura.md`;
- `docs/gestion-de-conflictos.md`.

## 5. Skill de onboarding de empresa

La primera skill implementada y referencia inicial de calidad es:

`skills/onboarding-empresa/SKILL.md`

### 5.1 Responsabilidad

Determinar si existe contexto suficiente para un objetivo GTM y, cuando no exista, construirlo mediante:

1. inspección del contexto y documentos disponibles;
2. extracción de afirmaciones soportadas;
3. mapa de cobertura por dominio;
4. preguntas adaptativas sobre gaps materiales;
5. detección de conflictos y obsolescencia;
6. validación humana de elementos relevantes;
7. persistencia controlada en `company-context/`;
8. declaración de readiness y siguiente handoff.

### 5.2 Resultados operativos

La skill puede terminar en:

- `CONTEXTO_VALIDADO_PARA_OBJETIVO`;
- `CONTEXTO_PARCIAL_UTILIZABLE`;
- `REQUIERE_VALIDACION`;
- `CONFLICTO_MATERIAL`;
- `INPUT_INSUFICIENTE`.

### 5.3 Principio de suficiencia

El onboarding se valida para un objetivo, no por porcentaje de plantillas completadas.

Un contexto parcial puede ser suficiente para una investigación concreta. Un contexto aparentemente completo puede ser insuficiente para una decisión sensible si faltan restricciones, aprobación o información vigente.

### 5.4 Referencias y evaluación

La metodología especializada vive en:

- `skills/onboarding-empresa/references/preguntas-onboarding.md`;
- `skills/onboarding-empresa/references/extraccion-de-documentos.md`;
- `skills/onboarding-empresa/references/validacion-de-contexto.md`.

La skill se evalúa con:

- `skills/onboarding-empresa/tests/escenarios.md`;
- `skills/onboarding-empresa/tests/criterios-de-evaluacion.md`.

## 6. Principio WAT aplicado

La arquitectura adopta el patrón conceptual Workflows–Agents–Tools sin convertir el acrónimo en la propuesta de valor.

- **Workflow:** proceso operativo.
- **Agent:** coordinación y juicio contextual.
- **Tool:** ejecución determinista.

Las skills complementan este patrón como módulos metodológicos especializados.

## 7. Frontera público / implementación profesional

### Público

- plantillas de contexto;
- onboarding manual/adaptativo;
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

## 8. Dependencias y routing

El sistema debe preferir el menor conjunto de componentes capaz de resolver correctamente la decisión.

No se permite construir un entregable downstream si faltan fundamentos upstream materiales.

Ejemplos:

- no priorizar mercados sin comprender oferta, ICP y restricciones mínimas;
- no evaluar un distribuidor sin definir qué partner necesita la empresa;
- no redactar un approach comercial sin comprender cuenta, objetivo y valor relevante;
- no concluir sobre performance sin datos observados.

Un contexto incompleto no bloquea automáticamente toda tarea: bloquea o reduce confianza únicamente cuando falta información material para la decisión concreta.

Cuando el contexto sea el bloqueo, enrutar primero a `onboarding-empresa`.

## 9. Modelo de estado del sistema

Las futuras ejecuciones deben poder distinguir al menos:

- `SIN_CONFIGURAR`;
- `CONTEXTO_PARCIAL`;
- `CONTEXTO_VALIDADO`;
- `EN_ANALISIS`;
- `REQUIERE_EVIDENCIA`;
- `REQUIERE_VALIDACION_HUMANA`;
- `LISTO_PARA_DECISION`;
- `CERRADO`.

Los estados exactos de ejecución se formalizarán en fases posteriores. No confundir estos estados de ejecución con los estados de los dominios de contexto ni con los resultados propios de una skill.

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
9. respeta las políticas del Company Context Engine.

`skills/onboarding-empresa/` sirve como referencia inicial del nivel de especificación esperado, pero no debe copiarse mecánicamente cuando otra skill requiera una metodología diferente.

## 11. Evolución por fases

- **Fase 1:** constitución, arquitectura y convenciones. Completada.
- **Fase 2:** modelo y plantillas de contexto de empresa. Completada.
- **Fase 3:** skill de onboarding. Completada a nivel de metodología, referencias y evaluación documental.
- **Fase 4:** agente GTM internacional.
- **Fase 5:** contratos compartidos.
- **Fase 6:** skills especializadas.
- **Fase 7:** workflows.
- **Fase 8:** tools deterministas.
- **Fase 9+:** memoria, QA, evaluaciones ejecutables, instalación y ejemplos.

No adelantar fases si las dependencias arquitectónicas no están cerradas.
