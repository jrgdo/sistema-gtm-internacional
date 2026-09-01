# Escenarios de prueba — investigación de mercado

## 1. Petición genérica de país

Usuario: `Analiza Alemania para nosotros.`

Esperado:
- no producir country report;
- pedir o inferir de contexto qué decisión debe soportar;
- si no puede definirse, `INPUT_INSUFICIENTE`.

## 2. Mercado con contexto suficiente

Empresa industrial española, línea y aplicación definidas, objetivo: validar si Francia merece una primera campaña de discovery.

Esperado:
- research acotado a variables que cambian esa decisión;
- evidencia + implicaciones + plan de validación.

## 3. Mucho dato macro, poca relevancia

Esperado:
- no usar PIB/industria total como prueba de oportunidad;
- buscar buyer/application evidence.

## 4. Señal de inversión

Varias plantas anuncian CAPEX.

Esperado:
- tratar como señal;
- no afirmar demanda de nuestra solución.

## 5. Regulación dudosa

Una fuente secundaria afirma que una certificación es obligatoria.

Esperado:
- buscar fuente regulatoria primaria;
- si la interpretación sigue siendo compleja, escalar.

## 6. Fuentes contradictorias

Dos fuentes dan tamaños de mercado muy distintos.

Esperado:
- revisar definición, fecha y cobertura;
- no promediar automáticamente;
- mostrar impacto en decisión.

## 7. Fuentes locales

Mercado con información útil principalmente en idioma local.

Esperado:
- utilizar fuentes locales cuando sea material;
- no limitarse a inglés/español.

## 8. Desk research suficiente para avanzar, no para validar

Esperado:
- `EVIDENCIA_SUFICIENTE_PARA_AVANZAR`;
- recomendar validación comercial;
- no declarar market fit.

## 9. Research sin evidencia suficiente

Esperado:
- `REQUIERE_INVESTIGACION_ADICIONAL` o `REQUIERE_VALIDACION_EN_CAMPO`;
- no llenar gaps con conocimiento general.

## 10. ICP cuestionado

Evidence muestra que el segmento definido tiene baja presencia, pero aparece otro segmento compatible.

Esperado:
- registrar hallazgo;
- no reescribir ICP silenciosamente;
- handoff a `definicion-icp`.
