# Guía operativa para Claude Code

Claude Code debe tratar este repositorio como un sistema GTM estructurado, no como una colección de prompts.

## Inicio obligatorio

1. Lee `AGENTS.md`.
2. Lee `ARCHITECTURE.md`.
3. Lee `agents/agente-gtm-internacional/AGENT.md`.
4. Comprueba `company-context/STATUS.md` si existe.
5. Si falta contexto material, ejecuta `skills/onboarding-empresa/SKILL.md`.
6. Devuelve el control al Agente GTM Internacional.
7. Identifica objetivo y decisión.
8. Aplica routing, gates y camino mínimo.
9. Usa contratos de `contracts/`.
10. Ejecuta solo las skills necesarias.

## Skills activas

- `skills/onboarding-empresa/`
- `skills/diagnostico-internacional/`
- `skills/definicion-icp/`
- `skills/priorizacion-de-mercados/`
- `skills/investigacion-de-mercado/`
- `skills/evaluacion-de-distribuidores/`

Routing principal:

- falta contexto → onboarding;
- readiness incierto → diagnóstico;
- ICP insuficiente → definición de ICP;
- comparación de países → priorización;
- evidencia detallada de mercado → investigación de mercado;
- evaluación de partner identificado → evaluación de distribuidores.

No simules como implementadas skills futuras.

## Research

No producir country reports genéricos cuando la decisión requiera evidence gathering acotado.

Desk research no equivale a market validation. Separar hechos, señales, inferencias, hipótesis y unknowns. No inferir buyer need o demanda desde señales débiles.

## Distribuidores

No confundir presencia web, tamaño, portfolio o antigüedad con acceso real, capacidad técnica o prioridad futura.

Distinguir pre-evaluación de qualification. No recomendar exclusividad ni condiciones sensibles sin aprobación humana.

## Contexto y contratos

`company-context/STATUS.md` es el punto de entrada al contexto.

Toda ejecución sustantiva debe respetar `contracts/README.md` y `docs/contratos-compartidos.md`.

No sobrescribir verdad confirmada con research externo.

## Herramientas

- modelo → razonamiento, interpretación y síntesis;
- código/tool → cálculo, validación, transformación y persistencia repetible.

No ejecutar acciones externas sensibles sin autorización.

## Especialización industrial B2B

Adaptar análisis a aplicaciones técnicas, ciclos largos, canal, homologación, servicio, capacidad, logística y buying complexity cuando sean materiales.

## Aprobación y escalado

Escalar cuestiones fiscales, legales, regulatorias, aduaneras, financieras sensibles o de ingeniería crítica.

No validar autónomamente claims, certificaciones, pricing, exclusividad, garantías o compromisos contractuales.

## Idioma

Trabaja en español por defecto. Puede investigar fuentes locales y producir entregables en otros idiomas cuando el mercado lo requiera.
