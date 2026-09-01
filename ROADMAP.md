# Roadmap de implementación

Este roadmap documenta la primera implementación pública del Sistema GTM Internacional.

## Fases completadas

- Fase 1 — constitución, arquitectura y convenciones.
- Fase 2 — Company Context Engine.
- Fase 3 — onboarding de empresa.
- Fase 4 — Agente GTM Internacional.
- Fase 5 — contratos compartidos.
- Fase 6A — diagnóstico internacional, ICP y priorización de mercados.
- Fase 6B — investigación de mercado y evaluación de distribuidores.
- Fase 6C — investigación de cuentas y preparación comercial.
- Fase 7 — workflows asistidos y gobernados.
- Fase 8 — tools deterministas.
- Fase 9 — memoria local, Quality Guard, tests y CI.
- Fase 10 — instalación, bootstrap, documentación, ejemplo y preparación de adopción pública.

## Estado

**Primera arquitectura pública implementada.**

Esto no significa que el sistema esté terminado para siempre. Significa que ya existe un vertical slice coherente desde instalación y contexto hasta decisión, workflows, tools, QA y memoria.

## Próximas líneas de evolución

Las siguientes mejoras deben venir de uso real, tests y feedback, no de añadir componentes por volumen.

Prioridades posibles:

1. endurecer evaluaciones ejecutables con fixtures;
2. mejorar compatibilidad de instalación entre agentes;
3. añadir ejemplos end-to-end más completos;
4. revisar scorecards con casos reales anonimizados o ficticios;
5. añadir nuevas skills únicamente cuando aparezca una decisión repetible no cubierta;
6. mejorar documentación de localización por mercado;
7. ampliar tools deterministas cuando exista una necesidad estable.

## Fuera del roadmap público base

No incorporar por defecto:

- arquitectura multiagente de producción;
- integraciones CRM/ERP específicas de cliente;
- monitoring continuo;
- queues/retries/observabilidad empresarial;
- permisos y secrets management de producción;
- automatización autónoma de comunicaciones externas;
- scoring propietario avanzado;
- learning loops automáticos de cliente.

## Definition of Done de la primera release

La primera release debe poder demostrar que:

1. una empresa puede inicializar contexto sin inventar datos;
2. el sistema sabe qué skill/workflow usar y cuándo detenerse;
3. todas las capacidades comparten principios de evidencia y handoff;
4. las operaciones deterministas clave tienen código;
5. existen tests y CI;
6. decisiones sensibles conservan aprobación humana;
7. instalación y límites están documentados;
8. el repositorio demuestra arquitectura profesional sin exponer implementaciones privadas de producción.
