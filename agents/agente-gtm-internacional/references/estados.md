# Estados del Agente GTM Internacional

## Objetivo

Definir estados operativos claros para evitar que el agente continúe por inercia cuando faltan contexto, evidencia o aprobación.

## Estados

### `SIN_CONFIGURAR`
No existe contexto de empresa suficiente para iniciar trabajo GTM fiable.

Ruta normal: `onboarding-empresa`.

### `CONTEXTUALIZANDO`
El contexto está siendo creado, revisado o actualizado.

No ejecutar trabajo downstream que dependa de dominios todavía no validados.

### `CONTEXTO_PARCIAL`
Existe contexto útil, pero faltan dominios o elementos.

No implica bloqueo automático. Evaluar si los gaps son materiales para la decisión concreta.

### `LISTO_PARA_ROUTING`
El objetivo está suficientemente claro y existe contexto mínimo para decidir el siguiente componente.

### `REQUIERE_CLARIFICACION`
La petición es demasiado ambigua para seleccionar un proceso fiable.

Hacer la mínima pregunta de alto valor necesaria para distinguir entre decisiones posibles.

### `REQUIERE_EVIDENCIA`
La decisión está clara, pero faltan datos o evidencia necesarios para analizarla responsablemente.

### `EN_EJECUCION`
Un workflow, skill o tool está trabajando sobre la decisión.

### `REQUIERE_VALIDACION_HUMANA`
Existe un gate que el sistema no debe resolver por sí mismo.

Ejemplos: conflicto estratégico, claim sensible, pricing, compromiso contractual o expertise regulatorio.

### `LISTO_PARA_DECISION`
El análisis está suficientemente preparado para que una persona responsable tome una decisión.

No significa que la IA haya tomado la decisión final.

### `BLOQUEADO`
No se puede continuar de forma responsable con la información o permisos disponibles.

Debe indicarse causa y condición de desbloqueo.

### `CERRADO`
El objetivo se ha completado, abandonado explícitamente o sustituido por otra decisión.

## Transiciones válidas frecuentes

```text
SIN_CONFIGURAR → CONTEXTUALIZANDO → CONTEXTO_PARCIAL/VALIDADO → LISTO_PARA_ROUTING
LISTO_PARA_ROUTING → EN_EJECUCION
EN_EJECUCION → REQUIERE_EVIDENCIA → EN_EJECUCION
EN_EJECUCION → REQUIERE_VALIDACION_HUMANA → EN_EJECUCION/LISTO_PARA_DECISION
EN_EJECUCION → LISTO_PARA_DECISION → CERRADO
```

## Regla de no progreso

Si dos iteraciones consecutivas no cambian materialmente evidencia, contexto, estado o decisión, detener el loop y revisar routing o solicitar intervención humana.
