# Sistema GTM Internacional

Agente de IA personalizable para apoyar decisiones de internacionalización, entrada en mercados y desarrollo comercial B2B.

Diseñado especialmente para empresas industriales españolas que están empezando a exportar o que ya operan internacionalmente y necesitan estructurar mejor su investigación, priorización y preparación comercial con IA.

> **La IA prepara. El equipo valida. Las decisiones importantes siguen siendo humanas.**

## Estado del proyecto

Este repositorio está en construcción por fases. La Fase 1 define la constitución técnica, los principios y las convenciones que deberán cumplir todos los agentes, skills, workflows y tools futuros.

Todavía no se considera una implementación GTM completa.

## Principios

- No generar antes de comprender el contexto y la decisión.
- No inventar información de empresa, mercado, cliente o producto.
- Separar hechos, evidencia, inferencias, hipótesis, supuestos y desconocidos.
- Priorizar decisiones comerciales concretas frente a informes genéricos.
- Usar IA para juicio y síntesis; usar código para cálculos, validaciones y operaciones deterministas.
- Mantener aprobación humana en decisiones, claims y compromisos sensibles.
- Diseñar para empresas industriales B2B, no reutilizar playbooks SaaS sin adaptación.
- Mantener separada la verdad de empresa de la investigación externa y del aprendizaje provisional.

## Arquitectura prevista

```text
USUARIO
  ↓
INSTRUCCIONES DEL REPOSITORIO
  ↓
AGENTE GTM INTERNACIONAL
  ↓
WORKFLOW ADECUADO
  ↓
SKILLS ESPECIALIZADAS
  ↓
TOOLS DETERMINISTAS CUANDO APLIQUE
  ↓
VALIDACIÓN DE EVIDENCIA Y APROBACIÓN
  ↓
DECISIÓN HUMANA
  ↓
MEMORIA VALIDADA
```

La arquitectura completa está documentada en [`ARCHITECTURE.md`](ARCHITECTURE.md).

## Para asistentes de IA

Antes de realizar trabajo GTM:

1. Lee `AGENTS.md`.
2. Lee `ARCHITECTURE.md`.
3. Si utilizas Claude Code, lee además `CLAUDE.md`.
4. Si utilizas Codex, lee además `CODEX.md`.
5. No asumas que existe contexto de empresa hasta verificarlo.
6. No crees nuevos métodos si ya existe una convención o componente adecuado en el repositorio.

## Alcance previsto del producto gratuito

El sistema está diseñado para evolucionar hacia capacidades como:

- onboarding de empresa;
- diagnóstico de preparación internacional;
- definición y revisión de ICP;
- priorización de mercados;
- investigación orientada a decisiones;
- evaluación de distribuidores;
- investigación de cuentas objetivo;
- preparación comercial.

La automatización de producción, integraciones empresariales y personalizaciones avanzadas requieren arquitectura adicional y no forman parte del alcance base de este repositorio.

## Idioma

La documentación del repositorio, las instrucciones y los componentes públicos se escriben en español. Los análisis para mercados internacionales podrán trabajar con fuentes y materiales en otros idiomas cuando sea necesario.
