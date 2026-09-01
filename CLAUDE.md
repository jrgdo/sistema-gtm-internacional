# Guía operativa para Claude Code

Claude Code debe tratar este repositorio como un sistema GTM estructurado, no como una colección de prompts.

## Inicio obligatorio

1. Lee `AGENTS.md`.
2. Lee `ARCHITECTURE.md`.
3. Lee `agents/agente-gtm-internacional/AGENT.md`.
4. Lee `docs/contratos-compartidos.md`.
5. Comprueba `company-context/STATUS.md` si existe.
6. Valida contexto, frescura y conflictos.
7. Si falta contexto esencial, ejecuta `skills/onboarding-empresa/SKILL.md`.
8. Devuelve el control al Agente GTM Internacional.
9. Identifica objetivo y decisión.
10. Aplica routing, gates y camino mínimo.
11. Antes de invocar un componente, estructura semánticamente su entrada según `contracts/entrada-componente.yaml`.
12. Interpreta su resultado según `contracts/salida-componente.yaml`.
13. Usa `contracts/handoff.yaml` cuando transfieras trabajo entre componentes.
14. Aplica evidencia, confianza y approval.
15. Cierra según `contracts/cierre-ejecucion.yaml`.

## Contratos compartidos

Los YAML de `contracts/` son contratos internos. No es necesario mostrarlos literalmente al usuario.

No completes campos desconocidos con contenido plausible. Preserva siempre la separación entre hechos, inferencias, hipótesis, supuestos y desconocidos.

Una recomendación no equivale a una decisión aprobada.

La confianza debe seguir `contracts/confianza.yaml`: nunca aumentarla por la calidad de redacción del modelo.

## Company Context Engine

Las plantillas públicas viven en `templates/contexto-empresa/`; el contexto real de una implementación vive en `company-context/`.

Lee `STATUS.md` primero y carga solo los dominios relevantes. No sobrescribas información confirmada con research externo y no guardes secretos o credenciales.

## Primera ejecución

Si no existe contexto válido, ejecuta el onboarding adaptativo. Revisa primero documentación existente, detecta cobertura y gaps, pregunta solo lo necesario, valida y persiste únicamente información permitida.

## Uso de herramientas

- razonamiento, interpretación y síntesis → modelo;
- cálculos, schemas, validaciones, persistencia y transformaciones repetibles → código/tool cuando exista.

No ejecutes acciones externas sensibles sin autorización explícita.

## Especialización industrial B2B

Adapta el análisis a empresas industriales y exportadoras: aplicación técnica, canal, homologación, servicio, capacidad, logística, lead times, distribuidores, integradores, OEM y ciclos largos cuando sean materiales.

No importes mecánicamente playbooks SaaS o consumo.

## Idioma

Trabaja en español por defecto. Puedes investigar fuentes y producir entregables localizados en otros idiomas cuando el mercado lo requiera.
