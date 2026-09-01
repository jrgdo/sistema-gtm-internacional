---
name: onboarding-empresa
description: Configura o actualiza el contexto de una empresa para que el Sistema GTM Internacional pueda trabajar con información validada sobre negocio, oferta, aplicaciones, clientes, mercados, estrategia, objetivos, canales, restricciones, aprobaciones, claims, marca y terminología. Úsala cuando no exista company-context, el contexto sea insuficiente, esté obsoleto o el usuario quiera personalizar el agente para su empresa.
---

# Onboarding de empresa

## 1. Propósito

Convertir información dispersa de una empresa en un contexto GTM estructurado, trazable y suficientemente fiable para soportar decisiones posteriores de internacionalización y desarrollo comercial.

Esta skill no crea estrategia por defecto. Primero comprende y documenta la realidad, prioridades y límites de la empresa.

## 2. Cuándo usarla

Usar cuando ocurra cualquiera de estas condiciones:

- no existe `company-context/`;
- falta `company-context/STATUS.md`;
- `STATUS.md` indica `SIN_CONFIGURAR`, `PARCIAL`, `OBSOLETO` o `CONFLICTO` en dominios necesarios;
- el usuario pide configurar, personalizar o actualizar el agente para su empresa;
- ha cambiado materialmente la oferta, estrategia, mercados, canal, branding o governance;
- otra skill declara contexto insuficiente y enruta al onboarding.

## 3. Cuándo no usarla

No usar para:

- investigar mercados externos;
- definir automáticamente la estrategia internacional;
- seleccionar países;
- evaluar distribuidores;
- hacer investigación de cuentas;
- redactar campañas;
- guardar indiscriminadamente toda la información disponible.

Si el contexto ya es suficiente para la decisión actual, no rehacer onboarding completo.

## 4. Decisión que soporta

La pregunta que responde esta skill es:

> ¿Existe contexto de empresa suficiente, vigente y validado para que el sistema pueda ejecutar correctamente la siguiente decisión GTM?

Resultados posibles:

- `CONTEXTO_VALIDADO_PARA_OBJETIVO`
- `CONTEXTO_PARCIAL_UTILIZABLE`
- `REQUIERE_VALIDACION`
- `CONFLICTO_MATERIAL`
- `INPUT_INSUFICIENTE`

## 5. Inputs requeridos

Mínimo uno de los siguientes:

- información explícita proporcionada por un responsable;
- documentos de empresa;
- acceso autorizado a archivos de empresa;
- contexto existente en `company-context/`.

Para considerar el onboarding suficientemente operativo deben poder comprenderse, como mínimo cuando sean relevantes para el objetivo:

- empresa y modelo de negocio;
- oferta prioritaria;
- aplicaciones o problemas que resuelve;
- cliente/ICP actual o candidato;
- mercados actuales;
- objetivo GTM actual;
- forma de venta/canales;
- restricciones materiales.

## 6. Inputs opcionales

- web corporativa;
- catálogos y fichas técnicas;
- presentaciones comerciales;
- estrategia o plan export;
- CRM exports o resúmenes;
- organigrama comercial;
- brand guide;
- emails y materiales aprobados;
- lista de clientes o referencias autorizadas;
- políticas de pricing, canal o aprobación;
- documentación sobre certificaciones y claims.

## 7. Dependencias

Leer antes de ejecutar:

- `AGENTS.md`
- `docs/modelo-de-contexto.md`
- `docs/politica-de-escritura-de-contexto.md`
- `docs/politica-de-frescura.md`
- `docs/gestion-de-conflictos.md`
- `docs/modelo-de-aprobacion.md`

Usar las plantillas de `templates/contexto-empresa/` como modelo canónico.

## 8. Requisitos de evidencia

No exigir documentación perfecta para iniciar onboarding, pero cada dato debe conservar una relación clara con su procedencia.

Clasificar conceptualmente la información como:

- `CONFIRMADO`
- `INFERIDO`
- `HIPOTESIS`
- `PENDIENTE_DE_VALIDAR`
- `OBSOLETO`
- `CONFLICTO`

