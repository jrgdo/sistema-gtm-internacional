# Guía operativa para Codex

Codex debe tratar este repositorio como un sistema GTM estructurado y evaluable, no como una colección de prompts.

**`AGENTS.md` es la instrucción nativa y canónica del proyecto para Codex.** Este archivo no la sustituye: añade orientación específica de ejecución y sirve también como guía legible para quienes trabajan con Codex.

## Inicio obligatorio

1. Lee y respeta `AGENTS.md`.
2. Lee `ARCHITECTURE.md`.
3. Si trabajas con el repositorio completo, lee `agents/agente-gtm-internacional/AGENT.md`.
4. Comprueba `company-context/STATUS.md` si existe.
5. Identifica objetivo, decisión y contexto mínimo necesario.
6. Ejecuta únicamente el workflow, skills y tools que correspondan.
7. Usa `contracts/` para handoffs y outputs estructurados cuando aplique.
8. Aplica `qa/QUALITY-GUARD.md` antes de considerar un resultado listo para decisión.

No cargues todas las referencias del repositorio por defecto. Abre únicamente la documentación necesaria para la tarea y respeta cualquier `AGENTS.md` más específico que aparezca en una subcarpeta.

## Primera ejecución

Si no existe contexto de empresa:

- usa `sistema-gtm-internacional` como punto de entrada cuando esté instalado mediante Agent Skills;
- usa `onboarding-empresa` para construir contexto validado;
- no inventes estrategia, ICP, claims, aplicaciones, mercados prioritarios ni restricciones para completar archivos.

## Shell, archivos y tools

Cuando estén autorizados:

- modelo → juicio, investigación, interpretación y síntesis;
- código/tool → cálculo, validación, transformación y persistencia repetible.

No uses código para ocultar decisiones metodológicas ni razonamiento probabilístico para operaciones deterministas. Si existe una tool adecuada en `tools/`, úsala.

## Reglas que no debes degradar

- research != customer discovery;
- señal != intención;
- cargo != autoridad;
- unknown != cero;
- presencia online de partner != acceso comercial;
- fit de cuenta != necesidad confirmada;
- score != decisión;
- aprendizaje != causalidad.

## Acciones sensibles

No apruebes autónomamente claims, certificaciones, suitability regulatoria, pricing, descuentos, garantías, exclusividad, contratos ni comunicaciones externas sensibles.

Escala fiscalidad, legal, regulación, aduanas, finanzas sensibles e ingeniería crítica.

No realices operaciones destructivas, force-pushes ni cambios irreversibles salvo instrucción explícita y autoridad suficiente.

## Cambios en el repositorio

Antes de crear una capacidad nueva:

1. comprueba si ya existe;
2. lee la convención correspondiente en `docs/`;
3. define responsabilidad y decisión soportada;
4. respeta `contracts/`;
5. añade escenarios o tests;
6. evita duplicación entre agente, workflow, skill y tool;
7. respeta la frontera pública.

## Validación

Después de cambios de código o arquitectura, haz best effort para ejecutar:

```bash
python -m py_compile tools/*.py tests/validar_sistema.py skills/sistema-gtm-internacional/scripts/inicializar_contexto.py
python tests/validar_sistema.py
```

No cierres un cambio con checks conocidos fallando sin explicarlo.

## Idioma

Trabaja en español por defecto. Investiga y produce materiales localizados en otros idiomas cuando la decisión internacional lo requiera.
