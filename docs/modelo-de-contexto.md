# Modelo de contexto

## Objetivo

Definir cómo debe representarse la información de empresa para que el agente trabaje con contexto fiable sin mezclar hechos, preferencias, estrategia, research y aprendizaje provisional.

## Capas de contexto

### 1. Verdad de empresa
Información validada sobre la organización:

- empresa y estructura;
- productos y servicios;
- aplicaciones;
- capacidades;
- clientes y segmentos actuales;
- mercados actuales;
- canales;
- restricciones;
- claims aprobados.

### 2. Estrategia
Decisiones y orientaciones aprobadas:

- mercados prioritarios;
- segmentos;
- modelo de entrada;
- posicionamiento;
- criterios de inversión;
- prioridades comerciales.

### 3. Objetivo actual
La decisión activa que el usuario intenta resolver.

Debe poder cambiar sin reescribir la verdad de empresa.

### 4. Marca y comunicación
Preferencias de expresión y terminología:

- voz;
- tono;
- formalidad;
- nivel técnico;
- idiomas;
- terminología aprobada;
- expresiones a evitar;
- ejemplos de comunicación.

### 5. Governance y aprobaciones
Qué elementos requieren validación y quién debe aprobarlos.

### 6. Research externo
Información obtenida fuera de la empresa. Nunca debe mezclarse automáticamente con verdad de empresa.

### 7. Memoria de decisiones
Decisiones tomadas, hipótesis, aprendizajes y experimentos.

## Estados de información

Toda información material debe poder clasificarse conceptualmente como:

- `CONFIRMADO`;
- `INFERIDO`;
- `HIPOTESIS`;
- `SUPUESTO`;
- `PENDIENTE_DE_VALIDAR`;
- `OBSOLETO`.

## Reglas de escritura

Puede escribirse como contexto confirmado cuando:

- el usuario lo declara explícitamente como hecho;
- aparece en documentación interna autorizada y no contradictoria;
- un responsable humano lo valida.

No debe guardarse como confirmado cuando procede únicamente de:

- una inferencia del modelo;
- una fuente externa;
- un directorio comercial;
- una noticia;
- un análisis competitivo;
- una única conversación no validada.

## Conflictos

Si dos fuentes internas se contradicen:

1. no elegir una silenciosamente;
2. registrar el conflicto;
3. identificar la fecha y procedencia;
4. pedir resolución humana cuando sea material.

## Frescura

Algunos elementos se vuelven obsoletos rápidamente:

- precios;
- capacidad;
- distribuidores activos;
- mercados prioritarios;
- responsables;
- claims;
- certificaciones;
- objetivos.

El modelo de contexto de Fase 2 deberá permitir registrar fecha de revisión cuando sea relevante.

## Privacidad

El repositorio público contendrá plantillas, nunca información real de clientes.

Las implementaciones locales deben evitar guardar:

- contraseñas;
- tokens;
- credenciales;
- datos personales no necesarios;
- secretos comerciales innecesarios para la tarea.

## Principio de diseño

**La memoria útil no es recordar más; es recordar únicamente información con procedencia, estado y relevancia claros.**
