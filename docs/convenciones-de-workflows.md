# Convenciones de workflows

## Objetivo

Definir cómo se modelan procesos completos para que el agente pueda ejecutar trabajo GTM de forma consistente, auditable y segura.

## Qué es un workflow

Un workflow representa un proceso operativo con inicio, precondiciones, pasos, decisiones, posibles bucles, criterios de parada y outputs.

No es una skill grande ni una checklist informal.

## Anatomía obligatoria

Todo futuro `WORKFLOW.md` debe incluir:

1. **Nombre y propósito**
2. **Trigger**
3. **Precondiciones**
4. **Contexto requerido**
5. **Estado inicial**
6. **Pasos ordenados**
7. **Skills utilizadas**
8. **Tools utilizadas**
9. **Decision gates**
10. **Condiciones de loop/reintento**
11. **Condiciones de parada**
12. **Aprobaciones humanas**
13. **Outputs**
14. **Persistencia**
15. **Errores y recuperación**
16. **Criterio de finalización**
17. **Tests o escenarios de aceptación**

## Regla de routing mínimo

El workflow debe utilizar el menor conjunto de componentes que permita resolver correctamente el trabajo.

No ejecutar todas las skills disponibles “por si acaso”.

## Preconditions

Un workflow no debe comenzar silenciosamente si faltan datos esenciales.

Ejemplo: comparar mercados requiere comprender al menos:

- oferta o aplicación relevante;
- objetivo;
- ICP o segmento suficiente;
- restricciones relevantes.

Si faltan, el workflow debe enrutar a la dependencia adecuada.

## Decision gates

Cada gate debe expresar:

- pregunta de decisión;
- información utilizada;
- posibles estados;
- consecuencia de cada estado.

Ejemplo:

```text
¿Hay evidencia suficiente?
├── sí → continuar
├── parcial → continuar con confianza limitada / pedir validación
└── no → ampliar investigación o detener
```

## Loops

Los bucles deben tener criterio de salida. Evitar agentes que “investigan hasta estar satisfechos”.

Un loop debe indicar:

- qué información falta;
- qué acción intenta conseguirla;
- número o condición razonable de reintento;
- cuándo aceptar incertidumbre.

## Human-in-the-loop

El workflow debe colocar aprobación humana donde cambia el riesgo.

Ejemplo:

- research interno → puede continuar;
- shortlist de distribuidores → revisión recomendable;
- contacto o compromiso externo → aprobación explícita.

## Estado

Los workflows futuros deberán utilizar estados compatibles con la arquitectura global.

No depender únicamente del texto libre de conversación para saber dónde está el proceso.

## Idempotencia conceptual

Reejecutar un workflow no debería duplicar decisiones o destruir contexto validado.

Cuando exista persistencia, el workflow debe comprobar estado previo antes de escribir.

## Errores

Distinguir:

- error técnico;
- input insuficiente;
- evidencia insuficiente;
- contradicción;
- necesidad de aprobación;
- tarea fuera de scope.

No tratarlos todos como “no puedo”.

## Ejemplo de workflow correcto

```text
Explorar nuevo mercado
↓
Contexto válido?
├── no → onboarding
└── sí
↓
Mercado ya seleccionado?
├── no → priorización
└── sí
↓
Investigación orientada a decisión
↓
Evidencia suficiente?
├── no → ampliar / declarar incertidumbre
└── sí
↓
Identificar opciones de entrada
↓
Preparar recomendación y experimento de validación
↓
Decisión humana
```

## Criterio de rechazo

Rechazar un workflow si:

- solo enumera tareas;
- no tiene gates;
- no declara dependencias;
- no tiene condición de parada;
- mezcla metodología especializada que debería estar en una skill;
- automatiza acciones sensibles sin aprobación.
