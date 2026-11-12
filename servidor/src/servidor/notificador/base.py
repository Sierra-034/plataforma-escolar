from typing import Protocol


class Notificador(Protocol):
    def enviar_codigo(self, contacto: str, codigo: str) -> None: ...
