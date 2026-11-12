"""Adaptador para demos y pruebas: guarda los mensajes en memoria en lugar de enviarlos."""


class BuzonSimulado:
    def __init__(self) -> None:
        self.mensajes: list[tuple[str, str]] = []

    def enviar_codigo(self, contacto: str, codigo: str) -> None:
        self.mensajes.append((contacto, codigo))
