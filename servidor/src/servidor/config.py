"""Configuración por variables de entorno (ninguna llave real en el repo)."""
import os

NOTIFICADOR = os.getenv("NOTIFICADOR", "buzon_simulado")  # buzon_simulado | correo  (ADR-0009)
