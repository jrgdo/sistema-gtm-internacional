#!/usr/bin/env python3
"""Calcula un score transparente de mercado a partir de criterios explícitos.

Entrada JSON esperada:
{
  "criterios": [
    {"nombre": "demanda", "bloque": "atractivo", "valor": 4, "peso": 0.25, "confianza": "MEDIA"}
  ]
}

Los valores deben estar entre 0 y 5. Los pesos no se inventan en esta tool.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

BLOQUES_VALIDOS = {"atractivo", "capacidad_de_ganar", "friccion"}


def calcular(payload: dict) -> dict:
    criterios = payload.get("criterios", [])
    if not criterios:
        raise ValueError("Se requiere al menos un criterio.")

    acumulado = {bloque: {"suma": 0.0, "peso": 0.0} for bloque in BLOQUES_VALIDOS}
    detalle = []

    for criterio in criterios:
        nombre = criterio["nombre"]
        bloque = criterio["bloque"]
        valor = float(criterio["valor"])
        peso = float(criterio["peso"])

        if bloque not in BLOQUES_VALIDOS:
            raise ValueError(f"Bloque no válido: {bloque}")
        if not 0 <= valor <= 5:
            raise ValueError(f"Valor fuera de rango para {nombre}: {valor}")
        if peso < 0:
            raise ValueError(f"Peso negativo para {nombre}")

        acumulado[bloque]["suma"] += valor * peso
        acumulado[bloque]["peso"] += peso
        detalle.append({**criterio, "contribucion": round(valor * peso, 4)})

    scores = {}
    for bloque, datos in acumulado.items():
        scores[bloque] = (
            round(datos["suma"] / datos["peso"], 3) if datos["peso"] > 0 else None
        )

    return {
        "scores_por_bloque": scores,
        "detalle": detalle,
        "advertencia": "El score ordena criterios explícitos; no sustituye evidencia, sensibilidad ni decisión humana.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("archivo", help="JSON con criterios, valores y pesos")
    args = parser.parse_args()
    payload = json.loads(Path(args.archivo).read_text(encoding="utf-8"))
    print(json.dumps(calcular(payload), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
