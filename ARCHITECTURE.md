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

### Agente
Decide qué proceso ejecutar, qué información falta, qué skill necesita y cuándo detenerse o pedir validación.

### Workflow
Define la secuencia operativa y los gates de una tarea completa.

### Skill
Contiene metodología especializada reutilizable para una responsabilidad concreta.

### Tool
Ejecuta trabajo determinista: cálculos, schemas, persistencia, validación, transformación o integración.

### Contexto de empresa
Contiene la verdad validada de la empresa, separada de investigación externa e hipótesis.

### Memoria
Conserva decisiones, hipótesis y aprendizajes con estado y trazabilidad adecuados.

## 4. Principio WAT aplicado

La arquitectura adopta el patrón conceptual Workflows–Agents–Tools sin convertir el acrónimo en la propuesta de valor.

- **Workflow:** proceso operativo.
- **Agent:** coordinación y juicio contextual.
- **Tool:** ejecución determinista.

Las skills complementan este patrón como módulos metodológicos especializados.

## 5. Frontera público / implementación profesional

### Público

- onboarding manual;
- contexto local;
- skills GTM seleccionadas;
- workflows manuales/asistidos;
- scorecards transparentes;
- tools locales sencillas;
- memoria básica;
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

## 6. Dependencias y routing

El sistema debe preferir el menor conjunto de componentes capaz de resolver correctamente la decisión.

No se permite construir un entregable downstream si faltan fundamentos upstream materiales.

Ejemplos:

- no priorizar mercados sin comprender oferta, ICP y restricciones mínimas;
- no evaluar un distribuidor sin definir qué partner necesita la empresa;
- no redactar un approach comercial sin comprender cuenta, objetivo y valor relevante;
- no concluir sobre performance sin datos observados.

## 7. Modelo de estado

Las futuras ejecuciones deben poder distinguir al menos:

- `SIN_CONFIGURAR`;
- `CONTEXTO_PARCIAL`;
- `CONTEXTO_VALIDADO`;
- `EN_ANALISIS`;
- `REQUIERE_EVIDENCIA`;
- `REQUIERE_VALIDACION_HUMANA`;
- `LISTO_PARA_DECISION`;
- `CERRADO`.

Los estados exactos se formalizarán en fases posteriores.

## 8. Criterios de calidad de arquitectura

Una nueva capacidad solo se añade cuando:

1. resuelve una responsabilidad diferenciada;
2. tiene contrato claro;
3. tiene dependencias explícitas;
4. puede evaluarse;
5. evita duplicar lógica;
6. respeta evidencia y aprobación;
7. encaja con empresas industriales B2B e internacionalización;
8. mantiene separada la lógica pública de una implementación privada de producción.

## 9. Evolución por fases

- **Fase 1:** constitución, arquitectura y convenciones.
- **Fase 2:** modelo de contexto de empresa.
- **Fase 3:** skill de onboarding.
- **Fase 4:** agente GTM internacional.
- **Fase 5:** contratos compartidos.
- **Fase 6:** skills especializadas.
- **Fase 7:** workflows.
- **Fase 8:** tools deterministas.
- **Fase 9+:** memoria, QA, evaluaciones, instalación y ejemplos.

No adelantar fases si las dependencias arquitectónicas no están cerradas.
