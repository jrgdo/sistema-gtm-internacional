#!/usr/bin/env python3
"""Calcula un score transparente de distribuidor con unknowns visibles.

No interpreta automáticamente campos desconocidos como cero.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def calcular(payload: dict) -> dict:
    criterios = payload.get("criterios", [])
    evaluados = []
    unknowns = []
    suma = 0.0
    peso_total = 0.0

    for criterio in criterios:
        nombre = criterio["nombre"]
        peso = float(criterio["peso"])
        valor = criterio.get("valor")

        if valor is None:
            unknowns.append(nombre)
            continue

        valor = float(valor)
        if not 0 <= valor <= 5:
            raise ValueError(f"Valor fuera de rango para {nombre}: {valor}")
        if peso < 0:
            raise ValueError(f"Peso negativo para {nombre}")

        contribucion = valor * peso
        suma += contribucion
        peso_total += peso
        evaluados.append({**criterio, "contribucion": round(contribucion, 4)})

    score = round(suma / peso_total, 3) if peso_total else None

    return {
        "score_sobre_criterios_evaluados": score,
        "criterios_evaluados": evaluados,
        "unknowns": unknowns,
        "cobertura": round(len(evaluados) / len(criterios), 3) if criterios else 0,
        "advertencia": "No usar un score con baja cobertura como recomendación definitiva. Unknown no equivale a cero.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("archivo")
    args = parser.parse_args()
    payload = json.loads(Path(args.archivo).read_text(encoding="utf-8"))
    print(json.dumps(calcular(payload), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