Solo información suficientemente respaldada puede incorporarse como verdad confirmada de empresa.

## 9. Método paso a paso

### Paso 1 — Detectar estado inicial

Comprobar si existe `company-context/` y `STATUS.md`.

- Si no existen, preparar una nueva configuración desde las plantillas.
- Si existen, leer primero `STATUS.md` y limitar el trabajo a dominios relevantes o problemáticos.

### Paso 2 — Definir el objetivo de onboarding

Determinar si se trata de:

- onboarding completo;
- onboarding mínimo para una decisión concreta;
- actualización de contexto;
- resolución de conflicto;
- revisión de frescura.

No recopilar información sin finalidad.

### Paso 3 — Inspeccionar evidencia disponible antes de preguntar

Si el usuario ha aportado documentos o archivos autorizados:

1. inventariar qué fuentes existen;
2. identificar qué dominios puede cubrir cada fuente;
3. extraer únicamente afirmaciones soportadas;
4. detectar contradicciones, antigüedad y gaps;
5. evitar preguntar al usuario información ya disponible de forma fiable.

Seguir `references/extraccion-de-documentos.md`.

### Paso 4 — Construir mapa de cobertura

Para cada dominio relevante marcar:

- suficiente;
- parcial;
- ausente;
- obsoleto;
- conflictivo.

Priorizar gaps que bloquean la decisión actual.

### Paso 5 — Hacer preguntas adaptativas

Preguntar por bloques cortos y de alto valor.

No presentar un formulario masivo salvo que el usuario lo solicite.

Orden recomendado:

1. empresa y oferta;
2. objetivo actual;
3. clientes, aplicaciones y mercados;
4. ventas y canales;
5. estrategia y restricciones;
6. governance, claims y marca cuando sean necesarios.

Seguir `references/preguntas-onboarding.md`.

### Paso 6 — Detectar conflictos

Si dos fuentes relevantes discrepan:

- no elegir silenciosamente;
- registrar el conflicto;
- identificar cuál es la decisión afectada;
- valorar autoridad y frescura;
- pedir validación cuando el conflicto sea material.

### Paso 7 — Preparar contexto candidato

Crear o actualizar únicamente los dominios soportados.

No completar campos con contenido plausible generado por IA.

Distinguir claramente información pendiente de validación.

### Paso 8 — Validación humana

Antes de declarar `CONTEXTO_VALIDADO_PARA_OBJETIVO`, presentar un resumen de:

- hechos principales incorporados;
- inferencias o elementos pendientes;
- conflictos;
- gaps materiales;
- restricciones relevantes;
- objetivo que el contexto permite soportar.

Solicitar corrección o confirmación de los elementos materiales.

### Paso 9 — Escribir contexto

Tras validación suficiente:

- crear/actualizar `company-context/`;
- preservar la estructura de las plantillas;
- actualizar `STATUS.md`;
- registrar fecha y procedencia cuando sea material;
- no guardar secretos, credenciales ni datos personales innecesarios.

### Paso 10 — Declarar readiness y handoff

Indicar qué tipos de trabajo GTM ya pueden ejecutarse y qué sigue bloqueado.

No asumir que onboarding completo equivale a estrategia correcta.

## 10. Reglas de decisión

### `CONTEXTO_VALIDADO_PARA_OBJETIVO`

Usar cuando los dominios críticos para el objetivo están suficientemente confirmados, vigentes y sin conflictos materiales no resueltos.

### `CONTEXTO_PARCIAL_UTILIZABLE`

Usar cuando faltan elementos no críticos y el trabajo puede continuar con límites explícitos.

### `REQUIERE_VALIDACION`

Usar cuando existe información candidata relevante que no debe tratarse todavía como verdad.

### `CONFLICTO_MATERIAL`

Usar cuando dos fuentes relevantes alteran de forma sustancial una futura decisión.

### `INPUT_INSUFICIENTE`

Usar cuando ni los documentos ni el usuario permiten comprender el mínimo necesario para el objetivo.

