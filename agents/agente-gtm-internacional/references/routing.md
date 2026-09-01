# Routing del Agente GTM Internacional

## Principio

El routing debe basarse en **objetivo + decisión + contexto + dependencias**, no solo en palabras clave.

## Árbol inicial

```text
PETICIÓN
  ↓
¿Existe contexto suficiente para esta decisión?
  ├─ NO → onboarding-empresa
  └─ SÍ
       ↓
¿La decisión está suficientemente clara?
  ├─ NO → REQUIERE_CLARIFICACION
  └─ SÍ
       ↓
¿Existe workflow formalizado?
  ├─ SÍ → ejecutar workflow
  └─ NO
       ↓
¿Existe skill directa adecuada?
  ├─ SÍ → ejecutar skill
  └─ NO → declarar capacidad no formalizada / fuera de scope según corresponda
```

## Mapa de negocio previsto

### Configurar o actualizar empresa
→ `onboarding-empresa`

### Evaluar readiness export/internacional
→ futura `diagnostico-internacional`

### Definir o revisar ICP
→ futura `definicion-icp`

### Decidir entre países o mercados
→ futura `priorizacion-de-mercados`

### Comprender un mercado específico
→ futura `investigacion-de-mercado`

### Evaluar distribuidor/partner
→ futura `evaluacion-de-distribuidores`

### Preparar una cuenta objetivo
→ futura `investigacion-de-cuentas`

### Preparar una reunión o acción comercial
→ futura `preparacion-comercial`

## Ambigüedad típica

Petición: "Quiero crecer en Alemania".

Posibles decisiones:

- decidir si Alemania merece prioridad;
- investigar el mercado alemán;
- buscar canal;
- evaluar distribuidores;
- construir pipeline de cuentas;
- preparar una acción comercial.

El agente debe usar el contexto existente para reducir ambigüedad y hacer solo la pregunta mínima restante.

## Routing upstream

Si falta una dependencia crítica, volver upstream.

Ejemplos:

- priorización sin ICP suficiente → definir/revisar ICP;
- evaluar distribuidor sin perfil de partner → resolver criterio de partner antes;
- preparación comercial sin cuenta/objetivo → completar investigación o contexto;
- trabajo sensible con claims no aprobados → validación humana.

## Routing downstream

Solo avanzar cuando el output anterior cumple su criterio de finalización.

No usar como trigger suficiente frases como "parece correcto", "probablemente" o "hay bastante información" si faltan campos materiales del contrato.

## Camino mínimo

Si una skill puede resolver correctamente la decisión, no ejecutar un workflow más amplio por defecto.

## Capacidades aún no implementadas

Mientras una capacidad futura no exista, el agente debe decirlo internamente y evitar simular que se ha ejecutado una skill formal inexistente. Puede ofrecer una ayuda limitada basada en las reglas generales del sistema si la tarea es segura, dejando claro el menor nivel de formalización.
