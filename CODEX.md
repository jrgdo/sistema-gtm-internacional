# Guía operativa para Codex

Codex debe tratar este repositorio como un sistema GTM estructurado, no como una colección de prompts.

`AGENTS.md` es la instrucción raíz del proyecto.

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
12. Interpreta la salida según `contracts/salida-componente.yaml`.
13. Usa `contracts/handoff.yaml` para transferencias relevantes.
14. Aplica `contracts/evidencia.yaml`, `contracts/confianza.yaml` y approvals.
15. Cierra según `contracts/cierre-ejecucion.yaml`.

## Contratos compartidos

Los YAML de `contracts/` definen interoperabilidad interna. No deben convertirse en ruido visible para el usuario.

No rellenes campos desconocidos con inferencias. Mantén separados hechos, inferencias, hipótesis, supuestos y desconocidos.

No confundas estados de sistema, estados de contexto y resultados propios de skills.

Una recomendación no equivale a una decisión aprobada.

## Uso de archivos, shell y tools

Cuando estén autorizados:

- juicio, interpretación y síntesis → modelo;
- cálculo, validación, persistencia y transformación repetible → tool o código.

No uses código para ocultar decisiones metodológicas. No uses razonamiento probabilístico para operaciones que deben ser deterministas.

## Company Context Engine

El contexto real vive en `company-context/`. Lee `STATUS.md` primero, carga solo dominios relevantes y aplica políticas de escritura, frescura y conflictos antes de modificar información.

No guardes secretos, tokens o credenciales.

## Creación de nuevos componentes

Toda nueva skill debe consumir conceptualmente `contracts/entrada-componente.yaml` y producir `contracts/salida-componente.yaml`.

Todo workflow debe preservar los handoffs relevantes mediante `contracts/handoff.yaml`.

Toda tool futura deberá declarar qué campos recibe y devuelve.

## Especialización industrial B2B

Adapta el trabajo a empresas industriales y exportadoras. Considera aplicación, canal, capacidad técnica, homologación, posventa, logística, distribuidores, integradores y ciclos largos cuando sean relevantes.

## Idioma

Trabaja en español por defecto. Las fuentes o entregables pueden utilizar otros idiomas cuando el mercado objetivo lo requiera.
