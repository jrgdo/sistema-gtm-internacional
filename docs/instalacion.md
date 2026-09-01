# Instalación

El Sistema GTM Internacional ofrece dos modos de uso.

## Opción A — instalación rápida con Agent Skills

Recomendada para usar las capacidades GTM desde un agente compatible sin clonar toda la arquitectura.

### Codex

```bash
npx skills add jrgdo/sistema-gtm-internacional --skill '*' --agent codex
```

### Claude Code

```bash
npx skills add jrgdo/sistema-gtm-internacional --skill '*' --agent claude-code
```

### Instalación interactiva

```bash
npx skills add jrgdo/sistema-gtm-internacional
```

El instalador permite elegir las skills y los agentes destino. Si quieres instalar todo en todos los agentes compatibles detectados puedes usar `--all`, pero no es la opción recomendada por defecto porque puede instalar capacidades donde no las necesitas.

Después, inicia con una petición como:

```text
Configura el Sistema GTM Internacional para mi empresa.
Trabaja en español.
No inventes información que no esté confirmada.
```

La skill `sistema-gtm-internacional` actúa como punto de entrada. Si no existe `company-context/`, puede utilizar `scripts/inicializar_contexto.py` para crear una estructura local vacía y continuar con `onboarding-empresa`.

### Alcance del modo Skills

La instalación mediante Agent Skills distribuye las carpetas de skills y sus archivos asociados. No instala necesariamente todos los archivos del repositorio raíz.

Por tanto, este modo incluye las capacidades especializadas y el routing básico del punto de entrada, pero **no equivale al repositorio completo** con agente raíz, workflows, contracts, tools, QA, tests y documentación de arquitectura.

## Opción B — repositorio completo

Recomendada para builders, consultores, equipos internos y evaluaciones técnicas que quieran estudiar, modificar o extender la arquitectura.

```bash
git clone https://github.com/jrgdo/sistema-gtm-internacional.git
cd sistema-gtm-internacional
```

En este modo están disponibles también:

- `AGENTS.md`, `CLAUDE.md` y `CODEX.md`;
- Agente GTM Internacional y routing completo;
- workflows;
- contracts;
- tools deterministas;
- Quality Guard;
- tests y GitHub Actions;
- templates, ejemplos y documentación.

## Actualizaciones

Si usas el CLI de Skills, revisa los cambios antes de actualizar una instalación que ya tenga contexto de empresa real. No sobrescribas `company-context/` ni memoria operativa sin validar el impacto.

## Seguridad

No versiones en un repositorio público:

- `company-context/` con datos internos;
- credenciales o tokens;
- contratos privados;
- datos personales innecesarios;
- exports de CRM sin sanitizar;
- pricing o condiciones comerciales confidenciales;
- documentos técnicos sujetos a restricciones de distribución.
