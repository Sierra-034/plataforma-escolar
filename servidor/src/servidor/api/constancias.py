"""Emisión y verificación de constancias (ESC-05, ESC-07, ESC-62; ADR-0008)."""
from fastapi import APIRouter, HTTPException

router = APIRouter(tags=["constancias"])


@router.get("/constancias/{folio}")
def verificar(folio: str):
    raise HTTPException(status_code=501, detail="pendiente")
