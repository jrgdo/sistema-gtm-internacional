# Política de handoffs

## Propósito

Asegurar que cada componente reciba contexto suficiente, produzca una salida interpretable y no obligue al siguiente componente a reconstruir la intención desde cero.

## Principio

Un handoff debe transportar **la decisión**, no solo texto.

## Paquete mínimo de entrada

Antes de invocar una skill o workflow, preparar semánticamente:

```yaml
objetivo:
decision:
estado_actual:
contexto_relevante:
inputs_confirmados:
restricciones:
gaps:
evidencia_disponible:
componente_destino:
resultado_esperado:
criterio_de_finalizacion:
```

No es obligatorio serializarlo todavía. Fase 5 formalizará schemas.

## Paquete mínimo de retorno

Todo componente debe devolver semánticamente:

```yaml
resultado:
estado:
evidencia:
supuestos:
desconocidos:
confianza:
riesgos:
validacion_necesaria:
siguiente_accion:
handoff_recomendado:
```

## Reglas

1. No pasar todo el repositorio como contexto si no es necesario.
2. No ocultar gaps al componente siguiente.
3. No promover hipótesis a input confirmado.
4. No asumir que el siguiente componente entiende automáticamente la decisión anterior.
5. Conservar restricciones y approvals relevantes en todo handoff downstream.
6. Si cambia el objetivo, reconstruir el handoff.
7. Si el componente devuelve `INPUT_INSUFICIENTE`, `CONFLICTO` o `REQUIERE_VALIDACION`, no convertirlo silenciosamente en éxito.

## Handoff upstream

Se usa cuando una dependencia anterior está incompleta.

Ejemplo:

```text
priorizacion-de-mercados
→ detecta ICP insuficiente
→ handoff a definicion-icp
→ retorna ICP validable
→ vuelve a priorizacion
```

## Handoff downstream

Solo ejecutar si el componente anterior ha alcanzado su criterio de finalización suficiente.

## Handoff a humano

Debe explicar:

- qué necesita decisión humana;
- por qué el modelo no debe decidirlo;
- evidencia disponible;
- alternativas y trade-offs si existen;
- qué componente podrá continuar después.

## Loops

Un loop solo se permite cuando el nuevo handoff contiene información material nueva.

Si no cambia evidencia, estado, restricción o decisión, detener el loop.

## Trazabilidad futura

En fases posteriores cada ejecución podrá incorporar identificadores como `run_id`, `decision_id` y versiones de contexto. En Fase 4 solo se fija la semántica para no acoplar prematuramente la arquitectura a un formato técnico.
