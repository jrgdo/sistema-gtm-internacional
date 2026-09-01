# Contribuir

Gracias por mejorar el Sistema GTM Internacional.

## Qué buscamos

Contribuciones que mejoren decisiones reales de internacionalización y GTM industrial B2B:

- casos límite;
- mejoras de metodología;
- nuevas fuentes o criterios;
- tests;
- correcciones de routing/gates;
- tools deterministas;
- documentación y ejemplos.

## Antes de proponer una nueva skill

Explica:

1. qué decisión soporta;
2. quién toma esa decisión;
3. inputs mínimos;
4. dónde falla hoy el proceso;
5. qué output necesita el siguiente paso;
6. qué debe seguir siendo decisión humana;
7. por qué no puede resolverse ampliando una skill existente.

Una skill no se acepta si es esencialmente un prompt largo sin contrato, metodología, failure modes ni evaluación.

## Calidad

Antes de proponer cambios:

```bash
python -m py_compile tools/*.py tests/validar_sistema.py skills/sistema-gtm-internacional/scripts/inicializar_contexto.py
python tests/validar_sistema.py
```

## Datos

Nunca incluir datos reales de clientes, credenciales, exports de CRM, contratos privados ni información personal innecesaria.

Los ejemplos deben ser ficticios, anonimizados o explícitamente públicos y apropiados para reutilización.
