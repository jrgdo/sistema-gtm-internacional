# Scoring y sensibilidad

## Principio

El scoring ayuda a hacer explícito el criterio; no convierte una decisión compleja en una verdad matemática.

## Reglas

- definir criterios antes de puntuar;
- documentar escala y significado de cada puntuación;
- usar pesos explícitos;
- asegurar que los pesos suman 100 cuando se agregan;
- no asignar cero a datos ausentes: usar `NO_EVALUABLE` o gap;
- evitar decimales que sugieran precisión inexistente;
- conservar evidencia detrás de cada score.

## Sensibilidad

Antes de tratar el ranking como robusto, comprobar:

1. si un cambio razonable de pesos altera el top 1–3;
2. si un único criterio domina el resultado;
3. si el ranking depende de un dato antiguo o débil;
4. si mercados con datos incompletos parecen artificialmente peores.

## Interpretación

- ranking estable + evidencia sólida → mayor confianza;
- ranking sensible + evidencia parcial → investigar antes de invertir;
- resultado dominado por una hipótesis → tratar como experimento;
- diferencias mínimas entre mercados → no fingir superioridad clara.

## Automatización futura

En una fase posterior, los cálculos podrán pasar a una tool determinista. Hasta entonces, la metodología y las reglas deben permanecer transparentes.