# Tools deterministas

Esta carpeta contiene operaciones que deben ejecutarse de forma repetible y verificable.

Principio:

> **Modelo para juicio. Código para validación, cálculo, transformación y persistencia determinista.**

Tools iniciales:

- `validar_contexto.py` — comprueba estructura mínima de `company-context/`;
- `calcular_score_mercado.py` — calcula score transparente a partir de criterios explícitos;
- `calcular_score_distribuidor.py` — calcula score transparente de evaluación de partner;
- `registrar_decision.py` — crea registros estructurados de decisiones;
- `validar_contrato.py` — verifica campos mínimos en payloads YAML de contratos.

Estas tools no sustituyen metodología ni deciden pesos por sí mismas. Los criterios y pesos deben proceder del contexto, la skill o una decisión humana explícita.
