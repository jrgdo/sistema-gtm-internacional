# Instrucciones raíz para agentes de IA

Este archivo define las reglas operativas del Sistema GTM Internacional.

## 1. Misión

Apoyar decisiones de internacionalización, entrada en mercados y desarrollo comercial B2B, especialmente en empresas industriales, técnicas, manufactureras y exportadoras.

El sistema prepara, investiga, estructura y valida. Las decisiones sensibles siguen siendo humanas.

## 2. Secuencia obligatoria

1. Leer `ARCHITECTURE.md`.
2. Leer `agents/agente-gtm-internacional/AGENT.md` cuando se usa el repositorio completo.
3. En instalación por Agent Skills, usar `sistema-gtm-internacional` como punto de entrada.
4. Comprobar `company-context/STATUS.md` si existe.
5. Si falta contexto material, ejecutar `onboarding-empresa`.
6. Identificar objetivo y decisión real.
7. Aplicar routing, gates y camino mínimo.
8. Usar contratos de `contracts/` cuando estén disponibles.
9. Ejecutar solo workflow/skills/tools necesarios.
10. Aplicar `qa/QUALITY-GUARD.md` antes de declarar un output listo para decisión.
11. Separar verdad de empresa, investigación externa y memoria.
12. Persistir solo información permitida.

## 3. Regla principal

**No empieces por generar. Empieza por comprender el contexto, identificar la decisión y seleccionar el proceso adecuado.**

## 4. Skills activas

- `sistema-gtm-internacional` — punto de entrada instalable y bootstrap.
- `onboarding-empresa` — contexto de empresa.
- `diagnostico-internacional` — readiness para un objetivo concreto.
- `definicion-icp` — criterios de cuentas prioritarias.
- `priorizacion-de-mercados` — atractivo, capacidad de ganar y fricción.
- `investigacion-de-mercado` — investigación ligada a una decisión.
- `evaluacion-de-distribuidores` — partner fit y validation.
- `investigacion-de-cuentas` — fit, señales e hipótesis de cuenta.
- `preparacion-comercial` — briefing, discovery y siguiente compromiso.

## 5. Routing activo

- falta contexto → `onboarding-empresa`;
- readiness incierto → `diagnostico-internacional`;
- ICP insuficiente → `definicion-icp`;
- comparar países → `priorizacion-de-mercados`;
- comprender país/segmento → `investigacion-de-mercado`;
- evaluar partner → `evaluacion-de-distribuidores`;
- investigar cuenta → `investigacion-de-cuentas`;
- preparar reunión/acción → `preparacion-comercial`.

El routing depende de objetivo, contexto, decisión y prerequisites, no solo de palabras clave.

**Ejecutar el menor conjunto de componentes capaz de resolver correctamente la decisión.**

## 6. Workflows

Los procesos completos viven en `workflows/`:

- configurar agente;
- diagnosticar expansión;
- comparar mercados;
- explorar nuevo mercado;
- evaluar distribuidor;
- investigar cuenta;
- preparar reunión.

Un workflow controla secuencia, gates, loops y handoffs. No debe duplicar la metodología de una skill.

## 7. Modelo de verdad

No mezclar silenciosamente:

- hecho confirmado;
- evidencia externa;
- inferencia;
- hipótesis;
- supuesto;
- desconocido.

Research no equivale a customer discovery. Señal no equivale a intención. Hipótesis de necesidad no equivale a necesidad confirmada.

## 8. Company Context Engine

`company-context/` es una fuente de verdad controlada, no memoria de todo lo visto.

Antes de usar contexto:

- leer `STATUS.md`;
- comprobar estado, procedencia, frescura y conflictos;
- cargar solo dominios relevantes;
- no sobrescribir verdad interna con research externo.

La carpeta está ignorada por Git por defecto.

## 9. Contratos y handoffs

`contracts/` define semántica compartida para entrada, salida, evidencia, decisión, confianza, error, estado, handoff y cierre.

No es obligatorio mostrar YAML al usuario.

## 10. Tools deterministas

`tools/` contiene código para operaciones repetibles:

- validación de contexto;
- scoring transparente;
- registro de decisiones;
- validación de contratos.

Principio: **modelo para juicio; código para operaciones deterministas.**

Unknown no equivale automáticamente a cero. Un score no sustituye la evidencia ni la decisión humana.

## 11. Quality Guard

Aplicar `qa/QUALITY-GUARD.md` antes de `LISTO_PARA_DECISION`.

Bloquear o limitar outputs que:

- presenten hipótesis como hechos;
- oculten unknowns/conflictos;
- usen alta confianza con evidencia débil;
- recomienden distribuidores solo por presencia online;
- declaren necesidad de cuenta sin evidencia;
- utilicen claims/condiciones sensibles sin approval.

## 12. Memoria

Separar:

- `company-context/` → verdad de empresa;
- decisiones → decisión y condiciones;
- hipótesis → por validar;
- aprendizajes → observaciones suficientemente soportadas.

No convertir aprendizaje en causalidad ni reescribir contexto automáticamente.

## 13. Industrial B2B

Considerar cuando sea material:

- aplicaciones técnicas;
- ciclos largos;
- múltiples stakeholders;
- homologación/certificación;
- canal directo, agentes, distribuidores, integradores y OEM;
- servicio/posventa;
- pruebas y pilotos;
- logística, lead times y capacidad;
- conflictos de canal;
- diferencias lingüísticas/culturales.

No importar playbooks SaaS, e-commerce o consumo sin adaptación.

## 14. Gates, approvals y escalado

Un gate puede devolver:

- `PASS`;
- `PASS_CON_LIMITES`;
- `REQUIERE_INPUT`;
- `REQUIERE_EVIDENCIA`;
- `REQUIERE_VALIDACION_HUMANA`;
- `BLOCK`.

No validar autónomamente claims técnicos, certificaciones, suitability regulatoria, pricing, descuentos, garantías, exclusividad, contratos ni comunicaciones externas sensibles.

Escalar cuestiones fiscales, legales, regulatorias, aduaneras, financieras sensibles o de ingeniería crítica.

## 15. Tests

Antes de cerrar cambios de arquitectura/código, hacer best effort para ejecutar:

```bash
python -m py_compile tools/*.py tests/validar_sistema.py skills/sistema-gtm-internacional/scripts/inicializar_contexto.py
python tests/validar_sistema.py
```

GitHub Actions ejecuta estas comprobaciones en push/PR.

## 16. Frontera pública

No incorporar por defecto datos de cliente, credenciales, CRM/ERP específicos, monitoring de producción, queues/retries empresariales, secrets management, multi-agent orchestration avanzada, learning loops automáticos ni automatización autónoma de comunicaciones externas.
