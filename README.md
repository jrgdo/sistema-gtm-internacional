# Sistema GTM Internacional

Agente de IA personalizable para investigación, priorización y preparación comercial internacional B2B.

Pensado especialmente para empresas industriales españolas que empiezan a exportar, exportan de forma reactiva o quieren profesionalizar mercados, distribuidores y desarrollo comercial internacional.

> **La IA prepara. El equipo decide. El sistema conserva únicamente contexto y aprendizaje suficientemente validados.**

[![skills.sh](https://skills.sh/b/jrgdo/sistema-gtm-internacional)](https://skills.sh/jrgdo/sistema-gtm-internacional)

## Qué diferencia este repositorio de un pack de prompts

No parte de una instrucción genérica tipo “actúa como experto en exportación”. El sistema combina:

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
QUALITY GUARD
        ↓
DECISIÓN HUMANA
        ↓
MEMORIA VALIDADA
```

La arquitectura separa razonamiento probabilístico de operaciones deterministas, distingue evidencia de hipótesis y sabe cuándo debe detenerse o escalar.

## Instalación rápida

Con Agent Skills:

```bash
npx skills add jrgdo/sistema-gtm-internacional
```

Para instalar todas las skills en agentes compatibles detectados:

```bash
npx skills add jrgdo/sistema-gtm-internacional --all
```

Después:

```text
Configura el Sistema GTM Internacional para mi empresa.
Trabaja en español.
No inventes información que no esté confirmada.
```

Consulta [`EMPIEZA-AQUI.md`](EMPIEZA-AQUI.md) y [`docs/instalacion.md`](docs/instalacion.md).

## Repositorio completo

Si quieres estudiar, modificar o extender la arquitectura:

```bash
git clone https://github.com/jrgdo/sistema-gtm-internacional.git
cd sistema-gtm-internacional
```

La instalación por Skills distribuye las carpetas de skills. El clone completo incluye además agente, workflows, contracts, tools, QA, tests, templates y documentación de arquitectura.

## Capacidades

### Configuración y estrategia

- `sistema-gtm-internacional` — punto de entrada y orquestación instalable.
- `onboarding-empresa` — configura contexto de empresa sin rellenar huecos con IA.
- `diagnostico-internacional` — evalúa readiness para una ambición concreta.
- `definicion-icp` — define qué organizaciones merecen prioridad.
- `priorizacion-de-mercados` — compara atractivo, capacidad de ganar y fricción.

### Inteligencia comercial

- `investigacion-de-mercado` — investigación ligada a una decisión, no country reports genéricos.
- `evaluacion-de-distribuidores` — fit, acceso, capacidad, conflictos, prioridad y siguiente validación.
- `investigacion-de-cuentas` — account fit, señales, hipótesis y stakeholders probables.
- `preparacion-comercial` — briefing, discovery, riesgos y siguiente compromiso.

## Workflows incluidos

- configurar agente;
- diagnosticar expansión;
- comparar mercados;
- explorar nuevo mercado;
- evaluar distribuidor;
- investigar cuenta;
- preparar reunión.

Cada workflow declara precondiciones, gates, stops y handoffs.

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
- research no equivale a customer discovery;
- unknown no equivale automáticamente a cero;
- una buena web no demuestra acceso comercial de un distribuidor;
- un cargo no demuestra autoridad de compra;
- un ranking no sustituye decisión humana;
- claims, certificaciones, pricing, exclusividad y compromisos sensibles requieren governance;
- si la cuestión es fiscal, legal, regulatoria o de ingeniería crítica, el sistema prepara y escala: no finge autoridad profesional.

## Company Context Engine

El sistema crea un `company-context/` local para almacenar únicamente contexto operativo validado. `.gitignore` excluye esa carpeta por defecto para reducir el riesgo de publicar información interna.

La memoria se mantiene separada:

- decisiones;
- hipótesis;
- aprendizajes.

Una observación comercial no reescribe automáticamente la verdad de empresa.

## Código y validación

El repositorio incluye tools Python para:

- validar estructura de contexto;
- calcular scorecards transparentes;
- registrar decisiones;
- validar contratos.

GitHub Actions comprueba sintaxis y estructura base en cada push/PR.

## Qué NO pretende resolver la versión pública

No incluye por defecto una arquitectura empresarial completa para:

- CRM/ERP sync;
- monitoring continuo;
- enrichment masivo;
- triggers y queues;
- secrets management;
- retries y observabilidad;
- permisos empresariales;
- multi-agent orchestration avanzada;
- learning loops automáticos;
- automatización autónoma de comunicaciones externas.

Consulta [`docs/cuando-necesitas-automatizacion.md`](docs/cuando-necesitas-automatizacion.md) y [`docs/cuando-necesitas-personalizacion-profesional.md`](docs/cuando-necesitas-personalizacion-profesional.md).

## Madurez

El objetivo no es usar más agentes. Es mejorar la cadena:

> **contexto → decisión → ejecución → evidencia → aprendizaje**

Puedes usar el [`autodiagnóstico de madurez`](docs/autodiagnostico-de-madurez.md) para evaluar qué nivel necesitas.

## Ejemplo ficticio

`examples/empresa-industrial-ficticia/` muestra cómo aplicar el sistema sin utilizar datos ni resultados de clientes reales.

## Contribuir

Consulta [`CONTRIBUTING.md`](CONTRIBUTING.md). Las propuestas de nuevas skills deben explicar la decisión soportada, inputs, output, errores frecuentes y qué debe seguir siendo decisión humana.

Si el proyecto te resulta útil, una ⭐ ayuda a que otros equipos de exportación e industrial B2B lo encuentren.

## Idioma

La documentación pública se mantiene en español. El sistema puede investigar fuentes y producir materiales en otros idiomas cuando el mercado objetivo lo requiera.
