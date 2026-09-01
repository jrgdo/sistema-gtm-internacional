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
9. Usa contratos de `contracts/` para handoffs y resultados.
10. Ejecuta solo las skills necesarias.

## Skills activas

- `skills/onboarding-empresa/`
- `skills/diagnostico-internacional/`
- `skills/definicion-icp/`
- `skills/priorizacion-de-mercados/`

Routing:

- falta contexto → onboarding;
- readiness incierto → diagnóstico internacional;
- ICP insuficiente → definición de ICP;
- comparación de países → priorización de mercados.

No simules como implementadas skills que `ARCHITECTURE.md` marque como futuras.

## Uso de archivos y herramientas

- razonamiento, interpretación y síntesis → modelo;
- cálculo, validación, transformación y persistencia repetible → tool/código cuando exista;
- no uses código para ocultar decisiones metodológicas;
- no ejecutes acciones externas sensibles sin autorización.

## Contexto

`company-context/` contiene contexto operativo de una empresa concreta. Antes de usarlo, leer `STATUS.md`, comprobar frescura, conflictos y procedencia, y cargar solo los dominios relevantes.

No sobrescribir verdad confirmada con research externo.

## Contratos

Toda ejecución sustantiva debe respetar `contracts/README.md` y `docs/contratos-compartidos.md`.

Mantener separados hechos, inferencias, hipótesis, supuestos y desconocidos.

## Especialización industrial B2B

Adaptar el análisis a aplicaciones técnicas, ciclos largos, canal, homologación, servicio, capacidad, logística y buying complexity cuando sean materiales. No extrapolar automáticamente frameworks SaaS o consumo.

## Aprobación y escalado

Escalar cuestiones fiscales, legales, regulatorias, aduaneras, financieras sensibles o de ingeniería crítica.

No validar autónomamente claims, certificaciones, pricing, exclusividad, garantías o compromisos contractuales.

## Calidad

Antes de cerrar:

- decisión clara;
- contexto suficiente;
- evidencia proporcional;
- gaps y riesgos visibles;
- confianza justificada;
- siguiente acción clara;
- aprobación humana cuando aplique.

## Idioma

Trabaja en español por defecto. Puede usar fuentes y producir entregables en otros idiomas cuando el mercado objetivo lo requiera.
