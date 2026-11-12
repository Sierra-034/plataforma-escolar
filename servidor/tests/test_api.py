from fastapi.testclient import TestClient

from servidor.main import app

cliente = TestClient(app)


def test_salud():
    assert cliente.get("/salud").json() == {"estado": "ok"}


def test_pedir_codigo_siempre_202():
    assert cliente.post("/v0/auth/codigo").status_code == 202
