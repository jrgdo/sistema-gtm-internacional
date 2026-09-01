# Quality Guard

El Quality Guard es una capa ligera de revisión de propiedades críticas antes de considerar un output listo para decisión.

No es un segundo agente autónomo ni sustituye revisión humana.

## Checks obligatorios

### Evidencia
- ¿Las afirmaciones materiales tienen procedencia adecuada?
- ¿Se distingue evidencia de inferencia e hipótesis?
- ¿La frescura es suficiente para la decisión?

### Contexto
- ¿El contexto usado está validado y vigente?
- ¿Existe conflicto abierto material?
- ¿Se ha cargado únicamente contexto relevante?

### Decisión
- ¿La pregunta/decisión está clara?
- ¿La recomendación es proporcional a la evidencia?
- ¿Unknowns críticos están visibles?
- ¿Existe siguiente acción verificable?

### Industrial B2B
- ¿Se han considerado aplicación, canal, homologación, servicio, capacidad, logística o buying complexity cuando son materiales?
- ¿Se ha evitado importar un playbook SaaS/consumo sin adaptación?

### Claims y approvals
Bloquear o escalar si aparecen sin validación suficiente:

- claims técnicos;
- certificaciones;
- suitability regulatoria;
- ROI/resultados cliente;
- pricing/descuentos;
- garantías;
- exclusividad;
- compromisos contractuales;
- comunicaciones externas sensibles.

## Errores críticos

Un output no puede marcarse `LISTO_PARA_DECISION` si:

- presenta una hipótesis como hecho;
- trata unknown como cero sin criterio explícito;
- recomienda distribuidor por presencia online sin evidencia de capacidad/acceso;
- presenta research como customer discovery;
- declara necesidad de cuenta sin evidencia;
- oculta conflicto material;
- usa alta confianza con evidencia débil o incompleta;
- recomienda una acción sensible sin approval requerido.

## Resultado del guard

- `PASS`
- `PASS_CON_LIMITES`
- `REQUIERE_EVIDENCIA`
- `REQUIERE_VALIDACION_HUMANA`
- `BLOCK`
