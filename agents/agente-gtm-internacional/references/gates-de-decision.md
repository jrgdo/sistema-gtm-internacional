# Gates de decisión

## Propósito

Impedir que el sistema avance a trabajo downstream cuando faltan fundamentos que cambiarían materialmente la calidad de la decisión.

Un gate debe ser explícito, proporcional al riesgo y específico de la tarea.

## Gate general de contexto

Antes de cualquier trabajo especializado comprobar:

- objetivo suficientemente claro;
- contexto de empresa relevante;
- dominios críticos sin conflictos bloqueantes;
- frescura suficiente para la decisión;
- ausencia de restricciones conocidas que invaliden el trabajo.

## Gate de priorización de mercados

Requiere como mínimo, cuando aplique:

- oferta o línea prioritaria;
- aplicación o problema que resuelve;
- ICP suficiente;
- objetivo de expansión;
- restricciones de capacidad, canal o servicio relevantes;
- mercados candidatos o criterio de generación de candidatos.

Bloquear o enrutar upstream si falta información que pueda invertir el ranking.

## Gate de investigación de mercado

Requiere:

- mercado/geografía definida;
- pregunta de negocio concreta;
- producto/aplicación relevante;
- ICP o segmento suficiente;
- alcance temporal cuando la frescura sea importante.

No producir un informe genérico de país si la decisión no está definida.

## Gate de evaluación de distribuidores

Requiere:

- mercado o territorio;
- perfil de partner deseado;
- cliente/segmento objetivo;
- oferta/aplicación;
- modelo de canal esperado;
- restricciones y conflictos de canal conocidos;
- criterios mínimos de evaluación.

No recomendar un partner por presencia web, tamaño aparente o número de marcas representadas sin evidencia adicional.

## Gate de investigación de cuentas

Requiere:

- cuenta identificada;
- mercado;
- oferta/aplicación relevante;
- ICP suficiente;
- objetivo comercial de la investigación.

Desk research no equivale a necesidad confirmada.

## Gate de preparación comercial

Requiere:

- cuenta/persona o tipo de interlocutor;
- objetivo de conversación;
- contexto comercial suficiente;
- propuesta/oferta relevante;
- claims/terminología aprobados cuando sean materiales;
- restricciones comerciales conocidas.

## Gate de comunicación externa

Antes de cualquier comunicación externa sensible comprobar:

- contenido factual soportado;
- claims permitidos;
- pricing/condiciones autorizados;
- voz y terminología adecuadas;
- aprobación humana cuando corresponda.

## Gate de aprendizaje

No convertir una observación o resultado aislado en nueva verdad estratégica.

Requiere:

- resultado observado;
- procedencia clara;
- muestra o contexto suficiente;
- explicación de limitaciones;
- validación humana si altera una decisión estratégica.

## Resultado de gate

Cada gate debe resolver uno de estos estados:

- `PASS`: puede continuar;
- `PASS_CON_LIMITES`: puede continuar con restricciones explícitas;
- `REQUIERE_INPUT`: falta contexto/dato;
- `REQUIERE_EVIDENCIA`: falta soporte externo;
- `REQUIERE_VALIDACION_HUMANA`: no puede resolver el modelo;
- `BLOCK`: continuar sería irresponsable.

## Regla de proporcionalidad

No convertir cada pequeño gap en bloqueo. Bloquear únicamente si el gap puede cambiar materialmente la decisión, crear riesgo significativo o inducir falsa certeza.
