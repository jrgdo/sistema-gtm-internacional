---
name: evaluacion-de-distribuidores
description: Evalúa distribuidores, importadores, representantes, agentes o partners comerciales para una empresa B2B industrial, distinguiendo evidencia, señales, gaps y fit con el modelo de canal. Úsala cuando la empresa necesita decidir si un candidato merece avanzar, investigar más, mantener en observación o descartar.
---

# Evaluación de distribuidores

## 1. Propósito

Evaluar candidatos de canal con criterios consistentes y evidencia suficiente para decidir dónde invertir tiempo comercial.

Esta skill no selecciona automáticamente un partner ni sustituye due diligence legal, financiera, técnica o contractual.

## 2. Cuándo usarla

Usar cuando exista un candidato concreto o una shortlist y la decisión sea:

- ¿merece avanzar?;
- ¿qué falta validar?;
- ¿qué riesgos o conflictos existen?;
- ¿cómo se compara con otros candidatos?;
- ¿qué compromiso siguiente debería demostrar antes de hablar de acuerdos mayores?

## 3. Cuándo no usarla

No usar para:

- buscar candidatos desde cero sin criterios de partner;
- definir estrategia de canal completa;
- firmar exclusividad;
- realizar due diligence legal/financiera completa;
- inferir acceso real al cliente por tamaño de web o número de marcas;
- asumir capacidad técnica por autodescripción comercial.

## 4. Decisión que soporta

> ¿Qué nivel de prioridad merece este candidato y qué evidencia adicional necesitamos antes de avanzar?

## 5. Inputs requeridos

- mercado/geografía;
- objetivo de canal;
- ICP o segmento objetivo;
- aplicaciones relevantes;
- perfil de partner deseado;
- criterios mínimos y restricciones;
- candidato identificable.

Si el perfil de partner no está definido y eso cambia la evaluación, devolver `INPUT_INSUFICIENTE` o enrutar upstream.

## 6. Inputs opcionales

- web del candidato;
- portfolio;
- marcas representadas;
- clientes/referencias autorizadas;
- cobertura territorial;
- equipo comercial/técnico;
- capacidad de servicio;
- condiciones propuestas;
- historial de conversaciones;
- pipeline u oportunidades aportadas;
- reporting;
- datos financieros públicos cuando sean apropiados.

## 7. Dependencias

Leer:

- `AGENTS.md`;
- `agents/agente-gtm-internacional/AGENT.md`;
- `docs/modelo-de-evidencia.md`;
- `docs/modelo-de-aprobacion.md`;
- `contracts/entrada-componente.yaml`;
- `contracts/salida-componente.yaml`;
- `contracts/evidencia.yaml`;
- `contracts/confianza.yaml`.

## 8. Dimensiones de evaluación

Evaluar solo dimensiones relevantes, pero considerar como base:

1. encaje sectorial y de aplicación;
2. acceso demostrable al comprador;
3. cobertura geográfica real;
4. capacidad comercial;
5. capacidad técnica y de preventa;
6. servicio/posventa cuando aplique;
7. compatibilidad de portfolio;
8. conflictos de marcas/categorías;
9. prioridad potencial para nuestra oferta;
10. calidad operativa y reporting;
11. capacidad de generar y seguir oportunidades;
12. disposición a asumir un siguiente compromiso verificable.

No otorgar alta valoración a una dimensión sin evidencia proporcional.

## 9. Método

### Paso 1 — Definir qué partner necesitamos

Antes de evaluar al candidato, confirmar:

- qué rol de canal buscamos;
- qué clientes debe alcanzar;
- qué cobertura necesitamos;
- qué soporte técnico/comercial debe aportar;
- qué conflictos son inaceptables.

### Paso 2 — Recopilar evidencia

Separar evidencia pública, evidencia proporcionada por el candidato y evidencia interna de nuestra relación con él.

### Paso 3 — Evaluar fit observable

Para cada dimensión:

- evidencia a favor;
- evidencia en contra;
- desconocidos;
- confianza;
- preguntas de validación.

### Paso 4 — No confundir proxies con prueba

Ejemplos:

- muchas marcas ≠ capacidad de priorizar la nuestra;
- web profesional ≠ acceso al buyer;
- años en el mercado ≠ pipeline relevante;
- equipo técnico declarado ≠ capacidad para nuestra aplicación;
- cobertura nacional declarada ≠ presencia efectiva en todos los territorios.

