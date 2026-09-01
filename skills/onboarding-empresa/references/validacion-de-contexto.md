# Protocolo de validación de contexto

## Objetivo

Determinar si el contexto recopilado es suficientemente fiable y completo para soportar una decisión GTM concreta.

## 1. Validar para un objetivo, no en abstracto

No existe un contexto universalmente "completo".

La suficiencia depende del trabajo siguiente.

Ejemplo:

- para investigar una cuenta puede bastar empresa, oferta, aplicación e ICP;
- para priorizar mercados se necesitan además restricciones, capacidad de ganar y objetivos;
- para preparar comunicación externa pueden ser necesarios claims, voz, terminología y aprobaciones.

## 2. Dimensiones de validación

Evaluar cada dominio relevante en cinco dimensiones:

### Cobertura
¿Tenemos la información necesaria?

### Procedencia
¿De dónde viene y quién tiene autoridad sobre ella?

### Frescura
¿Sigue siendo razonablemente vigente para la decisión?

### Coherencia
¿Existen contradicciones materiales?

### Sensibilidad
¿Requiere aprobación adicional por impacto técnico, comercial, legal o reputacional?

## 3. Estados de dominio

- `VALIDADO`: suficiente para el objetivo definido.
- `PARCIAL`: utilizable con limitaciones explícitas.
- `PENDIENTE`: falta información material.
- `OBSOLETO`: la vigencia es insuficiente.
- `CONFLICTO`: existen fuentes incompatibles con impacto material.

## 4. Regla de bloqueo

Un dominio bloquea trabajo downstream cuando:

- es esencial para la decisión;
- está `PENDIENTE`, `OBSOLETO` o `CONFLICTO`;
- y avanzar exigiría inventar o asumir algo material.

No bloquear por información opcional.

## 5. Resumen de validación humana

Antes de promover contexto crítico a validado, presentar de forma compacta:

### Entendido y soportado
Hechos y decisiones principales.

### Pendiente de confirmar
Información candidata relevante.

### Conflictos
Contradicciones que afectan el uso.

### Gaps
Lo que todavía falta.

### Restricciones
Condiciones que deben respetarse.

### Trabajo habilitado
Qué análisis puede ejecutarse ya.

## 6. Correcciones

Si el usuario corrige un dato:

1. identificar qué archivo y dominio afecta;
2. comprobar si invalida otros elementos;
3. actualizar procedencia/fecha cuando sea material;
4. revisar `STATUS.md`;
5. no mantener simultáneamente como confirmadas dos versiones incompatibles.

## 7. Confirmación parcial

La validación puede ser granular.

Ejemplo:

> "Confirmo productos y mercados actuales, pero todavía no está aprobada la estrategia 2027."

Resultado:

- productos → `VALIDADO`;
- mercados actuales → `VALIDADO`;
- estrategia futura → `PENDIENTE`.

No exigir una confirmación global falsa.

## 8. Umbral de readiness

Declarar `CONTEXTO_VALIDADO_PARA_OBJETIVO` solo si:

- todos los dominios bloqueantes están validados o suficientemente soportados;
- no hay conflictos materiales sin resolver;
- no se depende de inferencias ocultas;
- las limitaciones importantes son visibles;
- el usuario o fuente autorizada ha validado los elementos sensibles cuando corresponde.

## 9. Principio

**Validar contexto no significa certificar que la estrategia sea correcta. Significa que el sistema comprende suficientemente la realidad declarada de la empresa para empezar a trabajar sin inventarla.**