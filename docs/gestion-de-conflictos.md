# Gestión de conflictos de contexto

## 1. Propósito

Un sistema serio no debe resolver silenciosamente contradicciones entre fuentes. Debe detectarlas, registrar su impacto y escalar cuando afecten a una decisión.

## 2. Qué es un conflicto

Existe conflicto cuando dos o más fuentes relevantes sostienen versiones incompatibles de un dato material.

Ejemplos:

- estrategia anual prioriza Alemania, pero dirección comercial declara Francia como prioridad actual;
- catálogo indica una aplicación permitida y documentación técnica posterior la limita;
- un distribuidor figura como exclusivo en un documento y como no exclusivo en otro;
- una claim aparece en marketing pero no está validada por el área técnica.

## 3. Proceso obligatorio

Ante un conflicto:

1. no elegir una versión por conveniencia;
2. identificar exactamente qué dato está en conflicto;
3. registrar fuentes, fechas y responsables;
4. evaluar cuál tiene mayor autoridad y frescura;
5. determinar el impacto sobre la decisión actual;
6. marcar el dominio como `CONFLICTO` cuando sea material;
7. solicitar validación del rol adecuado;
8. documentar la resolución antes de promover una versión a contexto confirmado.

## 4. Formato mínimo de registro

```text
ID: CONFLICTO-XXX
Tema:
Fuente A:
Fecha A:
Fuente B:
Fecha B:
Impacto:
Hipótesis de resolución:
Decisor requerido:
Estado: ABIERTO | RESUELTO
Resolución:
Fecha de resolución:
```

## 5. Autoridad no significa verdad automática

Una fuente jerárquicamente superior no debe ganar siempre de forma automática. Una política antigua puede estar formalmente aprobada pero haber quedado sustituida por una decisión reciente todavía no documentada.

El agente debe hacer visible esta tensión y pedir confirmación cuando el impacto sea material.

## 6. Conflictos que bloquean

Bloquear o degradar la recomendación cuando el conflicto afecte a:

- seguridad o aptitud técnica;
- certificación/regulación;
- pricing o condiciones;
- exclusividad;
- capacidad/lead time;
- estrategia de entrada;
- mercado/segmento prioritario;
- claim externo;
- responsabilidades de aprobación.

## 7. Conflictos menores

Diferencias de redacción, estilo o detalle que no cambian la decisión pueden resolverse sin bloquear, pero no deben alterar hechos materiales.

## 8. Principio

**Una contradicción visible es preferible a una falsa coherencia creada por el modelo.**
