"""Adaptador de correo para el MVP. Pendiente: SMTP configurable por variables de entorno."""


class Correo:
    def enviar_codigo(self, contacto: str, codigo: str) -> None:
        raise NotImplementedError
