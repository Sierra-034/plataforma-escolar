"""Entrada con código de un solo uso (ESC-61, ADR-0009)."""
from fastapi import APIRouter, Response, status

router = APIRouter(tags=["identidad"])


@router.post("/auth/codigo", status_code=status.HTTP_202_ACCEPTED)
def pedir_codigo() -> Response:
    # Siempre 202, exista o no el contacto, para no revelar el padrón. Pendiente: generar, guardar HMAC, notificar.
    return Response(status_code=status.HTTP_202_ACCEPTED)
