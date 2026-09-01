# Contratos compartidos

Esta carpeta define el lenguaje común entre el Agente GTM Internacional, las skills, los workflows y las tools.

Los contratos sirven para:

- reducir ambigüedad entre componentes;
- hacer explícitos objetivo, decisión, evidencia, gaps y approvals;
- permitir handoffs consistentes;
- preparar validación determinista en fases posteriores;
- separar estructura interna de presentación al usuario.

## Principio

Los contratos son **semánticos y operativos**. No obligan a mostrar YAML o JSON al usuario final.

Una respuesta puede ser natural y breve, pero internamente debe conservar la información necesaria para que el siguiente componente pueda trabajar sin reinterpretar toda la conversación.

## Contratos iniciales

- `entrada-componente.yaml`: input estándar para skill, workflow o tool.
- `salida-componente.yaml`: resultado estándar de un componente.
- `handoff.yaml`: transferencia entre componentes.
- `cierre-ejecucion.yaml`: resumen de cierre coordinado.
- `evidencia.yaml`: estructura de evidencia.
- `decision.yaml`: estructura de decisión preparada.
- `error-operativo.yaml`: errores, bloqueos y estados no exitosos.
- `estados.yaml`: vocabulario compartido de estados.
- `confianza.yaml`: niveles y reglas de confianza.

## Reglas

1. No rellenar campos desconocidos con contenido plausible.
2. Usar `null`, listas vacías o estado explícito cuando algo no esté disponible.
3. No promover inferencias o hipótesis a hechos.
4. Mantener los campos mínimos necesarios; evitar payloads gigantes.
5. Un componente downstream debe poder entender el resultado upstream sin reabrir todo el contexto.
6. La versión visible al usuario puede ocultar detalles internos que no aporten valor.
7. En Fase 8 estos contratos podrán convertirse en schemas validables por código.
