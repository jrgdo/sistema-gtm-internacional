---
name: sistema-gtm-internacional
description: Punto de entrada del Sistema GTM Internacional. Coordina onboarding, diagnóstico, ICP, mercados, investigación, distribuidores, cuentas y preparación comercial usando contexto de empresa, evidencia, gates y aprobación humana. Úsala al configurar el sistema, decidir qué skill ejecutar o trabajar con varias capacidades GTM conectadas.
---

# Sistema GTM Internacional

## Rol

Esta skill es el punto de entrada instalable del sistema. No sustituye las skills especialistas: decide cuál usar, valida contexto y aplica camino mínimo.

## Primera ejecución

1. Comprobar si existe `company-context/STATUS.md` en el proyecto actual.
2. Si no existe, crear el workspace mediante `scripts/inicializar_contexto.py` cuando se pueda ejecutar código local, o crear manualmente la estructura indicada por el script.
3. Ejecutar `onboarding-empresa` para completar únicamente contexto relevante y validado.
4. No generar estrategia genérica como sustituto del onboarding.

## Routing activo

- falta contexto → `onboarding-empresa`;
- readiness incierto → `diagnostico-internacional`;
- ICP insuficiente → `definicion-icp`;
- comparar países → `priorizacion-de-mercados`;
- investigar país/segmento → `investigacion-de-mercado`;
- evaluar partner → `evaluacion-de-distribuidores`;
- investigar cuenta → `investigacion-de-cuentas`;
- preparar reunión/acción → `preparacion-comercial`.

## Camino mínimo

Ejecutar el menor conjunto de skills capaz de resolver correctamente la decisión. No lanzar toda la cadena por defecto.

## Reglas de verdad

Separar siempre:

- hechos confirmados;
- evidencia externa;
- inferencias;
- hipótesis;
- supuestos;
- desconocidos.

Research no equivale a customer discovery. Una señal no equivale a intención. Una hipótesis de necesidad no equivale a necesidad confirmada.

## Gates

Detener o limitar cuando falte contexto material, exista conflicto, la evidencia sea insuficiente o se requiera aprobación humana.

Escalar cuestiones fiscales, legales, regulatorias, aduaneras, financieras sensibles o de ingeniería crítica.

## Aprobación humana

No aprobar autónomamente claims técnicos, certificaciones, suitability regulatoria, pricing, descuentos, garantías, exclusividad, compromisos contractuales ni comunicaciones externas sensibles.

## Contexto local

`company-context/` es verdad operativa controlada, no memoria de todo lo observado. La investigación externa no debe sobrescribirla automáticamente.

## Compatibilidad

Esta skill está diseñada como punto de entrada cuando el repositorio se instala mediante un gestor compatible con Agent Skills. El repositorio completo contiene además arquitectura, workflows, tools, tests y documentación para builders.
