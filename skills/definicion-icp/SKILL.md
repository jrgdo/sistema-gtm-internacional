---
name: definicion-icp
description: Define o revisa el perfil de cliente ideal para una oferta, aplicación y objetivo GTM concretos en industrial B2B. Úsala cuando la empresa no tenga claro qué tipos de cuentas priorizar, cuando el ICP existente sea demasiado genérico o cuando una nueva línea, aplicación o mercado requiera adaptar el perfil objetivo.
---

# Definición de ICP

## 1. Propósito

Construir un ICP operativo que ayude a decidir qué cuentas merecen atención y cuáles no, utilizando evidencia de fit comercial y técnico en lugar de descripciones amplias de sector.

## 2. Pregunta de decisión

> ¿Qué características debe tener una empresa para que merezca prioridad comercial para esta oferta, aplicación y objetivo?

## 3. Inputs requeridos

- oferta prioritaria;
- aplicación/problema relevante;
- objetivo GTM;
- evidencia disponible de clientes, oportunidades o uso;
- restricciones materiales.

Usar `contracts/entrada-componente.yaml`.

## 4. Método

### Paso 1 — Delimitar unidad de análisis

Definir producto/línea, aplicación, geografía si aplica y objetivo comercial.

### Paso 2 — Analizar evidencia disponible

Separar:

- clientes con fit demostrado;
- clientes rentables pero no necesariamente replicables;
- oportunidades prometedoras;
- segmentos históricos por inercia;
- hipótesis del equipo.

### Paso 3 — Definir criterios de fit

Considerar cuando sea relevante:

- sector/subsector;
- aplicación;
- proceso industrial;
- tamaño/capacidad;
- complejidad técnica;
- installed base o tecnología compatible;
- geografía;
- modelo de compra;
- necesidad de servicio;
- capacidad económica;
- señales de cambio/proyecto;
- compatibilidad de canal.

### Paso 4 — Definir disqualifiers

Ejemplos:

- aplicación incompatible;
- volumen insuficiente;
- requisito técnico no soportado;
- conflicto de canal;
- geografía sin cobertura;
- condiciones de compra inviables.

### Paso 5 — Distinguir firmographics de evidencia de necesidad

No asumir necesidad porque una empresa pertenece a un sector. El ICP define probabilidad de fit, no intención confirmada.

### Paso 6 — Definir niveles

Resultado recomendado:

- `ICP_NUCLEO`
- `ICP_ADYACENTE`
- `EXPLORATORIO`
- `FUERA_DE_ICP`

### Paso 7 — Definir señales de priorización

Crear señales observables que una futura investigación de cuenta pueda comprobar.

## 5. Reglas de decisión

Un ICP debe ser suficientemente específico para excluir cuentas.

Si prácticamente cualquier empresa del sector entra, el ICP es demasiado amplio.

No derivar el ICP únicamente de los mejores clientes actuales: pueden existir sesgos históricos, geográficos o de canal.

## 6. Evidencia

Usar `contracts/evidencia.yaml`.

Separar evidencia de fit técnico, fit comercial, acceso y resultados observados.

## 7. Salida

Usar `contracts/salida-componente.yaml`.

Debe incluir:

- ICP núcleo;
- ICP adyacente si procede;
- criterios de inclusión;
- disqualifiers;
- señales observables;
- unknowns;
- hipótesis que requieren validación;
- confianza;
- siguiente validación.

## 8. Handoffs

- contexto insuficiente → onboarding;
- evidencia insuficiente sobre readiness → diagnostico-internacional;
- ICP suficientemente definido + decisión de países → priorizacion-de-mercados;
- ICP definido + cuenta concreta → futura investigacion-de-cuentas.

## 9. Failure modes

- solo se dispone de sector → devolver perfil provisional con baja confianza;
- cliente histórico muy grande distorsiona la muestra → explicitar sesgo;
- varios productos tienen ICP distinto → separar perfiles;
- mercado exige canal distinto → no asumir mismo ICP económico/comprador.

## 10. Anti-patrones

- ICP = “empresas industriales medianas”;
- copiar personas de marketing B2C;
- confundir buyer persona con ICP;
- incluir intención de compra sin evidencia;
- definir ICP únicamente por facturación;
- no declarar disqualifiers.

## 11. Referencias

- `references/criterios-icp.md`
- `references/icp-vs-buying-roles.md`

## 12. Evaluación

- `tests/escenarios.md`
- `tests/criterios-de-evaluacion.md`
