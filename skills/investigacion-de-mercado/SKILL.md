---
name: investigacion-de-mercado
description: Investiga un mercado, país, segmento o aplicación para apoyar una decisión GTM internacional concreta. Úsala cuando la empresa ya ha definido qué quiere decidir y necesita evidencia externa sobre demanda, estructura de compradores, competencia, canal, regulación, barreras, aplicaciones, señales y riesgos. No usar para generar informes genéricos de país ni para sustituir priorización de mercados.
---

# Investigación de mercado

## 1. Propósito

Producir inteligencia de mercado orientada a una decisión concreta de internacionalización o entrada en mercado B2B industrial.

Esta skill no genera un informe enciclopédico. Investiga únicamente lo necesario para reducir incertidumbre sobre una decisión explícita.

## 2. Cuándo usarla

Usar cuando exista una pregunta como:

- ¿qué necesitamos saber de Francia antes de invertir recursos?;
- ¿qué segmentos industriales parecen más relevantes para esta aplicación?;
- ¿cómo está estructurado el canal en este mercado?;
- ¿qué barreras regulatorias o comerciales pueden cambiar la decisión?;
- ¿qué competidores, alternativas o patrones de compra debemos validar?;
- ¿qué evidencia adicional necesitamos antes de priorizar o ejecutar?

## 3. Cuándo no usarla

No usar para:

- comparar países sin criterios de priorización;
- decidir ICP sin contexto suficiente;
- evaluar un distribuidor concreto;
- investigar una cuenta específica;
- producir un country report genérico;
- inferir demanda a partir de una sola métrica macroeconómica;
- presentar una señal de mercado como prueba de oportunidad comercial.

## 4. Decisión que soporta

Debe responder una pregunta del tipo:

> ¿Qué evidencia externa necesitamos y qué indica esa evidencia sobre la decisión GTM actual?

## 5. Inputs requeridos

- objetivo o decisión explícita;
- producto/servicio o línea prioritaria;
- aplicación o caso de uso relevante;
- ICP o hipótesis de comprador suficientemente definida;
- mercado, geografía o segmento a investigar;
- restricciones materiales conocidas.

Si falta alguno de los fundamentos que cambian la investigación, devolver `INPUT_INSUFICIENTE` o enrutar upstream.

## 6. Inputs opcionales

- mercados comparables;
- competidores conocidos;
- clientes o referencias existentes;
- canal actual;
- criterios regulatorios conocidos;
- hipótesis previas;
- fuentes internas;
- idioma o región subnacional.

## 7. Dependencias

Leer y respetar:

- `AGENTS.md`;
- `agents/agente-gtm-internacional/AGENT.md`;
- `docs/modelo-de-evidencia.md`;
- `docs/contratos-compartidos.md`;
- `contracts/entrada-componente.yaml`;
- `contracts/salida-componente.yaml`;
- `contracts/evidencia.yaml`;
- `contracts/confianza.yaml`.

## 8. Requisitos de evidencia

Priorizar, según la afirmación:

1. fuentes oficiales y regulatorias;
2. fuentes sectoriales primarias;
3. asociaciones profesionales;
4. webs y documentación de empresas relevantes;
5. datos comerciales o industriales fiables;
6. fuentes secundarias especializadas;
7. prensa y señales públicas cuando aporten contexto;
8. fuentes agregadas o directorios solo como apoyo, nunca como prueba suficiente por sí solos.

Registrar cuando sea material:

- fuente;
- fecha;
- geografía;
- alcance;
- naturaleza de la evidencia;
- limitaciones;
- nivel de confianza.

## 9. Método

### Paso 1 — Reformular la decisión

Convertir la petición en una pregunta investigable y acotada.

Ejemplo:

Mal: `Analiza Alemania`.

Mejor: `Determinar si el segmento de fabricantes de maquinaria alimentaria en Alemania justifica una validación comercial durante los próximos 6 meses para la línea X.`

### Paso 2 — Definir hipótesis de investigación

Separar:

- lo que ya sabemos;
- lo que creemos;
- lo que necesitamos validar;
- qué hallazgo podría cambiar la decisión.

### Paso 3 — Construir plan de evidencia

Seleccionar únicamente bloques relevantes, por ejemplo:

- tamaño y estructura del segmento;
- aplicaciones;
- base de compradores;
- concentración geográfica;
- patrones de canal;
- competencia y sustitutos;
- regulación/homologación;
- barreras de entrada;
- service requirements;
- señales de inversión o demanda;
- ferias/asociaciones relevantes;
- sensibilidad a precio, lead time o soporte cuando exista evidencia.

No investigar todos los bloques por defecto.

