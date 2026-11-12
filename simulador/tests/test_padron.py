from simulador import padron


def test_misma_semilla_mismo_padron():
    assert padron.generar(50, 7) == padron.generar(50, 7)


def test_matriculas_unicas():
    filas = padron.generar(200, 1)
    assert len({f["matricula"] for f in filas}) == 200