### Paso 5 — Identificar conflictos y riesgos

Revisar:

- marcas competidoras;
- canibalización;
- concentración excesiva;
- dependencia de una persona;
- cobertura insuficiente;
- falta de soporte;
- reputación o señales públicas relevantes;
- posibles conflictos contractuales o territoriales.

### Paso 6 — Exigir siguiente compromiso

Antes de elevar prioridad, buscar una acción verificable como:

- introducir una cuenta relevante;
- compartir plan de cobertura;
- aportar shortlist de oportunidades;
- participar en una sesión técnica;
- acordar proceso de reporting;
- validar una aplicación concreta.

El compromiso debe ser proporcional a la fase de relación.

### Paso 7 — Clasificar

Resultados posibles:

- `SHORTLIST`;
- `INVESTIGAR`;
- `HOLD`;
- `DESCARTAR`;
- `NO_EVALUABLE`.

No usar `SHORTLIST` si faltan evidencias críticas de acceso, capacidad o conflictos materiales.

## 10. Contrato de salida

Seguir `contracts/salida-componente.yaml` y mantener semántica como:

```yaml
candidato:
mercado:
rol_de_canal:
resultado:
dimensiones:
  - criterio:
    evidencia_a_favor:
    evidencia_en_contra:
    desconocidos:
    confianza:
hechos:
inferencias:
hipotesis:
riesgos:
conflictos:
preguntas_de_validacion:
siguiente_compromiso:
confianza_global:
siguiente_accion:
```

## 11. Confianza

Alta confianza requiere evidencia material sobre las dimensiones críticas.

No declarar alta confianza si:

- acceso al cliente es solo declarado;
- capacidad técnica no está demostrada;
- existen conflictos de portfolio no aclarados;
- cobertura territorial es ambigua;
- el candidato no ha demostrado ningún compromiso verificable.

## 12. Failure modes

### Solo existe información pública

Realizar pre-evaluación y marcar limitaciones. No fingir qualification completa.

### Candidato aporta claims no verificables

Tratar como declaración del candidato, no como hecho confirmado.

### Conflicto de marcas

Analizar materialidad y pedir aclaración; no asumir automáticamente descarte ni compatibilidad.

### Pide exclusividad muy pronto

Escalar a dirección/legal y exigir evidencia antes de recomendar avance contractual.

### Buen fit pero poca evidencia de acceso

Resultado `INVESTIGAR`, no `SHORTLIST` con alta confianza.

### No existe perfil de partner

Enrutar upstream; evaluar sin target profile produce falsos positivos.

## 13. Handoffs

- falta claridad de mercado → `investigacion-de-mercado`;
- falta ICP → `definicion-icp`;
- readiness interno dudoso → `diagnostico-internacional`;
- candidato avanza y hay reunión → futura `preparacion-comercial`;
- requiere análisis contractual/financiero → especialista humano.

## 14. Aprobación humana

Obligatoria para:

- selección final;
- exclusividad;
- territorio;
- pricing especial;
- condiciones comerciales;
- contratos;
- compromisos de soporte o stock;
- descartes basados en información sensible o ambigua.

## 15. Persistencia

La evaluación no debe modificar automáticamente la verdad de empresa.

Una shortlist, hipótesis o evaluación deberá persistirse más adelante en memoria/decision logs cuando esa capa exista.

## 16. Anti-patrones

- recomendar por “buena impresión”;
- usar tamaño de empresa como proxy de acceso;
- asumir que distribuye marcas conocidas = buen fit;
- premiar número de contactos sin evidencia;
- ignorar prioridad dentro del portfolio;
- ignorar conflictos de canal;
- confundir discovery con qualification;
- pedir exclusividad como prueba de compromiso;
- convertir una reunión agradable en evidencia de capacidad.

## 17. Definition of Done

La evaluación termina cuando deja claro:

1. qué evidencia existe;
2. qué dimensiones son fuertes o débiles;
3. qué no sabemos;
4. qué riesgo puede cambiar la decisión;
5. qué compromiso debe demostrar el candidato después;
6. si merece `SHORTLIST`, `INVESTIGAR`, `HOLD`, `DESCARTAR` o `NO_EVALUABLE`.
