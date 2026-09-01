# Política de escritura del contexto de empresa

## 1. Propósito

Evitar que el agente convierta investigación, inferencias o generación probabilística en verdad operativa de empresa.

El contexto debe ser útil, trazable y suficientemente fiable para apoyar decisiones comerciales reales.

## 2. Qué puede incorporarse como información confirmada

Puede registrarse como confirmada cuando procede de:

- una afirmación explícita de un responsable autorizado;
- documentación interna vigente;
- catálogo, ficha técnica, contrato, política o registro oficial de la empresa;
- dato de sistema interno cuya procedencia sea clara;
- fuente externa autorizada específicamente para un dato factual público de la propia empresa, siempre que no contradiga información interna más fiable.

## 3. Qué no puede convertirse automáticamente en verdad

- inferencias del modelo;
- hipótesis comerciales;
- investigación web sobre necesidades o intenciones de clientes;
- conclusiones obtenidas de una única señal débil;
- contenido promocional no validado como evidencia técnica;
- información de terceros no contrastada;
- datos antiguos cuya vigencia sea material;
- borradores generados por IA.

Estos elementos pueden conservarse en espacios de hipótesis o investigación en fases posteriores, pero no deben contaminar `company-context/` como hechos confirmados.

## 4. Estados conceptuales de información

- `CONFIRMADO`: respaldado y apto para el uso definido.
- `INFERIDO`: conclusión razonable, todavía no validada como hecho.
- `HIPOTESIS`: posibilidad que debe contrastarse.
- `PENDIENTE_DE_VALIDAR`: información candidata con validación explícita pendiente.
- `OBSOLETO`: anteriormente válido pero ya no suficientemente vigente.
- `CONFLICTO`: dos o más fuentes relevantes no coinciden.

Los archivos de contexto usan estados de dominio simplificados, mientras que estas categorías gobiernan la naturaleza de la información dentro del dominio.

## 5. Jerarquía orientativa de procedencia

Para verdad interna de empresa, preferir:

1. fuente interna autorizada y vigente;
2. registro o sistema operativo de la empresa;
3. documentación técnica/comercial aprobada;
4. declaración explícita de un responsable;
5. fuente externa primaria sobre la propia empresa;
6. fuente secundaria;
7. inferencia del modelo.

Esta jerarquía es orientativa: una fuente más formal pero obsoleta puede ser menos útil que una decisión reciente de dirección debidamente confirmada.

## 6. Actualización

Antes de sobrescribir información existente:

1. identificar el dato afectado;
2. comprobar estado y fuente anterior;
3. evaluar si el nuevo dato es más reciente y autorizado;
4. detectar posibles conflictos;
5. preservar la trazabilidad material;
6. actualizar `STATUS.md` cuando cambie la confiabilidad de un dominio.

Nunca sobrescribir silenciosamente una decisión estratégica confirmada a partir de investigación externa.

## 7. Minimización de datos

Guardar solo información necesaria para el propósito GTM.

No guardar por defecto:

- contraseñas, tokens o credenciales;
- datos personales sensibles;
- información personal irrelevante de compradores;
- documentación confidencial completa si basta un resumen autorizado;
- datos cuya retención no tenga una finalidad clara.

## 8. Principio operativo

**El contexto es una fuente de verdad controlada, no una memoria de todo lo que el modelo ha visto.**
