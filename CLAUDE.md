# Guía operativa para Claude Code

Claude Code debe tratar este repositorio como un sistema GTM estructurado y evaluable, no como una colección de prompts.

`AGENTS.md` contiene las reglas canónicas. Este archivo añade únicamente instrucciones específicas de ejecución para Claude Code.

## Inicio obligatorio

1. Lee `AGENTS.md`.
2. Lee `ARCHITECTURE.md`.
3. Si trabajas con el repositorio completo, lee `agents/agente-gtm-internacional/AGENT.md`.
4. Comprueba `company-context/STATUS.md` si existe.
5. Identifica objetivo, decisión y contexto mínimo necesario.
6. Ejecuta únicamente el workflow, skills y tools que correspondan.
7. Aplica `qa/QUALITY-GUARD.md` antes de considerar un resultado listo para decisión.

No cargues todos los documentos del repositorio por defecto. Abre únicamente las referencias necesarias para la decisión actual.

## Primera ejecución

Si no existe contexto de empresa:

- usa `sistema-gtm-internacional` como punto de entrada cuando esté instalado mediante Agent Skills;
- usa `onboarding-empresa` para construir contexto validado;
- no rellenes huecos inventando estrategia, ICP, claims, aplicaciones o restricciones.

## Uso de herramientas

- modelo → juicio, investigación, interpretación y síntesis;
- código/tool → cálculo, validación, transformación y persistencia repetible.

No uses razonamiento probabilístico para operaciones que deben ser deterministas. Si existe una tool adecuada en `tools/`, úsala en vez de recalcular manualmente.

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

Antes de una acción difícil de revertir o que afecte sistemas externos, confirma que existe autorización suficiente.

## Cambios en el repositorio

Antes de añadir una capacidad nueva:

1. comprueba si ya existe;
2. lee la convención correspondiente en `docs/`;
3. define la decisión que soporta;
4. respeta `contracts/`;
5. añade escenarios o tests;
6. evita duplicar metodología entre agente, workflow y skill;
7. respeta la frontera pública.

## Validación

Después de cambios de código o arquitectura, haz best effort para ejecutar:

```bash
python -m py_compile tools/*.py tests/validar_sistema.py skills/sistema-gtm-internacional/scripts/inicializar_contexto.py
python tests/validar_sistema.py
```

No declares terminado un cambio con checks conocidos fallando sin explicarlo.

## Idioma

Trabaja en español por defecto. Usa fuentes y materiales en otros idiomas cuando la decisión internacional lo requiera.
