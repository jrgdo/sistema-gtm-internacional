# Modelo de aprobación humana

## Objetivo

Definir cuándo el sistema puede preparar trabajo de forma autónoma y cuándo debe detenerse para solicitar validación humana.

## Principio

La IA puede investigar, estructurar, comparar, resumir, calcular y preparar recomendaciones. No debe convertir decisiones sensibles en acciones externas definitivas sin la aprobación adecuada.

## Categorías de riesgo

### Bajo riesgo
Puede ejecutarse y presentarse como borrador o análisis:

- estructurar información;
- preparar preguntas;
- comparar mercados con criterios transparentes;
- ordenar distribuidores para investigación;
- resumir documentación;
- identificar gaps;
- preparar briefing interno.

### Riesgo medio
Puede prepararse, pero requiere revisión antes de utilizarse externamente:

- mensajes comerciales;
- posicionamiento;
- claims de diferenciación;
- recomendaciones de canal;
- shortlist de partners;
- materiales localizados;
- propuestas de acciones comerciales.

### Alto riesgo
Requiere validación humana explícita antes de tratarse como definitivo o ejecutarse:

- certificaciones;
- cumplimiento regulatorio;
- seguridad;
- aptitud técnica para una aplicación;
- pricing y descuentos;
- garantías;
- exclusividad;
- territorio contractual;
- condiciones de pago;
- capacidad productiva o fechas de entrega;
- declaraciones de ROI;
- resultados de clientes;
- compromisos contractuales;
- decisiones de inversión relevantes;
- comunicaciones enviadas en nombre de la empresa.

## Estados de aprobación propuestos

En fases posteriores se podrán formalizar estados como:

- `BORRADOR`;
- `LISTO_PARA_REVISION`;
- `REQUIERE_VALIDACION`;
- `APROBADO`;
- `APROBADO_CON_CONDICIONES`;
- `RECHAZADO`;
- `NO_SOPORTADO`.

## Regla de no simulación

El sistema nunca debe afirmar que algo fue:

- enviado;
- publicado;
- aprobado;
- desplegado;
- actualizado en CRM;
- comunicado a un partner;

si no existe confirmación verificable de la acción.

## Aprobación y empresa

Las reglas genéricas de este repositorio son un mínimo. Una implementación personalizada puede exigir aprobaciones adicionales según:

- sector;
- riesgo técnico;
- normativa;
- estructura comercial;
- políticas internas;
- mercados objetivo.

## Principio de diseño

**La aprobación humana debe situarse en el punto donde cambia el riesgo, no simplemente al final del proceso.**
