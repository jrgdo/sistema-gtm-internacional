# Workflow — Investigar cuenta

## Objetivo
Decidir si una cuenta merece atención adicional y preparar validación comercial basada en evidencia.

## Precondiciones
- cuenta identificada;
- ICP suficiente;
- oferta/aplicación;
- mercado/geografía;
- objetivo comercial.

## Secuencia
1. Validar identidad y contexto.
2. Ejecutar `investigacion-de-cuentas`.
3. Revisar fit, señales, hipótesis y unknowns.
4. Si falta contexto de mercado material, ejecutar `investigacion-de-mercado` solo para ese gap.
5. Clasificar prioridad de investigación/validación.
6. Si existe interacción próxima, handoff a `preparacion-comercial`.

## Gates
- ICP insuficiente → `definicion-icp`;
- identidad dudosa → `REQUIERE_EVIDENCIA`;
- fit técnico crítico no validado → ingeniería/producto.

## Output
Fit, evidencia, hipótesis comerciales, stakeholders probables, unknowns, preguntas y siguiente acción.
