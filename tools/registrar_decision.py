#!/usr/bin/env python3
"""Registra una decisión GTM en formato Markdown trazable."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path


def renderizar(payload: dict) -> str:
    decision = payload.get("decision", "")
    if not decision:
        raise ValueError("El campo 'decision' es obligatorio.")

    return "\n".join([
        f"# Decisión — {decision}",
        "",
        f"Fecha: {payload.get('fecha', date.today().isoformat())}",
        f"Estado: {payload.get('estado', 'PENDIENTE_DE_VALIDAR')}",
        "",
        "## Contexto",
        payload.get("contexto", "No documentado."),
        "",
        "## Evidencia",
        payload.get("evidencia", "No documentada."),
        "",
        "## Supuestos",
        payload.get("supuestos", "Ninguno registrado."),
        "",
        "## Riesgos",
        payload.get("riesgos", "No documentados."),
        "",
        "## Validación humana",
        payload.get("validacion_humana", "Pendiente de definir."),
        "",
        "## Siguiente revisión",
        payload.get("siguiente_revision", "No definida."),
        "",
    ])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("entrada", help="JSON con la decisión")
    parser.add_argument("salida", help="Ruta Markdown de salida")
    args = parser.parse_args()

    payload = json.loads(Path(args.entrada).read_text(encoding="utf-8"))
    salida = Path(args.salida)
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(renderizar(payload), encoding="utf-8")
    print(str(salida))


if __name__ == "__main__":
    main()
