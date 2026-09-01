# Roadmap de implementación

Este roadmap define las fases restantes del Sistema GTM Internacional y autoriza su ejecución secuencial sobre `main` sin necesidad de revalidar el alcance al cerrar cada fase, salvo que aparezca un bloqueo real de arquitectura, seguridad o compatibilidad.

## Estado actual

Completadas:

- Fase 1 — constitución, arquitectura y convenciones.
- Fase 2 — Company Context Engine.
- Fase 3 — onboarding de empresa.
- Fase 4 — Agente GTM Internacional.
- Fase 5 — contratos compartidos.
- Fase 6A — diagnóstico internacional, ICP y priorización de mercados.
- Fase 6B — investigación de mercado y evaluación de distribuidores.

## Fases restantes

### Fase 6C — cuentas y preparación comercial

Implementar:

- `investigacion-de-cuentas`;
- `preparacion-comercial`.

Objetivo: conectar inteligencia de mercado y canal con preparación de oportunidades, reuniones y siguientes compromisos comerciales sin convertir hipótesis en necesidades confirmadas.

### Fase 7 — workflows

Implementar workflows asistidos y gobernados para:

- configurar agente;
- diagnosticar expansión;
- comparar mercados;
- explorar nuevo mercado;
- evaluar distribuidor;
- investigar cuenta;
- preparar reunión.

Cada workflow debe declarar precondiciones, skills utilizadas, gates, estados, stops, outputs y handoffs.

### Fase 8 — tools deterministas

Implementar tools locales, transparentes y testeables para:

- validar estructura de contexto;
- calcular scorecards transparentes cuando proceda;
- registrar decisiones;
- validar outputs mínimos y contratos.

Principio: razonamiento para juicio; código para operaciones deterministas.

### Fase 9 — memoria, QA y evaluaciones ejecutables

Implementar:

- memoria local de decisiones, hipótesis y aprendizajes;
- reglas de Quality Guard ligeras;
- fixtures y validadores ejecutables;
- tests de propiedades críticas.

No implementar multi-agent QA de producción ni learning loops automáticos.

### Fase 10 — adopción, instalación y release público

Implementar:

- instalación y primera ejecución;
- guía de personalización;
- buenas prácticas y límites;
- autodiagnóstico de madurez;
- ejemplo de empresa industrial ficticia;
- templates de GitHub Issues/Discussions;
- checklist de release;
- README orientado a adopción y lead magnet.

## Definition of Done global

El repositorio público se considera listo para una primera release cuando:

1. puede configurarse para una empresa sin inventar contexto;
2. el agente enruta correctamente entre las capacidades implementadas;
3. las skills y workflows comparten contratos compatibles;
4. las operaciones deterministas críticas tienen tools y validación;
5. existen tests de propiedades, no solo ejemplos narrativos;
6. el sistema mantiene aprobación humana en decisiones sensibles;
7. la documentación permite instalar, personalizar y entender límites;
8. la experiencia demuestra arquitectura de automatización profesional sin exponer infraestructura privada de producción.
