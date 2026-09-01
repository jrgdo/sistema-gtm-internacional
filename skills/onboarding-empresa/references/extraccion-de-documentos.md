# Protocolo de extracción de documentos

## Objetivo

Extraer contexto útil de documentos de empresa sin confundir lenguaje promocional, inferencias o información antigua con verdad operativa.

## 1. Inventario inicial

Antes de extraer contenido, identificar:

- tipo de documento;
- fecha o versión si existe;
- propietario o área responsable si se conoce;
- propósito original;
- dominios de contexto que puede informar;
- posibles limitaciones.

Ejemplos de documentos:

- catálogo;
- ficha técnica;
- presentación comercial;
- plan estratégico;
- manual de marca;
- lista de precios;
- CRM export;
- acta de dirección;
- documentación regulatoria;
- web corporativa.

## 2. Jerarquía contextual

No todas las fuentes tienen la misma autoridad para todas las preguntas.

Ejemplos:

- ficha técnica aprobada > copy comercial para especificaciones;
- decisión reciente de dirección > plan estratégico antiguo para prioridades;
- CRM actualizado > presentación antigua para actividad comercial;
- brand guide > ejemplos aislados para voz oficial.

La autoridad depende del dato, no del prestigio general del documento.

## 3. Extracción por afirmaciones

Extraer afirmaciones concretas, no resúmenes vagos.

Para cada afirmación material identificar cuando sea posible:

- contenido;
- fuente;
- fecha/versión;
- dominio;
- estado candidato;
- necesidad de validación.

## 4. No elevar automáticamente lenguaje promocional

Frases como:

- "líder del mercado";
- "máxima calidad";
- "solución innovadora";
- "reduce costes";
- "mejora la productividad";

no deben convertirse en hechos técnicos o comerciales salvo evidencia adecuada.

Clasificar como mensaje de marketing o claim pendiente de validación cuando corresponda.

## 5. Certificaciones y regulación

No inferir certificaciones, homologaciones o aptitud regulatoria porque un producto parezca similar a otro.

Registrar únicamente lo explícitamente soportado y señalar alcance geográfico o de producto cuando sea material.

## 6. Clientes y referencias

Una lista de clientes demuestra relación o experiencia solo en el alcance realmente soportado.

No inferir automáticamente:

- satisfacción;
- resultados;
- recurrencia;
- tamaño de contrato;
- permiso para uso público de referencia.

## 7. Estrategia

Distinguir:

- estrategia oficialmente aprobada;
- intención expresada;
- prioridad histórica;
- propuesta del documento;
- hipótesis del equipo.

No tratar una presentación exploratoria como decisión de dirección.

## 8. Frescura

Si un dato puede haber cambiado materialmente, registrar necesidad de revisión.

Especial atención a:

- pricing;
- lead times;
- capacidad;
- disponibilidad;
- distribuidores;
- territorios;
- exclusividades;
- prioridades;
- personas responsables;
- pipeline.

## 9. Conflictos

Cuando dos documentos discrepen:

1. conservar ambas afirmaciones;
2. identificar fecha, autoridad y propósito;
3. marcar `CONFLICTO` si afecta la decisión;
4. no resolverlo solo por recencia si la fuente reciente no tiene autoridad suficiente;
5. pedir validación cuando sea material.

## 10. Resultado de extracción

La extracción debe producir un mapa como:

```yaml
fuente:
fecha_o_version:
dominios_cubiertos: []
afirmaciones_confirmables: []
elementos_pendientes: []
claims_sensibles: []
conflictos: []
gaps_detectados: []
```

## 11. Principio

**Extraer no significa aceptar. La extracción crea candidatos de contexto; la política de escritura decide qué puede convertirse en verdad operativa.**