### Paso 4 — Investigar de fuera hacia dentro

Empezar por evidencia estructural y primaria, luego profundizar en señales comerciales.

Evitar empezar por directorios de empresas y construir una narrativa desde ellos.

### Paso 5 — Triangular

Para afirmaciones materiales, contrastar más de una evidencia cuando sea razonable.

Una cifra aislada, un artículo promocional o una landing page no bastan para una conclusión fuerte.

### Paso 6 — Clasificar hallazgos

Separar explícitamente:

- hechos observados;
- inferencias;
- hipótesis;
- unknowns;
- evidencia contradictoria.

### Paso 7 — Traducir evidencia a implicación GTM

Por cada hallazgo material, responder:

- ¿por qué importa para nuestra decisión?;
- ¿favorece, limita o no cambia la hipótesis?;
- ¿qué falta validar en campo?;
- ¿qué no puede concluirse todavía?

### Paso 8 — Recomendar siguiente validación

La salida debe priorizar qué validar después, no fingir que research de escritorio equivale a customer discovery.

## 10. Reglas de decisión

La skill puede devolver:

- `EVIDENCIA_SUFICIENTE_PARA_AVANZAR`;
- `EVIDENCIA_PARCIAL`;
- `REQUIERE_INVESTIGACION_ADICIONAL`;
- `REQUIERE_VALIDACION_EN_CAMPO`;
- `EVIDENCIA_CONTRADICTORIA`;
- `INPUT_INSUFICIENTE`.

Nunca devolver “mercado validado” únicamente por research secundario.

## 11. Contrato de salida

Seguir `contracts/salida-componente.yaml` y, conceptualmente, incluir:

```yaml
objetivo:
decision:
mercado_o_segmento:
hechos:
inferencias:
hipotesis:
desconocidos:
evidencia:
hallazgos_clave:
implicaciones_gtm:
riesgos:
confianza:
validacion_necesaria:
siguiente_accion:
handoff_recomendado:
```

## 12. Confianza

Alta confianza requiere:

- fuentes adecuadas a la afirmación;
- evidencia relativamente reciente cuando la frescura sea material;
- triangulación suficiente;
- ausencia de contradicciones no resueltas;
- buena cobertura de las variables que realmente cambian la decisión.

No usar alta confianza para hipótesis de intención de compra, prioridad de cliente o necesidad no observada.

## 13. Failure modes

### Datos de mercado abundantes pero irrelevantes

Reducir al scope de la decisión.

### Solo existen fuentes secundarias

Usarlas con confianza limitada y señalar la limitación.

### Evidencia contradictoria

No elegir silenciosamente; mostrar qué cambia según cada escenario.

### Regulación compleja

Preparar evidencia y preguntas, pero escalar a experto regulatorio cuando la interpretación sea material.

### Señales sin causalidad

No convertir inversiones, empleo, noticias o expansión sectorial en demanda confirmada para la oferta.

### Research web sin validación comercial

Declarar explícitamente que desk research no sustituye entrevistas, pruebas, distribuidores o conversaciones con compradores.

## 14. Handoffs

- evidencia suficiente para comparar países → `priorizacion-de-mercados`;
- mercado atractivo pero canal incierto → futura `evaluacion-de-distribuidores` o workflow de entrada;
- ICP cuestionado por evidencia → `definicion-icp`;
- readiness interno insuficiente → `diagnostico-internacional`;
- necesidad de validación comercial → workflow futuro de market validation.

## 15. Aprobación humana

Requiere revisión humana para:

- conclusiones regulatorias materiales;
- recomendaciones de inversión relevantes;
- claims de market fit;
- cambios de estrategia derivados de evidencia ambigua;
- interpretación de datos confidenciales o contractuales.

## 16. Persistencia

No escribir research externo directamente en `company-context/` como verdad de empresa.

Los hallazgos futuros deberán vivir en memoria/evidencia cuando esa capa exista o permanecer en el entregable de investigación.

## 17. Anti-patrones

- country report genérico;
- ranking sin decisión;
- usar PIB como proxy suficiente de oportunidad;
- tratar importaciones totales como demanda accesible;
- inferir necesidad desde crecimiento sectorial;
- confundir número de empresas con mercado servible;
- listar competidores sin analizar implicación;
- asumir que presencia de distribuidores implica canal adecuado;
- afirmar regulatory fit sin validación especializada;
- ocultar fuentes débiles tras lenguaje convincente.

## 18. Definition of Done

La investigación termina cuando reduce una incertidumbre concreta y deja claro:

1. qué sabemos;
2. qué creemos;
3. qué no sabemos;
4. qué evidencia cambia la decisión;
5. qué debemos validar después.
