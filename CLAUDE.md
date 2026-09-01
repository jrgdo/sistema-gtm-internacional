# Guía operativa para Claude Code

Claude Code debe tratar este repositorio como un sistema GTM estructurado, no como una colección de prompts.

## Inicio

1. Lee `AGENTS.md`.
2. Lee `ARCHITECTURE.md`.
3. Lee `agents/agente-gtm-internacional/AGENT.md`.
4. Comprueba `company-context/STATUS.md` si existe.
5. Si falta contexto material, ejecuta `onboarding-empresa`.
6. Identifica objetivo y decisión.
7. Aplica routing, gates y camino mínimo.
8. Usa contracts para handoffs cuando estén disponibles.
9. Ejecuta workflow/skills/tools necesarios.
10. Aplica Quality Guard antes de `LISTO_PARA_DECISION`.

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

## Contexto

`company-context/` es verdad operativa controlada. Leer `STATUS.md`, comprobar procedencia, frescura y conflictos, y no sobrescribirla con research externo.

## Uso de herramientas

- modelo → juicio, interpretación, investigación y síntesis;
- código/tool → cálculo, validación, transformación y persistencia repetible.

No uses razonamiento probabilístico para una operación que debe ser determinista.

## Reglas críticas

- research != customer discovery;
- señal != intención;
- cargo != autoridad;
- unknown != cero;
- web/portfolio != acceso real de distribuidor;
- fit de cuenta != necesidad confirmada;
- score != decisión.

## Aprobación y escalado

No validar autónomamente claims, certificaciones, suitability regulatoria, pricing, exclusividad, garantías, contratos ni compromisos externos sensibles.

Escalar fiscalidad, legal, regulación, aduanas, finanzas sensibles e ingeniería crítica.

## Memoria

No mezclar `company-context/` con decisiones, hipótesis o aprendizajes. Promover cambios a verdad de empresa solo mediante política de contexto y validación.

## Tests

Tras cambios de código/arquitectura, hacer best effort para ejecutar:

```bash
python -m py_compile tools/*.py tests/validar_sistema.py skills/sistema-gtm-internacional/scripts/inicializar_contexto.py
python tests/validar_sistema.py
```

## Idioma

Trabaja en español por defecto. Usa fuentes y materiales en otros idiomas cuando la decisión internacional lo requiera.
