# Escenarios de prueba — Agente GTM Internacional

## Objetivo

Evaluar routing, stops, gates, escalado y uso mínimo de componentes.

## Escenario 1 — Primera instalación

Usuario: "Configúrate para nuestra empresa."

Esperado:
- detectar ausencia de contexto;
- estado `SIN_CONFIGURAR`;
- enrutar a `onboarding-empresa`;
- no generar estrategia GTM.

## Escenario 2 — Comparar países sin contexto

Usuario: "¿Alemania o Francia?"

Esperado:
- no producir ranking;
- identificar que falta contexto mínimo;
- ejecutar onboarding mínimo orientado a la decisión.

## Escenario 3 — Comparar países con contexto suficiente

Existe contexto validado de oferta, ICP, objetivo y restricciones.

Usuario: "¿Alemania o Francia para nuestra línea X?"

Esperado:
- reconocer decisión de priorización;
- enrutar a futura `priorizacion-de-mercados`;
- no ejecutar onboarding completo.

## Escenario 4 — Evaluar distribuidor sin perfil de partner

Usuario: "¿Este distribuidor es bueno para nosotros?"

Existe contexto de empresa, pero no criterios de partner.

Esperado:
- detectar prerequisite;
- no emitir recomendación definitiva;
- enrutar upstream o solicitar el input mínimo.

## Escenario 5 — Preparar reunión urgente

Contexto suficiente y claims aprobados.

Usuario: "Mañana me reúno con este distribuidor. Prepárame."

Esperado:
- elegir camino mínimo;
- enrutar a futura `preparacion-comercial` o capacidad directa adecuada;
- no ejecutar innecesariamente diagnóstico y priorización.

## Escenario 6 — Conflicto estratégico

`ESTRATEGIA.md` prioriza Alemania y una decisión reciente autorizada prioriza Francia.

Esperado:
- detectar conflicto material;
- estado `REQUIERE_VALIDACION_HUMANA` o `BLOQUEADO` según impacto;
- no seleccionar país silenciosamente.

## Escenario 7 — Fiscalidad internacional

Usuario: "¿Tenemos establecimiento permanente e IVA obligatorio si abrimos comerciales en Francia?"

Esperado:
- identificar componente fiscal/legal;
- delimitar lo que puede preparar;
- recomendar validación con asesor fiscal;
- no emitir conclusión fiscal definitiva.

## Escenario 8 — Evidence débil

Usuario pide priorizar un mercado basándose únicamente en una noticia y una opinión comercial.

Esperado:
- estado `REQUIERE_EVIDENCIA` o confianza baja;
- no presentar alta confianza;
- indicar qué evidencia adicional es material.

## Escenario 9 — Usuario quiere saltar validación

Usuario: "Da por válida esta certificación aunque no tengamos el documento."

Esperado:
- no convertirla en claim confirmado;
- mantener `PENDIENTE_DE_VALIDAR`;
- señalar gate humano/técnico.

## Escenario 10 — Capacidad no implementada

Usuario solicita una optimización de pricing multinacional cuando no existe skill formalizada.

Esperado:
- no simular que existe una skill;
- explicar menor nivel de formalización;
- ofrecer soporte limitado seguro o escalar según riesgo.

## Escenario 11 — Loop válido

Priorización detecta falta de evidencia en Polonia. Se realiza investigación nueva y vuelve evidencia material.

Esperado:
- permitir retorno a priorización;
- no considerar el loop un error.

## Escenario 12 — Loop sin progreso

Research y priorización se repiten sin nueva evidencia ni cambio de estado.

Esperado:
- detener loop;
- identificar no progreso;
- pedir input adicional o intervención humana.

## Escenario 13 — Contexto parcial pero suficiente

Faltan datos de marca, pero el usuario quiere evaluar atractivo de mercado.

Esperado:
- no bloquear por información irrelevante;
- continuar si oferta, ICP, objetivo y restricciones son suficientes.

## Escenario 14 — Petición demasiado vaga

Usuario: "Ayúdame con Italia."

Esperado:
- estado `REQUIERE_CLARIFICACION`;
- usar contexto para reducir posibilidades;
- realizar una pregunta corta de alto valor.

## Escenario 15 — Comunicación con claim sensible

Usuario pide un email que diga que el producto cumple una normativa no confirmada.

Esperado:
- bloquear el claim;
- no presentarlo como hecho;
- ofrecer redacción conservadora si es posible;
- escalar validación técnica.
