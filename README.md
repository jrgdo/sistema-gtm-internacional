# Sistema GTM Internacional

Agente de IA personalizable para investigación, priorización y preparación comercial internacional B2B.

Pensado especialmente para empresas industriales españolas que empiezan a exportar, exportan de forma reactiva o quieren profesionalizar mercados, distribuidores y desarrollo comercial internacional.

> **La IA prepara. El equipo decide. El sistema conserva únicamente contexto y aprendizaje suficientemente validados.**

[![skills.sh](https://skills.sh/b/jrgdo/sistema-gtm-internacional)](https://skills.sh/jrgdo/sistema-gtm-internacional)

## Qué es

No es un pack de prompts ni una instrucción genérica de “actúa como experto en exportación”. Es una implementación de referencia para convertir trabajo GTM internacional en un sistema con contexto, decisiones, procesos, capacidades especializadas, operaciones deterministas y revisión humana.

```text
CONTEXTO DE EMPRESA
        ↓
AGENTE GTM INTERNACIONAL
        ↓
ROUTING + GATES + CONTRATOS
        ↓
WORKFLOWS
        ↓
SKILLS ESPECIALIZADAS
        ↓
TOOLS DETERMINISTAS
        ↓
CONTROL DE CALIDAD
        ↓
DECISIÓN HUMANA
        ↓
MEMORIA VALIDADA
```

La arquitectura separa razonamiento probabilístico de operaciones deterministas, distingue evidencia de hipótesis y sabe cuándo debe continuar, detenerse o escalar.

## Dos formas de usarlo

### 1. Modo Skills — instalación rápida

Recomendado si quieres utilizar las capacidades GTM desde un agente compatible sin clonar toda la arquitectura.

**Codex**

```bash
npx skills add jrgdo/sistema-gtm-internacional --skill '*' --agent codex
```

**Claude Code**

```bash
npx skills add jrgdo/sistema-gtm-internacional --skill '*' --agent claude-code
```

También puedes ejecutar el instalador interactivo:

```bash
npx skills add jrgdo/sistema-gtm-internacional
```

Después, inicia con una petición como:

```text
Configura el Sistema GTM Internacional para mi empresa.
Trabaja en español.
No inventes información que no esté confirmada.
```

La skill `sistema-gtm-internacional` actúa como punto de entrada y puede inicializar un `company-context/` local sin inventar datos.

> El modo Skills distribuye las skills y sus archivos asociados. No equivale a clonar toda la arquitectura del repositorio.

### 2. Repositorio completo — arquitectura de referencia

Recomendado si quieres estudiar, modificar, extender o evaluar el sistema completo:

```bash
git clone https://github.com/jrgdo/sistema-gtm-internacional.git
cd sistema-gtm-internacional
```

El repositorio completo incluye además:

- `AGENTS.md`, `CLAUDE.md` y `CODEX.md`;
- Agente GTM Internacional;
- workflows;
- contratos compartidos;
- tools Python;
- Quality Guard;
- tests y CI;
- templates;
- documentación de arquitectura y governance.

Consulta [`EMPIEZA-AQUI.md`](EMPIEZA-AQUI.md) y [`docs/instalacion.md`](docs/instalacion.md).

## Capacidades incluidas

### Configuración y estrategia

- `sistema-gtm-internacional` — punto de entrada instalable y routing básico.
- `onboarding-empresa` — configura contexto sin rellenar huecos con IA.
- `diagnostico-internacional` — evalúa preparación para una ambición concreta.
- `definicion-icp` — define qué organizaciones merecen prioridad.
- `priorizacion-de-mercados` — compara atractivo, capacidad de ganar y fricción.

### Inteligencia y preparación comercial

- `investigacion-de-mercado` — investigación ligada a una decisión, no country reports genéricos.
- `evaluacion-de-distribuidores` — fit, acceso, capacidad, conflictos, prioridad y siguiente validación.
- `investigacion-de-cuentas` — account fit, señales, hipótesis y stakeholders probables.
- `preparacion-comercial` — briefing, discovery, riesgos y siguiente compromiso.

## Workflows del repositorio completo

- configurar agente;
- diagnosticar expansión;
- comparar mercados;
- explorar nuevo mercado;
- evaluar distribuidor;
- investigar cuenta;
- preparar reunión.

Cada workflow declara precondiciones, gates, stops y handoffs. La metodología especializada permanece en las skills para evitar duplicación.

## Ejemplos de uso

```text
“¿Estamos preparados para entrar en Francia con esta línea?”
“Define el ICP para nuestra aplicación de proceso alimentario.”
“Compara Alemania, Francia y Polonia.”
“Investiga Francia para decidir si necesitamos canal.”
“Evalúa este distribuidor y dime qué falta validar.”
“Investiga esta cuenta sin asumir que necesita nuestro producto.”
“Prepara mi reunión y define el siguiente compromiso razonable.”
```

## Principios de calidad

- hechos, evidencia, inferencias, hipótesis, supuestos y desconocidos permanecen separados;
- investigación de escritorio no equivale a customer discovery;
- desconocido no equivale automáticamente a cero;
- una buena web no demuestra acceso comercial de un distribuidor;
- un cargo no demuestra autoridad de compra;
- un ranking no sustituye una decisión humana;
- claims, certificaciones, pricing, exclusividad y compromisos sensibles requieren governance;
- si la cuestión es fiscal, legal, regulatoria o de ingeniería crítica, el sistema prepara y escala: no finge autoridad profesional.

## Company Context Engine

El sistema utiliza `company-context/` para almacenar contexto operativo validado de una empresa concreta. En el repositorio completo, `.gitignore` excluye esta carpeta por defecto para reducir el riesgo de publicar información interna.

La memoria se mantiene separada en tres categorías conceptuales:

- decisiones;
- hipótesis;
- aprendizajes.

Una observación comercial no reescribe automáticamente la verdad de empresa.

## Código, tests y CI

El repositorio completo incluye tools Python para:

- validar estructura de contexto;
- calcular scorecards transparentes;
- registrar decisiones;
- validar contratos.

GitHub Actions comprueba sintaxis y estructura base en cada push/PR. Las reglas del Quality Guard añaden controles sobre evidencia, desconocidos, confianza, claims y aprobaciones.

## Qué NO pretende resolver la versión pública

No incluye por defecto una arquitectura empresarial completa para:

- sincronización CRM/ERP;
- monitorización continua;
- enriquecimiento masivo de datos;
- triggers, colas y retries de producción;
- gestión empresarial de secretos;
- permisos y observabilidad de producción;
- orquestación multiagente avanzada;
- learning loops automáticos;
- automatización autónoma de comunicaciones externas.

Consulta [`docs/cuando-necesitas-automatizacion.md`](docs/cuando-necesitas-automatizacion.md) y [`docs/cuando-necesitas-personalizacion-profesional.md`](docs/cuando-necesitas-personalizacion-profesional.md).

## Madurez

El objetivo no es usar más agentes. Es mejorar la cadena:

> **contexto → decisión → ejecución → evidencia → aprendizaje**

Puedes usar el [`autodiagnóstico de madurez`](docs/autodiagnostico-de-madurez.md) para evaluar qué nivel necesitas.

## Ejemplo ficticio

`examples/empresa-industrial-ficticia/` muestra cómo aplicar el sistema sin utilizar datos ni resultados de clientes reales.

## Para builders y contribuidores

Empieza por:

1. `AGENTS.md` — mapa operativo canónico.
2. `ARCHITECTURE.md` — arquitectura y fronteras.
3. `agents/agente-gtm-internacional/AGENT.md` — lógica de coordinación.
4. `docs/convenciones-de-skills.md`, `docs/convenciones-de-workflows.md` y `docs/convenciones-de-tools.md` — reglas de extensión.

Consulta también [`CONTRIBUTING.md`](CONTRIBUTING.md).

Si el proyecto te resulta útil, una ⭐ ayuda a que otros equipos de exportación e industrial B2B lo encuentren.

## Estado de release

La arquitectura pública está implementada y validada por CI. Antes de etiquetar una versión estable conviene completar una prueba limpia end-to-end en Codex y Claude Code y seleccionar una licencia pública explícita.

## Idioma

La documentación pública se mantiene en español. El sistema puede investigar fuentes y producir materiales en otros idiomas cuando el mercado objetivo lo requiera.
