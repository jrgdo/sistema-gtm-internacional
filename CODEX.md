# Guía operativa para Codex

Codex debe tratar este repositorio como un sistema GTM estructurado, no como una colección de prompts.

`AGENTS.md` es la instrucción raíz del proyecto. Este archivo añade notas específicas de ejecución para Codex.

## Inicio obligatorio

Antes de realizar trabajo sustantivo:

1. lee `AGENTS.md`;
2. lee `ARCHITECTURE.md`;
3. carga únicamente la documentación relevante de `docs/`;
4. comprueba si existe `company-context/STATUS.md`;
5. si existe, léelo primero y determina qué dominios son necesarios para la decisión;
6. valida estado, frescura y conflictos de esos dominios;
7. si falta contexto esencial, no lo inventes;
8. identifica el objetivo y la decisión comercial;
9. selecciona el workflow y las skills mínimas necesarias;
10. utiliza tools deterministas cuando exista una herramienta adecuada;
11. aplica las reglas de evidencia, aprobación y persistencia antes de cerrar la tarea.

## Uso de archivos, shell y herramientas

Cuando estén disponibles y autorizadas, utiliza filesystem, shell y otras herramientas para realizar operaciones verificables.

Principio:

- juicio, interpretación y síntesis → modelo;
- cálculo, validación, persistencia y transformación repetible → tool o código.

No uses código para ocultar una decisión metodológica que debería ser explícita. No uses razonamiento probabilístico del modelo para operaciones que deben ser deterministas.

## Company Context Engine

Las plantillas públicas viven en `templates/contexto-empresa/`. El contexto operativo de una empresa concreta debe vivir en `company-context/`.

`company-context/STATUS.md` es el punto de entrada obligatorio al contexto. No cargues todos los dominios por defecto.

Antes de usar o modificar contexto:

- comprueba procedencia y estado;
- comprueba si la frescura puede cambiar la decisión;
- identifica conflictos abiertos;
- aplica `docs/politica-de-escritura-de-contexto.md`;
- aplica `docs/politica-de-frescura.md`;
- usa `docs/gestion-de-conflictos.md` si dos fuentes materiales no coinciden.

No conviertas inferencias en verdad de empresa y no sobrescribas hechos confirmados a partir de una sola fuente externa.

## Primera ejecución

Si falta contexto válido de empresa, no produzcas una estrategia genérica como sustituto.

Mientras el onboarding no esté implementado, utiliza `templates/contexto-empresa/` para identificar y estructurar el contexto mínimo necesario. Nunca completes huecos con datos inventados.

## Cambios en el repositorio

Antes de crear una nueva skill, workflow o tool:

1. comprueba si ya existe una capacidad equivalente;
2. lee la convención correspondiente en `docs/`;
3. define responsabilidad, contrato y criterios de calidad;
4. evita duplicación;
5. añade tests o criterios de validación cuando la fase correspondiente lo permita.

## Checklist antes de cerrar una tarea

- objetivo/decisión entendidos;
- contexto suficiente, vigente y sin conflictos bloqueantes;
- evidencia proporcionada o identificada;
- hechos e hipótesis separados;
- riesgos y gaps visibles;
- recomendación proporcional a la confianza;
- siguiente acción clara;
- aprobación humana señalada cuando aplica;
- persistencia compatible con la política de contexto.

## Idioma

Trabaja en español por defecto. Las fuentes y entregables de mercado pueden utilizar otros idiomas cuando la tarea de internacionalización lo requiera.
