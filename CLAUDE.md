# Guía operativa para Claude Code

Claude Code debe tratar este repositorio como un sistema GTM estructurado, no como una colección de prompts.

## Inicio obligatorio

Antes de realizar trabajo sustantivo:

1. lee `AGENTS.md`;
2. lee `ARCHITECTURE.md`;
3. carga únicamente la documentación relevante de `docs/`;
4. comprueba si existe contexto de empresa válido;
5. si falta contexto esencial, no lo inventes;
6. identifica el objetivo y la decisión comercial;
7. selecciona el workflow y las skills mínimas necesarias;
8. utiliza tools deterministas cuando exista una herramienta adecuada;
9. aplica las reglas de evidencia, aprobación y persistencia antes de cerrar la tarea.

## Uso del sistema de archivos

Cuando el repositorio evolucione y exista contexto local de empresa:

- lee primero su estado antes de utilizarlo;
- no sobrescribas información confirmada con investigación externa;
- conserva por separado verdad de empresa, hipótesis y aprendizaje;
- evita guardar datos personales o confidenciales que no sean necesarios;
- no incluyas credenciales, tokens o secretos en archivos versionados.

## Comportamiento de primera ejecución

Si no existe una configuración válida de empresa, la respuesta correcta no es generar una estrategia genérica. Debe iniciarse el proceso de onboarding cuando esté disponible.

Mientras el onboarding todavía no exista, identifica explícitamente la información mínima necesaria y no presentes recomendaciones definitivas.

## Uso de herramientas

Claude Code puede utilizar filesystem, terminal, búsqueda u otras capacidades autorizadas para ejecutar trabajo verificable.

Principio:

- razonamiento, interpretación y síntesis → modelo;
- cálculos, validaciones, schemas, transformaciones y operaciones repetibles → código/tool cuando exista.

No ejecutes acciones externas sensibles sin autorización explícita.

## Calidad

Antes de finalizar un entregable GTM, verifica:

- ¿la decisión está clara?;
- ¿la evidencia respalda la recomendación?;
- ¿se han señalado gaps e hipótesis?;
- ¿la recomendación está adaptada a industrial B2B cuando corresponde?;
- ¿hay una siguiente acción concreta?;
- ¿requiere aprobación humana?;
- ¿se ha evitado guardar información no validada como verdad?

## Idioma

Trabaja en español por defecto dentro de este repositorio. Puedes investigar fuentes en otros idiomas y producir materiales localizados cuando el mercado objetivo lo requiera.
