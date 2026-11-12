from fastapi import FastAPI

from servidor.api import auth, constancias

app = FastAPI(title="Plataforma escolar: servidor de referencia", version="0.0.1")
app.include_router(auth.router, prefix="/v0")
app.include_router(constancias.router, prefix="/v0")


@app.get("/salud", include_in_schema=False)
def salud():
    return {"estado": "ok"}
