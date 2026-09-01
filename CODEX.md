# Guía operativa para Codex

`AGENTS.md` es la instrucción raíz del proyecto. Codex debe tratar este repositorio como un sistema GTM estructurado y evaluable, no como una colección de prompts.

## Inicio

1. Lee `AGENTS.md`.
2. Lee `ARCHITECTURE.md`.
3. Lee `agents/agente-gtm-internacional/AGENT.md`.
4. Comprueba `company-context/STATUS.md` si existe.
5. Si falta contexto material, ejecuta `onboarding-empresa`.
6. Identifica objetivo y decisión.
7. Aplica routing, gates y camino mínimo.
8. Usa contracts para handoffs y resultados.
9. Ejecuta workflow/skills/tools necesarios.
10. Aplica `qa/QUALITY-GUARD.md` antes de `LISTO_PARA_DECISION`.

## Skills activas

- `sistema-gtm-internacional`
- `onboarding-empresa`
- `diagnostico-internacional`
- `definicion-icp`
- `priorizacion-de-mercados`
- `investigacion-de-mercado`
- `evaluacion-de-distribuidores`
- `investigacion-de-cuentas`
- `preparacion-comercial`

## Archivos, shell y tools

Cuando estén autorizados:

- modelo → juicio, investigación, interpretación y síntesis;
- código/tool → cálculo, schema validation, transformación y persistencia repetible.

No uses código para ocultar decisiones metodológicas ni razonamiento probabilístico para operaciones deterministas.

## Contexto

`company-context/STATUS.md` es el punto de entrada obligatorio al contexto real de empresa. Comprobar procedencia, estado, frescura y conflictos antes de usar o modificar información.

`.gitignore` excluye `company-context/` por defecto. No anules esta protección sin una razón explícita y segura.

## Contratos

Todo componente nuevo debe ser compatible con `contracts/` y mantener separados hechos, evidencia, inferencias, hipótesis, supuestos y desconocidos.

## Reglas críticas

- research != customer discovery;
- señal != intención;
- cargo != autoridad;
- unknown != cero;
- fit de cuenta != necesidad;
- presencia online de partner != acceso comercial;
- score != decisión;
- aprendizaje != causalidad.

## Aprobación y escalado

No validar autónomamente claims, certificaciones, suitability regulatoria, pricing, descuentos, garantías, exclusividad, contratos ni comunicaciones externas sensibles.

Escalar fiscalidad, legal, regulación, aduanas, finanzas sensibles o ingeniería crítica.

## Cambios en el repositorio

Antes de crear una nueva capacidad:

1. comprueba si ya existe;
2. lee la convención correspondiente;
3. define responsabilidad y decisión soportada;
4. usa contratos compartidos;
5. añade escenarios/tests;
6. evita duplicación;
7. respeta la frontera pública.

## Tests

Después de cambios de código/arquitectura, hacer best effort para ejecutar:

```bash
python -m py_compile tools/*.py tests/validar_sistema.py skills/sistema-gtm-internacional/scripts/inicializar_contexto.py
python tests/validar_sistema.py
```

No cierres un cambio con checks conocidos fallando sin explicarlo.

## Idioma

Trabaja en español por defecto. Puede investigar y producir materiales localizados en otros idiomas cuando la decisión lo requiera.
