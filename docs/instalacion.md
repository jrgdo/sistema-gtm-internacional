# Instalación

El Sistema GTM Internacional ofrece dos modos de uso.

## Opción A — instalación rápida con Agent Skills

Recomendada para usar las capacidades con agentes compatibles sin clonar toda la arquitectura.

```bash
npx skills add jrgdo/sistema-gtm-internacional
```

El CLI permite seleccionar las skills y agentes destino. Para instalar todas las skills detectadas en los agentes compatibles instalados:

```bash
npx skills add jrgdo/sistema-gtm-internacional --all
```

Después, inicia con una petición como:

```text
Configura el Sistema GTM Internacional para mi empresa.
Trabaja en español.
No inventes información que no esté confirmada.
```

La skill `sistema-gtm-internacional` actúa como punto de entrada. Si no existe `company-context/`, puede utilizar su script `scripts/inicializar_contexto.py` para crear la estructura local y continuar con `onboarding-empresa`.

### Importante

La instalación con Agent Skills instala las carpetas de skills, no necesariamente todos los archivos de arquitectura del repositorio raíz. Por eso el punto de entrada y bootstrap viven dentro de `skills/sistema-gtm-internacional/`.

## Opción B — repositorio completo

Recomendada para builders, consultores y equipos que quieran estudiar, modificar o extender workflows, tools, contratos y tests.

```bash
git clone https://github.com/jrgdo/sistema-gtm-internacional.git
cd sistema-gtm-internacional
```

En este modo están disponibles también:

- `AGENTS.md`, `CLAUDE.md` y `CODEX.md`;
- agente y routing completo;
- workflows;
- contracts;
- tools deterministas;
- QA y tests;
- documentación y ejemplos.

## Actualizaciones

Si usas el CLI de Skills, consulta las capacidades de actualización del propio CLI antes de actualizar una instalación existente. Revisa cambios relevantes antes de aplicarlos en un entorno con contexto de empresa real.

## Seguridad

No versionar en un repositorio público:

- `company-context/` con datos sensibles;
- credenciales;
- tokens;
- contratos privados;
- datos personales innecesarios;
- exports de CRM sin sanitizar.
