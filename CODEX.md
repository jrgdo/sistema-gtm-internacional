# Guía operativa para Codex

Codex debe tratar este repositorio como un sistema GTM estructurado, no como una colección de prompts.

`AGENTS.md` es la instrucción raíz del proyecto. Este archivo añade notas específicas de ejecución para Codex.

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

## Uso de archivos, shell y herramientas

Cuando estén disponibles y autorizadas, utiliza filesystem, shell y otras herramientas para realizar operaciones verificables.

Principio:

- juicio, interpretación y síntesis → modelo;
- cálculo, validación, persistencia y transformación repetible → tool o código.

No uses código para ocultar una decisión metodológica que debería ser explícita. No uses razonamiento probabilístico del modelo para operaciones que deben ser deterministas.

## Contexto de empresa

Cuando en fases posteriores exista `company-context/`:

- valida su estado antes de usarlo;
- no conviertas inferencias en verdad de empresa;
- no sobrescribas hechos confirmados a partir de una sola fuente externa;
- conserva trazabilidad de cambios relevantes;
- no escribas secretos o credenciales en archivos versionados.

## Primera ejecución

Si falta contexto válido de empresa, inicia el onboarding cuando esa capacidad esté implementada.

Mientras no exista, explica qué información mínima falta y evita conclusiones definitivas sobre mercados, clientes, distribuidores o estrategia.

## Cambios en el repositorio

Antes de crear una nueva skill, workflow o tool:

1. comprueba si ya existe una capacidad equivalente;
2. lee la convención correspondiente en `docs/`;
3. define responsabilidad, contrato y criterios de calidad;
4. evita duplicación;
5. añade tests o criterios de validación cuando la fase correspondiente lo permita.

## Checklist antes de cerrar una tarea

- objetivo/decisión entendidos;
- contexto suficiente;
- evidencia proporcionada o identificada;
- hechos e hipótesis separados;
- riesgos y gaps visibles;
- recomendación proporcional a la confianza;
- siguiente acción clara;
- aprobación humana señalada cuando aplica.

## Idioma

Trabaja en español por defecto. Las fuentes y entregables de mercado pueden utilizar otros idiomas cuando la tarea de internacionalización lo requiera.
