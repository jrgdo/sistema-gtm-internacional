# Convenciones de skills

## Objetivo

Evitar skills genéricas, solapadas o difíciles de evaluar. Cada skill debe representar una capacidad profesional reutilizable con inputs, método, outputs y límites claros.

## Regla de entrada

No crear una skill porque una tarea pueda describirse con un prompt. Crear una skill solo cuando exista una responsabilidad especializada que:

- se repita;
- tenga una metodología reconocible;
- requiera criterios consistentes;
- produzca un output reutilizable;
- pueda evaluarse;
- tenga límites claros.

## Anatomía obligatoria

Toda futura `SKILL.md` deberá incluir, como mínimo:

1. **Nombre y propósito**
2. **Cuándo usarla**
3. **Cuándo no usarla**
4. **Decisión o trabajo que soporta**
5. **Inputs requeridos**
6. **Inputs opcionales**
7. **Dependencias**
8. **Requisitos de evidencia**
9. **Método paso a paso**
10. **Reglas de decisión**
11. **Contrato de salida**
12. **Niveles o reglas de confianza**
13. **Failure modes**
14. **Handoffs / routing siguiente**
15. **Aprobación humana necesaria**
16. **Reglas de persistencia**
17. **Anti-patrones**
18. **Ejemplos**
19. **Criterios de evaluación/tests**

## Scope

Una skill debe tener una responsabilidad suficientemente estrecha.

Mal:

`estrategia-gtm-total`

Mejor:

- `priorizacion-de-mercados`;
- `evaluacion-de-distribuidores`;
- `investigacion-de-cuentas`.

El agente o workflow coordina varias skills cuando la tarea es más amplia.

## Inputs

Los inputs deben distinguir:

- contexto obligatorio;
- evidencia externa;
- decisiones previas;
- preferencias del usuario;
- restricciones.

Una skill debe poder declarar `INPUT_INSUFICIENTE` en lugar de rellenar huecos.

## Método

El método debe describir cómo trabaja un profesional competente, no una lista de verbos vagos.

Evitar:

- “analiza profundamente”;
- “actúa como experto”;
- “encuentra las mejores opciones”;
- “haz una investigación exhaustiva”.

Preferir pasos observables y criterios explícitos.

## Output contract

El output debe estar diseñado para la siguiente decisión o handoff.

Ejemplo conceptual:

```yaml
objetivo:
contexto_usado:
evidencia:
resultado:
confianza:
supuestos:
desconocidos:
riesgos:
validacion_necesaria:
siguiente_accion:
```

El schema compartido definitivo se formalizará en Fase 5.

## Confianza

Una skill no puede declarar alta confianza si:

- faltan inputs esenciales;
- la evidencia es antigua o secundaria;
- existen contradicciones materiales;
- el resultado depende de una hipótesis no validada.

## Failure modes mínimos

Cada skill debe declarar qué hace cuando:

- falta contexto;
- no encuentra evidencia;
- encuentra evidencia contradictoria;
- la petición está fuera de scope;
- existe riesgo alto;
- otra skill es prerequisite.

## Especialización industrial B2B

Cada skill debe revisar si la metodología contempla correctamente factores industriales relevantes. No añadir factores solo para parecer sectorial.

## Referencias

Mover metodología extensa, tablas, ejemplos y taxonomías a `references/` para mantener `SKILL.md` operativo y legible.

## Tests

Las skills se evaluarán por propiedades, no por redacción exacta.

Ejemplos:

- una skill de distribuidores no debe recomendar con alta confianza si no existe evidencia de acceso al cliente;
- una skill de mercados debe separar atractivo y capacidad de ganar;
- una skill de cuentas no debe presentar necesidad como hecho sin evidencia.

## Criterio de rechazo

Una skill se rechaza si es esencialmente un prompt largo sin:

- contrato;
- dependencias;
- metodología verificable;
- failure modes;
- criterios de calidad.
