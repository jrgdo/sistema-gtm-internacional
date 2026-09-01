# Checklist de release pública

## Arquitectura

- [x] instrucciones raíz sincronizadas;
- [x] agente coordinador implementado;
- [x] contracts compartidos;
- [x] workflows básicos;
- [x] skills estratégicas y comerciales;
- [x] tools deterministas;
- [x] Quality Guard;
- [x] memoria separada de contexto.

## Instalación

- [x] skill `sistema-gtm-internacional` como punto de entrada instalable;
- [x] bootstrap de `company-context/`;
- [x] instalación rápida documentada;
- [x] clone completo documentado;
- [x] protección `.gitignore` para datos reales.

## Calidad

- [x] escenarios de evaluación en skills/agente clave;
- [x] smoke test de estructura;
- [x] compilación Python en CI;
- [x] GitHub Actions en push/PR;
- [x] reglas de approvals/escalado;
- [x] ejemplo ficticio.

## Antes de etiquetar una versión

- [ ] comprobar que CI está verde;
- [ ] probar instalación con el CLI de Skills en entorno limpio;
- [ ] probar primera ejecución en al menos Codex y Claude Code;
- [ ] verificar que `company-context/` no se versiona;
- [ ] revisar links del README;
- [ ] revisar lista de skills detectadas por el CLI;
- [ ] registrar limitaciones conocidas;
- [ ] elegir y añadir licencia antes de promover reutilización si el propietario del repo lo decide.

## Criterio

No publicar una versión estable únicamente porque el repositorio “se ve completo”. La release debe superar instalación, primera ejecución y al menos un workflow end-to-end.
