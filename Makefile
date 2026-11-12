PY := .venv/bin/python
PIP := .venv/bin/pip
URL ?= http://localhost:8000

.PHONY: instalar padron servidor probar conformidad estandar

instalar:
	python3 -m venv .venv
	$(PIP) install -e "servidor[dev]" -e "simulador[dev]"

padron:
	$(PY) -m simulador padron --alumnos 300 --semilla 1 > institucion-sintetica/padron.csv

servidor:
	.venv/bin/uvicorn servidor.main:app --reload

probar:
	.venv/bin/pytest servidor simulador

estandar:
	@test -f estandar/README.md || { echo "Falta el submódulo estandar/. Corre: git submodule update --init (o setup-submodulo.sh si aún no se agrega)"; exit 1; }

conformidad: estandar
	$(PIP) install -q -e estandar/conformidad
	cd estandar/conformidad && ../../.venv/bin/pytest --base-url $(URL)
