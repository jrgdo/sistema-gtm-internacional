# Guía operativa para Claude Code

Claude Code debe tratar este repositorio como un sistema GTM estructurado, no como una colección de prompts.

## Inicio obligatorio

Antes de realizar trabajo sustantivo:

1. lee `AGENTS.md`;
2. lee `ARCHITECTURE.md`;
3. lee `agents/agente-gtm-internacional/AGENT.md`;
4. carga únicamente la documentación relevante de `docs/`;
5. comprueba si existe `company-context/STATUS.md`;
6. si existe, léelo primero y determina qué dominios son relevantes para la decisión;
7. comprueba estado, frescura y conflictos antes de usar esos dominios;
8. si falta contexto esencial, ejecuta `skills/onboarding-empresa/SKILL.md`;
9. tras onboarding o validación de contexto, devuelve el control al Agente GTM Internacional para routing;
10. selecciona el workflow y las skills mínimas necesarias cuando existan;
11. utiliza tools deterministas cuando exista una herramienta adecuada;
12. aplica las reglas de evidencia, aprobación y persistencia antes de cerrar la tarea.

## Agente GTM Internacional

`agents/agente-gtm-internacional/AGENT.md` es la capa de coordinación.

Debe decidir:

- qué decisión o entregable intenta preparar el usuario;
- qué contexto es material;
- qué componente usar;
- qué dependencies deben cumplirse;
- cuándo avanzar, bloquear o escalar;
- cuándo solicitar validación humana.

Aplicar siempre el principio de camino mínimo: no ejecutar componentes innecesarios.

Consultar sus referencias de routing, estados, gates, handoffs y límites cuando la ejecución lo requiera.

## Company Context Engine

Las plantillas públicas viven en `templates/contexto-empresa/`. En una implementación concreta, el contexto operativo debe vivir en `company-context/`.

`company-context/STATUS.md` es el índice de salud del contexto. No cargues todos los archivos automáticamente si no son necesarios.

Antes de confiar en un dato, comprueba:

- si está confirmado o es una inferencia;
- si procede de una fuente autorizada;
- si sigue vigente para la decisión actual;
- si existe un conflicto abierto;
- si requiere aprobación humana.

No sobrescribas información confirmada con investigación externa. Si una nueva fuente contradice el contexto, registra el conflicto y escala según `docs/gestion-de-conflictos.md`.

## Primera ejecución y onboarding

Si no existe una configuración válida de empresa, no generes una estrategia genérica.

Ejecuta `skills/onboarding-empresa/SKILL.md` y sigue este orden:

1. revisar documentos y contexto disponible;
2. detectar cobertura, gaps, obsolescencia y conflictos;
3. preguntar solo la información material que falta;
4. presentar un resumen de validación;
5. crear o actualizar `company-context/` solo con información permitida;
6. actualizar `STATUS.md`;
7. declarar qué trabajo GTM queda habilitado o bloqueado.

No ejecutes onboarding completo si el contexto ya es suficiente para el objetivo actual.

## Routing, gates y stops

Antes de ejecutar una capacidad downstream:

- comprobar prerequisites;
- no inventar inputs faltantes;
- permitir `PASS_CON_LIMITES` cuando el gap no sea material;
- detenerse si existe conflicto, evidencia insuficiente o aprobación obligatoria;
- escalar a expertise humano especializado cuando la cuestión material sea fiscal, legal, regulatoria, aduanera, financiera sensible o de ingeniería crítica.

Un stop correcto no es un error del sistema.

## Uso del sistema de archivos

Cuando exista contexto local de empresa:

- lee `STATUS.md` antes de los dominios específicos;
- conserva por separado verdad de empresa, hipótesis e investigación;
- aplica `docs/politica-de-escritura-de-contexto.md` antes de persistir cambios;
- aplica `docs/politica-de-frescura.md` cuando la fecha pueda cambiar la decisión;
- evita guardar datos personales o confidenciales que no sean necesarios;
- no incluyas credenciales, tokens o secretos en archivos versionados.

## Uso de herramientas

Claude Code puede utilizar filesystem, terminal, búsqueda u otras capacidades autorizadas para ejecutar trabajo verificable.

Principio:

- razonamiento, interpretación y síntesis → modelo;
- cálculos, validaciones, schemas, transformaciones y operaciones repetibles → código/tool cuando exista.

No ejecutes acciones externas sensibles sin autorización explícita.

## Calidad

Antes de finalizar un entregable GTM, verifica:

- ¿la decisión está clara?;
- ¿el contexto utilizado está suficientemente validado y vigente?;
- ¿se ha utilizado el camino mínimo?;
- ¿se han respetado prerequisites y gates?;
- ¿la evidencia respalda la recomendación?;
- ¿se han señalado gaps, conflictos e hipótesis?;
- ¿la recomendación está adaptada a industrial B2B cuando corresponde?;
- ¿hay una siguiente acción concreta?;
- ¿requiere aprobación humana o expertise especializado?;
- ¿se ha evitado guardar información no validada como verdad?

## Idioma

Trabaja en español por defecto dentro de este repositorio. Puedes investigar fuentes en otros idiomas y producir materiales localizados cuando el mercado objetivo lo requiera.
