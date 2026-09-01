# Workflow — Comparar mercados

## Objetivo
Comparar países o mercados candidatos de forma trazable para decidir dónde profundizar primero.

## Precondiciones
- oferta/aplicación prioritaria;
- ICP suficiente;
- objetivo y restricciones;
- mercados candidatos definidos o shortlist inicial.

## Secuencia
1. Validar contexto y objetivo.
2. Ejecutar `priorizacion-de-mercados`.
3. Identificar criterios con evidencia débil.
4. Ejecutar `investigacion-de-mercado` únicamente sobre gaps capaces de cambiar el ranking.
5. Repriorizar solo si existe nueva evidencia material.
6. Preparar decisión humana y plan de validación del mercado prioritario.

## Gates
- ICP insuficiente → `definicion-icp`;
- evidencia no comparable → `REQUIERE_EVIDENCIA`;
- ranking sensible a supuestos no validados → `PASS_CON_LIMITES` o validación adicional.

## Output
Ranking razonado, atractivo, capacidad de ganar, fricción, sensibilidad, unknowns y siguiente validación.
