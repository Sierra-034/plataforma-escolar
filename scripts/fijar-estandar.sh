#!/usr/bin/env bash
# Fija el submódulo estandar/ en una etiqueta del estándar. Uso: scripts/fijar-estandar.sh esp-con-v0.2.0
set -euo pipefail
ETIQUETA="${1:?Indica la etiqueta, p. ej. esp-con-v0.2.0}"
cd "$(git rev-parse --show-toplevel)"
test -f estandar/README.md || { echo "Falta estandar/. Corre: git submodule update --init" >&2; exit 1; }
git -C estandar fetch --tags --quiet origin
git -C estandar checkout --quiet "$ETIQUETA"
git add estandar
echo "estandar/ fijado en $ETIQUETA. Revisa y haz commit:"
echo "  git commit -m \"chore: fijar estándar en $ETIQUETA\""
