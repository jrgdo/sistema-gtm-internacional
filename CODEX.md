# Guía operativa para Codex

Codex debe tratar este repositorio como un sistema GTM estructurado, no como una colección de prompts.

`AGENTS.md` es la instrucción raíz del proyecto. Este archivo añade notas específicas de ejecución para Codex.

## Inicio obligatorio

Antes de realizar trabajo sustantivo:

1. lee `AGENTS.md`;
2. lee `ARCHITECTURE.md`;
3. lee `agents/agente-gtm-internacional/AGENT.md`;
4. carga únicamente la documentación relevante de `docs/`;
5. comprueba si existe `company-context/STATUS.md`;
6. si existe, léelo primero y determina qué dominios son necesarios para la decisión;
7. valida estado, frescura y conflictos de esos dominios;
8. si falta contexto esencial, ejecuta `skills/onboarding-empresa/SKILL.md`;
9. tras onboarding o validación de contexto, devuelve el control al Agente GTM Internacional;
10. selecciona el workflow y las skills mínimas necesarias cuando existan;
11. utiliza tools deterministas cuando exista una herramienta adecuada;
12. aplica las reglas de evidencia, aprobación y persistencia antes de cerrar la tarea.

## Agente GTM Internacional

`agents/agente-gtm-internacional/AGENT.md` es la capa de coordinación.

Debe decidir:

- qué decisión o entregable intenta preparar el usuario;
- qué contexto es material;
- qué componente usar;
- qué prerequisites deben cumplirse;
- cuándo avanzar, bloquear o escalar;
- cuándo solicitar validación humana.

Aplica siempre el principio de camino mínimo y consulta las referencias del agente sobre routing, estados, gates, handoffs y límites cuando sean relevantes.

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

## Primera ejecución y onboarding

Si falta contexto válido de empresa, no produzcas una estrategia genérica como sustituto.

Ejecuta `skills/onboarding-empresa/SKILL.md` y:

1. inspecciona primero archivos y documentos disponibles;
2. crea un mapa de cobertura;
3. detecta gaps, conflictos y posibles datos obsoletos;
4. pregunta solo lo necesario para el objetivo actual;
5. presenta el contexto candidato para validación;
6. crea o actualiza `company-context/` respetando las políticas de persistencia;
7. actualiza `STATUS.md` y declara readiness.

No reinicies onboarding si el contexto existente es suficiente para la decisión actual.

## Routing, gates y stops

Antes de ejecutar una capacidad downstream:

- comprueba prerequisites;
- no inventes inputs faltantes;
- permite `PASS_CON_LIMITES` cuando el gap no sea material;
- detente si existe conflicto, evidencia insuficiente o aprobación obligatoria;
- escala a expertise humano especializado cuando la cuestión material sea fiscal, legal, regulatoria, aduanera, financiera sensible o de ingeniería crítica.

Un stop correcto no es un error técnico.

## Cambios en el repositorio

Antes de crear una nueva skill, workflow o tool:

1. comprueba si ya existe una capacidad equivalente;
2. lee la convención correspondiente en `docs/`;
3. define responsabilidad, contrato y criterios de calidad;
4. evita duplicación;
5. añade tests o criterios de validación cuando la fase correspondiente lo permita.

Usa `skills/onboarding-empresa/` como referencia inicial de profundidad para skills y `agents/agente-gtm-internacional/` como referencia de calidad de orquestación, sin copiar mecánicamente lógica irrelevante.

## Checklist antes de cerrar una tarea

- objetivo/decisión entendidos;
- contexto suficiente, vigente y sin conflictos bloqueantes;
- camino mínimo aplicado;
- prerequisites y gates respetados;
- evidencia proporcionada o identificada;
- hechos e hipótesis separados;
- riesgos y gaps visibles;
- recomendación proporcional a la confianza;
- siguiente acción clara;
- aprobación humana o escalado especializado señalado cuando aplica;
- persistencia compatible con la política de contexto.

## Idioma

Trabaja en español por defecto. Las fuentes y entregables de mercado pueden utilizar otros idiomas cuando la tarea de internacionalización lo requiera.
