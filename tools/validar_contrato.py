#!/usr/bin/env python3
"""Valida presencia de campos mínimos en payloads YAML/JSON del sistema."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None

CONTRATOS = {
    "entrada": ["objetivo", "decision", "contexto_relevante"],
    "salida": ["resultado", "estado", "confianza", "siguiente_accion"],
    "handoff": ["objetivo", "decision", "componente_destino", "criterio_de_finalizacion"],
    "decision": ["decision", "recomendacion", "validacion_humana"],
}


def cargar(path: Path) -> dict:
    texto = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(texto)
    if yaml is None:
        raise RuntimeError("PyYAML es necesario para validar archivos YAML.")
    return yaml.safe_load(texto) or {}


def validar(tipo: str, payload: dict) -> dict:
    if tipo not in CONTRATOS:
        raise ValueError(f"Tipo de contrato no soportado: {tipo}")
    faltantes = [campo for campo in CONTRATOS[tipo] if campo not in payload or payload[campo] in (None, "")]
    return {
        "tipo": tipo,
        "valido": not faltantes,
        "campos_faltantes": faltantes,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("tipo", choices=sorted(CONTRATOS))
    parser.add_argument("archivo")
    args = parser.parse_args()
    resultado = validar(args.tipo, cargar(Path(args.archivo)))
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    raise SystemExit(0 if resultado["valido"] else 1)


if __name__ == "__main__":
    main()
