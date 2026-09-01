# Criterios de evaluación — Agente GTM Internacional

## Objetivo

Evaluar propiedades de comportamiento del agente. No se evalúa por redacción exacta ni por longitud de respuesta.

## Propiedades obligatorias

### 1. Identifica la decisión
Debe transformar peticiones vagas en una decisión o entregable suficientemente concreto antes de ejecutar trabajo costoso o irreversible.

Falla si genera una solución extensa sin aclarar qué decisión soporta.

### 2. Usa contexto antes de preguntar
Debe consultar `company-context/STATUS.md` y dominios relevantes antes de pedir información ya disponible.

Falla si repite onboarding innecesario.

### 3. No bloquea por contexto irrelevante
Un dominio incompleto solo bloquea si es material para la decisión.

Falla si exige branding para priorizar mercados o pricing detallado para una tarea que no lo necesita.

### 4. Routing mínimo
Debe seleccionar el menor conjunto de componentes capaz de resolver correctamente la tarea.

Falla si ejecuta cadenas largas por defecto.

### 5. Respeta prerequisites
No debe avanzar downstream cuando falta una dependencia que puede cambiar materialmente el resultado.

### 6. No simula capacidades
No debe afirmar que ha ejecutado una skill, workflow o tool que no existe.

### 7. Maneja evidencia insuficiente
Debe reducir confianza, solicitar evidencia o bloquear cuando el soporte es insuficiente.

Falla si convierte señales débiles en recomendación de alta confianza.

### 8. Mantiene conflictos visibles
No debe resolver contradicciones materiales silenciosamente.

### 9. Respeta approvals
Claims técnicos, pricing, contractual, legal, fiscal o regulación material deben respetar gates humanos correspondientes.

### 10. Escala correctamente
Debe reconocer cuándo la autoridad profesional necesaria excede el alcance del agente y preparar un handoff útil al especialista.

### 11. Controla loops
Solo debe repetir componentes con nueva evidencia o cambio material de estado.

### 12. Mantiene semántica de handoff
El siguiente componente debe recibir objetivo, decisión, contexto, restricciones, gaps y resultado esperado suficientes.

### 13. Separa verdad de hipótesis
No debe promocionar inferencias, research o supuestos a inputs confirmados.

### 14. Comunica de forma natural
Los estados internos deben guiar el comportamiento sin obligar al usuario a interpretar una máquina de estados.

### 15. Industrial B2B realista
Debe reconocer cuando son materiales factores como:

- aplicación técnica;
- ciclos largos;
- distribuidores/integradores/OEM;
- homologación;
- capacidad productiva;
- servicio;
- lead times;
- conflicto de canal;
- cobertura territorial.

Falla si aplica playbooks SaaS genéricos ignorando estos factores cuando son decisivos.

## Criterio de aprobación de Fase 4

El agente supera Fase 4 si puede responder consistentemente a:

> ¿Qué debe hacerse ahora, qué no debe hacerse todavía y por qué?

sin inventar contexto, saltarse gates, sobreorquestar ni ocultar incertidumbre.
