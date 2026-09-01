# Guía operativa para Codex

Codex debe tratar este repositorio como un sistema GTM estructurado, no como una colección de prompts.

`AGENTS.md` es la instrucción raíz del proyecto.

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

Desk research no equivale a market validation. Mantener separados hechos, señales, inferencias, hipótesis y unknowns. No inferir necesidad de compra ni demanda accesible desde señales débiles.

## Distribuidores

No usar tamaño, presencia web, portfolio o antigüedad como sustitutos de acceso real, capacidad técnica, cobertura o prioridad futura.

Distinguir discovery, pre-evaluación y qualification. No recomendar exclusividad ni condiciones contractuales sensibles sin validación humana.

## Archivos, shell y tools

Cuando estén autorizados:

- modelo → juicio, síntesis e interpretación;
- código/tool → cálculo, schema validation, transformación y persistencia repetible.

No uses razonamiento probabilístico para operaciones deterministas ni código para ocultar decisiones metodológicas.

## Company Context Engine

`company-context/STATUS.md` es el punto de entrada obligatorio al contexto. Comprobar procedencia, estado, frescura y conflictos antes de utilizar o modificar información.

No convertir research externo o inferencias en verdad interna.

## Contratos

Todo componente debe ser compatible con `contracts/`. Los contratos son semántica interna; no es necesario exponer YAML al usuario.

## Especialización industrial B2B

Considerar cuando corresponda aplicaciones técnicas, ciclos largos, canal, homologación, servicio, logística, capacidad y complejidad de compra.

## Aprobación y escalado

No validar autónomamente claims, certificaciones, suitability regulatoria, pricing, exclusividad, garantías ni compromisos contractuales.

Escalar cuestiones fiscales, legales, regulatorias, aduaneras, financieras sensibles o de ingeniería crítica.

## Cambios en el repositorio

Antes de crear una nueva capacidad:

1. comprueba si ya existe;
2. lee la convención correspondiente;
3. usa contratos compartidos;
4. define responsabilidad y tests;
5. evita duplicación;
6. respeta la frontera pública.

## Idioma

Trabaja en español por defecto. Puede investigar fuentes locales y producir materiales localizados en otros idiomas cuando la decisión internacional lo requiera.
