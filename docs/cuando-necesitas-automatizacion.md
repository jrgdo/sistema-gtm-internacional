# Cuándo necesitas automatización

El repositorio público está diseñado para ayudar a estructurar decisiones y ejecutar workflows asistidos. No todo proceso necesita automatización de producción.

## Señales de que el sistema manual/asistido empieza a quedarse corto

- el equipo repite la misma investigación muchas veces;
- hay copy/paste constante entre IA, hojas, CRM y Drive;
- el contexto se queda desactualizado;
- varias personas aplican criterios diferentes;
- los approvals dependen de mensajes o memoria individual;
- se necesitan señales recurrentes de mercados/cuentas;
- hay cientos de cuentas o distribuidores que evaluar;
- los resultados deben escribirse automáticamente en sistemas internos;
- los fallos de integración necesitan retries, logs y ownership;
- la dirección necesita reporting continuo.

## Qué cambia en una implementación profesional

Una automatización real puede requerir:

- CRM/ERP/Drive;
- bases de datos;
- APIs y enrichment;
- scheduling y triggers;
- permissions/secrets;
- human-in-the-loop;
- observabilidad;
- retries y manejo de errores;
- evaluaciones de calidad;
- mantenimiento.

## Regla

**Automatizar cuando el workflow ya está suficientemente entendido y la repetición/integración justifica la complejidad.**

No automatizar para ocultar un proceso mal definido.
