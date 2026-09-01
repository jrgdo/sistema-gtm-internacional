#!/usr/bin/env python3
"""Valida la estructura mínima del Company Context Engine."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ARCHIVOS_REQUERIDOS = [
    "STATUS.md",
    "EMPRESA.md",
    "PRODUCTOS-Y-SERVICIOS.md",
    "APLICACIONES.md",
    "ICP-Y-CLIENTES.md",
    "MERCADOS.md",
    "ESTRATEGIA.md",
    "OBJETIVO-ACTUAL.md",
    "VENTAS-Y-CANALES.md",
    "RESTRICCIONES.md",
    "APROBACIONES.md",
    "CLAIMS-APROBADOS.md",
    "MARCA-Y-VOZ.md",
    "TERMINOLOGIA.md",
]


def validar_contexto(ruta: Path) -> dict:
    if not ruta.exists() or not ruta.is_dir():
        return {
            "valido_estructura": False,
            "error": "RUTA_CONTEXT0_INEXISTENTE",
            "archivos_faltantes": ARCHIVOS_REQUERIDOS,
        }

    faltantes = [nombre for nombre in ARCHIVOS_REQUERIDOS if not (ruta / nombre).is_file()]
    vacios = [
        nombre
        for nombre in ARCHIVOS_REQUERIDOS
        if (ruta / nombre).is_file() and not (ruta / nombre).read_text(encoding="utf-8").strip()
    ]

    return {
        "valido_estructura": not faltantes and not vacios,
        "archivos_faltantes": faltantes,
        "archivos_vacios": vacios,
        "nota": "La estructura válida no implica que el contenido esté validado, vigente o libre de conflictos.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Valida la estructura de company-context/")
    parser.add_argument("ruta", nargs="?", default="company-context")
    args = parser.parse_args()
    resultado = validar_contexto(Path(args.ruta))
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    raise SystemExit(0 if resultado["valido_estructura"] else 1)


if __name__ == "__main__":
    main()
