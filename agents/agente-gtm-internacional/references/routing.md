# Routing del Agente GTM Internacional

## Principio

El routing se basa en **objetivo + decisión + contexto + dependencias + etapa**, no solo en palabras clave.

## Árbol inicial

```text
PETICIÓN
  ↓
¿Contexto suficiente para esta decisión?
  ├─ NO → onboarding-empresa
  └─ SÍ
       ↓
¿Decisión suficientemente clara?
  ├─ NO → REQUIERE_CLARIFICACION
  └─ SÍ
       ↓
¿Existe workflow adecuado?
  ├─ SÍ → ejecutar workflow
  └─ NO
       ↓
¿Existe skill directa adecuada?
  ├─ SÍ → ejecutar skill
  └─ NO → ayuda limitada / capacidad no formalizada / FUERA_DE_SCOPE
```

## Routing activo

### Configurar/actualizar empresa
→ `onboarding-empresa`

### Evaluar readiness internacional
→ `diagnostico-internacional`

### Definir/revisar ICP
→ `definicion-icp`

### Comparar países/mercados
→ `priorizacion-de-mercados`

### Comprender mercado/segmento
→ `investigacion-de-mercado`

### Evaluar distribuidor/partner
→ `evaluacion-de-distribuidores`

### Investigar cuenta objetivo
→ `investigacion-de-cuentas`

### Preparar reunión/acción comercial
→ `preparacion-comercial`

## Workflows

Cuando la tarea requiere varias skills/gates:

- configuración → `workflows/configurar-agente/`;
- readiness → `workflows/diagnosticar-expansion/`;
- comparación → `workflows/comparar-mercados/`;
- exploración → `workflows/explorar-nuevo-mercado/`;
- partner → `workflows/evaluar-distribuidor/`;
- cuenta → `workflows/investigar-cuenta/`;
- reunión → `workflows/preparar-reunion/`.

## Ambigüedad típica

“Quiero crecer en Alemania” puede significar priorizar Alemania, investigarla, buscar canal, evaluar partners, construir cuentas o preparar ejecución.

Usar contexto para reducir ambigüedad y hacer solo la pregunta mínima que cambie routing.

## Routing upstream

- priorización sin ICP → `definicion-icp`;
- market research sin pregunta clara → clarificar decisión;
- distribuidor sin perfil de partner → resolver criteria upstream;
- cuenta sin ICP → `definicion-icp`;
- preparación comercial sin contexto de cuenta/partner → investigación correspondiente;
- claims/condiciones sensibles → validation humana.

## Routing downstream

Avanzar solo cuando el output anterior cumple criterio de finalización.

Ejemplos:

- market prioritization → market research cuando existen gaps capaces de cambiar ranking;
- market research → partner evaluation cuando la hipótesis de canal lo justifica;
- account research → preparación comercial cuando hay interacción próxima;
- distributor evaluation → preparación comercial cuando existe reunión o siguiente compromiso.

## Loops

Solo volver a una capacidad anterior con nueva evidencia o cambio material de estado.

No repetir `research → ranking → research` sin progreso.

## Camino mínimo

Si una skill directa resuelve correctamente la decisión, no ejecutar un workflow más amplio.
