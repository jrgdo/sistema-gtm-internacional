# Convenciones de tools

## Objetivo

Definir cuándo una operación debe implementarse como herramienta determinista en lugar de delegarse al razonamiento probabilístico del modelo.

## Principio

**El modelo decide e interpreta. La tool calcula, valida, transforma o persiste.**

## Cuándo crear una tool

Crear una tool cuando la tarea requiera:

- cálculo repetible;
- validación de schema;
- normalización de datos;
- transformación determinista;
- lectura/escritura estructurada;
- persistencia;
- integración con sistemas;
- comprobaciones binarias o reglas explícitas;
- operaciones donde un error silencioso sería costoso.

## Cuándo NO crear una tool

No crear una tool para:

- redactar opiniones;
- interpretar matices comerciales;
- formular hipótesis;
- comparar evidencia cualitativa sin reglas formales;
- sustituir una skill metodológica.

## Contrato mínimo

Toda tool futura debe definir:

1. nombre;
2. responsabilidad única;
3. inputs tipados;
4. validación de inputs;
5. output tipado;
6. errores esperables;
7. side effects;
8. reglas de idempotencia cuando aplique;
9. seguridad;
10. tests.

## Inputs

No aceptar texto libre cuando una estructura tipada reduzca ambigüedad.

Ejemplo preferido:

```json
{
  "criterios": [
    {"nombre": "acceso_cliente", "peso": 0.30, "puntuacion": 4}
  ]
}
```

frente a:

`Calcula más o menos qué distribuidor parece mejor.`

## Outputs

Una tool debe devolver datos suficientes para auditar el resultado.

Ejemplo de score:

- score total;
- componentes;
- pesos utilizados;
- warnings;
- inputs faltantes.

No devolver únicamente `82/100` sin explicación.

## Errores

Los errores deben ser explícitos y accionables.

Ejemplos:

- `INPUT_INVALIDO`;
- `CAMPO_REQUERIDO`;
- `PESOS_NO_SUMAN_1`;
- `ESTADO_NO_PERMITIDO`;
- `ARCHIVO_NO_ENCONTRADO`.

No ocultar errores técnicos convirtiéndolos en una recomendación comercial.

## Idempotencia

Para operaciones de escritura:

- comprobar si el registro ya existe;
- evitar duplicados;
- mantener identificadores estables cuando sea posible;
- no sobrescribir información confirmada sin una regla explícita.

## Seguridad

Las tools públicas no deben incluir:

- credenciales embebidas;
- tokens;
- claves privadas;
- endpoints de clientes;
- datos confidenciales de ejemplo.

Las futuras integraciones deben separar configuración, secretos y código.

## Logging

Cuando una tool modifique estado, debe poder indicar:

- qué hizo;
- sobre qué objeto;
- resultado;
- error o warning;
- timestamp cuando sea relevante.

## Tests

Cada tool determinista debe incluir tests de:

- caso correcto;
- input vacío;
- límites;
- tipos inválidos;
- errores esperables;
- repetición/idempotencia cuando corresponda.

## Primeras tools previstas

En fases posteriores podrían incluirse:

- validador de contexto de empresa;
- calculadora transparente de score de mercados;
- calculadora transparente de score de distribuidores;
- registrador de decisiones;
- validador de contratos de salida.

Estas previsiones no autorizan su implementación antes de cerrar sus contratos.
