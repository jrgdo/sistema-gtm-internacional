# Contratos compartidos del sistema

## 1. Propósito

Los contratos de `contracts/` definen el lenguaje común entre agente, workflows, skills y tools.

No son formularios para el usuario final. Son acuerdos de interoperabilidad.

## 2. Problema que resuelven

Sin contratos compartidos, cada componente tendería a devolver estructuras diferentes y el agente tendría que reinterpretar continuamente:

- qué decisión se está preparando;
- qué evidencia existe;
- qué es hecho o hipótesis;
- qué falta;
- qué confianza corresponde;
- qué debe ocurrir después.

Eso aumenta ambigüedad, coste y riesgo de pérdida de contexto.

## 3. Contrato de entrada

`contracts/entrada-componente.yaml`

Debe usarse conceptualmente antes de invocar una skill, workflow o tool.

Contiene:

- objetivo;
- decisión;
- entregable esperado;
- estado actual;
- contexto relevante;
- inputs confirmados;
- restricciones;
- gaps;
- evidencia disponible;
- componente destino;
- criterio de finalización;
- approvals relevantes.

No rellenar campos faltantes mediante inferencia solo para completar el schema.

## 4. Contrato de salida

`contracts/salida-componente.yaml`

Todo componente sustantivo debe poder expresar:

- resultado;
- estado;
- hechos;
- inferencias;
- hipótesis;
- supuestos;
- desconocidos;
- evidencia;
- confianza;
- riesgos;
- validación;
- siguiente acción;
- handoff;
- persistencia permitida.

## 5. Evidencia

`contracts/evidencia.yaml` evita que una URL o documento se trate como evidencia sin contexto.

La evidencia debe conservar, cuando sea material:

- qué afirmación soporta;
- tipo de fuente;
- fecha;
- alcance geográfico/sectorial;
- autoridad;
- actualidad;
- relevancia;
- limitaciones;
- conflictos.

## 6. Decisiones

`contracts/decision.yaml` representa una decisión preparada para revisión humana.

Una recomendación no equivale a una decisión aprobada.

Debe mantener separadas:

- opciones consideradas;
- criterios;
- recomendación;
- evidencia;
- supuestos;
- riesgos;
- condiciones para avanzar;
- validación humana;
- responsable.

## 7. Estados

`contracts/estados.yaml` mantiene vocabularios separados para:

- estado del sistema;
- estado del contexto;
- resultado propio del onboarding;
- stop conditions.

No reutilizar un estado de una capa como si significara lo mismo en otra.

## 8. Confianza

`contracts/confianza.yaml` formaliza `ALTA`, `MEDIA`, `BAJA` y `NO_EVALUABLE`.

La confianza nunca depende de lo convincente que parezca la redacción.

## 9. Handoffs

`contracts/handoff.yaml` debe permitir que el siguiente componente trabaje con el mínimo contexto suficiente.

El handoff debe preservar gaps y conflictos. No simplificarlos para que el flujo parezca limpio.

## 10. Errores y bloqueos

`contracts/error-operativo.yaml` representa estados donde no procede continuar normalmente.

Un bloqueo puede ser un resultado correcto.

Ejemplos:

- contexto insuficiente;
- evidencia insuficiente;
- conflicto material;
- approval pendiente;
- petición fuera de scope.

## 11. Cierre

`contracts/cierre-ejecucion.yaml` resume el resultado coordinado y prepara futura memoria y decision logging.

## 12. Compatibilidad de nuevas capacidades

Toda nueva skill debe indicar cómo consume `entrada-componente` y cómo produce semánticamente `salida-componente`.

Todo workflow debe utilizar `handoff` para transferencias relevantes.

Toda tool futura debe declarar claramente qué parte del contrato recibe y qué parte devuelve.

## 13. Evolución

Los archivos YAML actuales son contratos declarativos. En Fase 8 podrán traducirse a JSON Schema, Pydantic, Zod u otro mecanismo de validación determinista.

No introducir validación ejecutable antes de que los contratos hayan demostrado estabilidad suficiente con skills reales.
