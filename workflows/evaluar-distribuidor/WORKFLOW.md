# Workflow — Evaluar distribuidor

## Objetivo
Determinar si un candidato merece avanzar, qué debe validarse y cuál es el siguiente compromiso antes de decisiones de mayor riesgo.

## Precondiciones
- mercado y aplicación;
- ICP/cliente objetivo;
- perfil de partner deseado;
- modelo de canal o hipótesis suficiente.

## Secuencia
1. Validar prerequisites.
2. Ejecutar `evaluacion-de-distribuidores`.
3. Clasificar evidencia vs claims del candidato.
4. Identificar gaps materiales: acceso, capacidad, conflictos, prioridad, operativa.
5. Preparar preguntas y siguiente compromiso verificable.
6. Si hay reunión próxima, ejecutar `preparacion-comercial`.
7. Escalar exclusividad, contrato, pricing o regulación antes de comprometerse.

## Gates
- perfil de partner inexistente → upstream;
- conflicto de portfolio crítico → `REQUIERE_VALIDACION_HUMANA` o `BLOCK`;
- evidencia insuficiente → no shortlist definitivo.

## Output
Estado del candidato, evidencias, unknowns, riesgos, preguntas de validación y siguiente compromiso.
