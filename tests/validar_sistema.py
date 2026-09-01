#!/usr/bin/env python3
"""Smoke test ejecutable del repositorio público."""

from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]

REQUERIDOS = [
    "AGENTS.md",
    "ARCHITECTURE.md",
    "CLAUDE.md",
    "CODEX.md",
    "ROADMAP.md",
    "agents/agente-gtm-internacional/AGENT.md",
    "skills/sistema-gtm-internacional/SKILL.md",
    "skills/onboarding-empresa/SKILL.md",
    "skills/diagnostico-internacional/SKILL.md",
    "skills/definicion-icp/SKILL.md",
    "skills/priorizacion-de-mercados/SKILL.md",
    "skills/investigacion-de-mercado/SKILL.md",
    "skills/evaluacion-de-distribuidores/SKILL.md",
    "skills/investigacion-de-cuentas/SKILL.md",
    "skills/preparacion-comercial/SKILL.md",
    "contracts/entrada-componente.yaml",
    "contracts/salida-componente.yaml",
    "qa/QUALITY-GUARD.md",
    "tools/validar_contexto.py",
    "tools/calcular_score_mercado.py",
    "tools/calcular_score_distribuidor.py",
    "workflows/comparar-mercados/WORKFLOW.md",
    "workflows/evaluar-distribuidor/WORKFLOW.md",
    "workflows/investigar-cuenta/WORKFLOW.md",
    "workflows/preparar-reunion/WORKFLOW.md",
]


def main() -> None:
    faltantes = [ruta for ruta in REQUERIDOS if not (RAIZ / ruta).is_file()]
    if faltantes:
        print("FALLO: faltan archivos requeridos:")
        for ruta in faltantes:
            print(f"- {ruta}")
        raise SystemExit(1)

    skills = list((RAIZ / "skills").glob("*/SKILL.md"))
    sin_frontmatter = []
    for skill in skills:
        texto = skill.read_text(encoding="utf-8")
        cabecera = texto[:2500]
        if not texto.startswith("---\n") or "name:" not in cabecera or "description:" not in cabecera:
            sin_frontmatter.append(str(skill.relative_to(RAIZ)))

    if sin_frontmatter:
        print("FALLO: skills sin frontmatter mínimo:")
        for ruta in sin_frontmatter:
            print(f"- {ruta}")
        raise SystemExit(1)

    print(f"OK: estructura base válida. Skills detectadas: {len(skills)}")


if __name__ == "__main__":
    main()
