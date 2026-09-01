# Workflow — Configurar agente

## Objetivo
Crear o actualizar un `company-context/` suficientemente fiable para un objetivo GTM concreto.

## Precondiciones
Ninguna. Puede ejecutarse en primera instalación.

## Secuencia
1. Leer instrucciones raíz y contratos.
2. Comprobar `company-context/STATUS.md`.
3. Ejecutar `onboarding-empresa`.
4. Revisar resultado: validado, parcial, conflicto, input insuficiente.
5. Resolver únicamente gaps materiales para el objetivo.
6. Actualizar contexto y `STATUS.md` según política.
7. Devolver control al Agente GTM Internacional.

## Gates
- conflicto material → `REQUIERE_VALIDACION_HUMANA`;
- input insuficiente → `BLOCK` para decisiones dependientes;
- contexto parcial no crítico → `PASS_CON_LIMITES`.

## Output
Estado del contexto, dominios habilitados/bloqueados y siguiente acción.
