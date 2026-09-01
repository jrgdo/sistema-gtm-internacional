# Empieza aquí

Este repositorio contiene un sistema GTM asistido por IA para empresas B2B, especialmente industriales, que están empezando a exportar o quieren profesionalizar su crecimiento internacional.

## Si solo quieres usarlo

Instala todas las skills en el agente que vayas a utilizar.

### Codex

```bash
npx skills add jrgdo/sistema-gtm-internacional --skill '*' --agent codex
```

### Claude Code

```bash
npx skills add jrgdo/sistema-gtm-internacional --skill '*' --agent claude-code
```

También puedes usar la instalación interactiva:

```bash
npx skills add jrgdo/sistema-gtm-internacional
```

Después escribe:

```text
Configura el Sistema GTM Internacional para mi empresa.
Trabaja en español.
No inventes datos. Pregunta solo lo que sea material para el objetivo actual.
```

Aporta documentación cuando ayude: catálogo, presentación comercial, estrategia, mercados actuales, ICP, brand guide, políticas de canal o documentación técnica autorizada.

El sistema debe revisar primero lo disponible, detectar gaps y pedir únicamente la información que pueda cambiar la decisión actual. Valida el contexto candidato antes de tratarlo como verdad de empresa.

> El modo Skills instala las capacidades especializadas. Si quieres trabajar con la arquitectura completa —agente raíz, workflows, tools, contracts, QA y tests— utiliza el repositorio completo.

## Si quieres estudiar o modificar la arquitectura

Clona el repositorio y empieza por:

1. `AGENTS.md` — mapa operativo canónico.
2. `ARCHITECTURE.md` — arquitectura y fronteras.
3. `agents/agente-gtm-internacional/AGENT.md` — coordinación y routing.
4. `contracts/` — lenguaje común entre componentes.
5. `workflows/` — procesos completos.
6. `skills/` — metodología especializada.
7. `tools/` — operaciones deterministas.
8. `qa/QUALITY-GUARD.md` — controles de calidad.
9. `ROADMAP.md` — evolución y estado del sistema.

## Qué puedes pedir

- “Diagnostica si estamos preparados para entrar en Francia con esta línea.”
- “Ayúdame a definir el ICP para esta aplicación.”
- “Compara Alemania, Francia y Polonia para decidir dónde investigar primero.”
- “Investiga Francia para decidir si necesitamos canal.”
- “Evalúa este distribuidor y dime qué falta demostrar.”
- “Investiga esta cuenta sin asumir que necesita nuestro producto.”
- “Prepara mi reunión con este partner y define el siguiente compromiso razonable.”

## Regla central

**No empieces por generar. Empieza por comprender el contexto, identificar la decisión y seleccionar el proceso adecuado.**
