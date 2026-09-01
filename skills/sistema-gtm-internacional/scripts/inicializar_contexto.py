#!/usr/bin/env python3
"""Crea un workspace company-context/ mínimo sin inventar datos de empresa."""

from __future__ import annotations

import argparse
from pathlib import Path

PLANTILLAS = {
    "STATUS.md": "# Estado del contexto\n\nEstado general: SIN_CONFIGURAR\n\n## Dominios\n\nCompletar estado, fecha, gaps y conflictos antes de trabajo GTM sustantivo.\n",
    "EMPRESA.md": "# Empresa\n\n## Identidad\n\n## Modelo de negocio\n\n## Capacidades relevantes\n\n## Procedencia y validación\n",
    "PRODUCTOS-Y-SERVICIOS.md": "# Productos y servicios\n\n## Oferta prioritaria\n\n## Diferenciadores confirmados\n\n## Limitaciones\n\n## Evidencia / procedencia\n",
    "APLICACIONES.md": "# Aplicaciones\n\n## Aplicaciones confirmadas\n\n## Aplicaciones por validar\n\n## Condiciones técnicas relevantes\n",
    "ICP-Y-CLIENTES.md": "# ICP y clientes\n\n## ICP actual\n\n## Criterios de inclusión\n\n## Disqualifiers\n\n## Clientes/referencias autorizadas\n",
    "MERCADOS.md": "# Mercados\n\n## Mercados actuales\n\n## Mercados en evaluación\n\n## Experiencia previa\n",
    "ESTRATEGIA.md": "# Estrategia\n\n## Prioridades\n\n## Canales preferidos\n\n## No-prioridades\n\n## Horizonte\n",
    "OBJETIVO-ACTUAL.md": "# Objetivo actual\n\n## Objetivo\n\n## Decisión a preparar\n\n## Horizonte\n\n## Resultado esperado\n",
    "VENTAS-Y-CANALES.md": "# Ventas y canales\n\n## Modelo comercial actual\n\n## Canal directo\n\n## Distribuidores/agentes/integradores\n\n## Proceso comercial\n",
    "RESTRICCIONES.md": "# Restricciones\n\n## Capacidad\n\n## Logística/lead times\n\n## Canal\n\n## Regulación/certificación\n\n## Recursos\n",
    "APROBACIONES.md": "# Aprobaciones\n\n## Claims\n\n## Pricing/condiciones\n\n## Comunicaciones externas\n\n## Contratos/exclusividad\n",
    "CLAIMS-APROBADOS.md": "# Claims aprobados\n\nRegistrar únicamente claims autorizados, su evidencia, alcance y restricciones de uso.\n",
    "MARCA-Y-VOZ.md": "# Marca y voz\n\n## Personalidad\n\n## Tono\n\n## Nivel técnico\n\n## Idiomas\n\n## Evitar\n",
    "TERMINOLOGIA.md": "# Terminología\n\n## Términos preferidos\n\n## Términos prohibidos/evitar\n\n## Traducciones validadas\n",
}


def inicializar(destino: Path) -> list[str]:
    destino.mkdir(parents=True, exist_ok=True)
    creados = []
    for nombre, contenido in PLANTILLAS.items():
        ruta = destino / nombre
        if ruta.exists():
            continue
        ruta.write_text(contenido, encoding="utf-8")
        creados.append(nombre)
    return creados


def main() -> None:
    parser = argparse.ArgumentParser(description="Inicializa company-context/ sin inventar datos")
    parser.add_argument("ruta", nargs="?", default="company-context")
    args = parser.parse_args()
    creados = inicializar(Path(args.ruta))
    print(f"Contexto inicializado. Archivos creados: {len(creados)}")
    for nombre in creados:
        print(f"- {nombre}")


if __name__ == "__main__":
    main()