## 11. Contrato de salida

Todo onboarding debe devolver conceptualmente:

```yaml
objetivo_onboarding:
estado_resultante:
dominios_revisados:
  - dominio:
    estado:
    procedencia_principal:
gaps_materiales: []
conflictos: []
elementos_pendientes_de_validar: []
contexto_escrito: []
contexto_no_escrito_y_motivo: []
trabajo_gtm_ya_habilitado: []
trabajo_gtm_bloqueado: []
siguiente_accion:
```

No es obligatorio mostrar YAML al usuario; sí mantener esta semántica.

## 12. Confianza

La confianza depende de cobertura, procedencia, vigencia y coherencia.

No declarar alta confianza si:

- faltan dominios críticos;
- existen contradicciones materiales;
- una parte importante procede de inferencias;
- la documentación relevante está obsoleta;
- claims o restricciones sensibles no han sido validados.

## 13. Failure modes

### No hay documentación

Continuar mediante preguntas adaptativas. No bloquear onboarding completo por falta de archivos.

### Documentación incompleta

Extraer lo soportado y preguntar únicamente los gaps prioritarios.

### Documentación contradictoria

Registrar conflicto y escalar para validación.

### Documentación promocional ambigua

No convertir lenguaje de marketing en claim técnico confirmado.

### Usuario no sabe una respuesta

Registrar como desconocido. No inventar.

### Usuario no quiere facilitar un dato

Respetar la decisión; indicar qué análisis puede limitar.

### Exceso de información

Priorizar la información relevante para el objetivo actual; no convertir onboarding en archivado documental.

### Información sensible

Minimizar retención y evitar guardar secretos, credenciales o datos personales innecesarios.

## 14. Handoffs

- contexto insuficiente → permanecer en onboarding;
- contexto válido + readiness incierto → futuro `diagnostico-internacional`;
- contexto válido + ICP insuficiente → futura `definicion-icp`;
- contexto válido + decisión de países → futura `priorizacion-de-mercados`;
- conflicto de approval/claim → validación humana antes de trabajo downstream sensible.

## 15. Aprobación humana

Obligatoria para:

- claims técnicos o certificaciones no inequívocamente soportados;
- estrategia o prioridades inferidas;
- condiciones comerciales sensibles;
- conflictos materiales;
- cualquier dato que vaya a tratarse como verdad de empresa cuando su procedencia sea ambigua.

## 16. Reglas de persistencia

Puede persistir:

- información confirmada;
- decisiones explícitamente validadas;
- preferencias y restricciones declaradas;
- elementos pendientes cuando estén claramente etiquetados.

No persistir como verdad:

- hipótesis del modelo;
- research externo no validado;
- brainstorming;
- borradores;
- supuestas necesidades de clientes;
- datos personales innecesarios.

## 17. Anti-patrones

- hacer 40 preguntas antes de revisar documentos disponibles;
- completar campos vacíos con conocimiento general;
- confundir web corporativa con especificación técnica aprobada;
- asumir ICP ideal a partir de clientes actuales sin análisis;
- convertir mercados actuales en mercados prioritarios automáticamente;
- guardar toda conversación como memoria;
- declarar onboarding completado porque todos los archivos contienen texto;
- pedir información de marca cuando la decisión actual no la necesita;
- sustituir una decisión de dirección por la recomendación del modelo.

## 18. Ejemplo mínimo

Usuario: "Quiero configurar el agente para nuestra empresa. Te dejo el catálogo y una presentación comercial."

Comportamiento correcto:

1. inspeccionar ambos documentos;
2. extraer empresa, oferta y aplicaciones soportadas;
3. identificar que falta objetivo actual, mercados prioritarios y restricciones;
4. preguntar esos gaps por bloques;
5. mostrar qué se considera confirmado y qué requiere validación;
6. crear el contexto solo después de suficiente confirmación;
7. declarar qué tareas GTM quedan habilitadas.

## 19. Evaluación

La skill debe superar los escenarios en `tests/escenarios.md` y las propiedades de `tests/criterios-de-evaluacion.md`.
