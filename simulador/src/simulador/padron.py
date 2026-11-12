"""Padrón sintético reproducible: mismas opciones y semilla, mismo padrón. Nadie real aparece aquí."""
import csv
import io
import random

NOMBRES = ["Ana", "Luis", "María", "José", "Fernanda", "Diego", "Valeria", "Jorge", "Ximena", "Carlos"]
APELLIDOS = ["García", "Hernández", "López", "Martínez", "González", "Pérez", "Rodríguez", "Sánchez", "Ramírez", "Cruz"]
CAMPOS = ["matricula", "nombre", "apellidos", "semestre", "grupo", "turno", "ciclo", "correo"]


def generar(alumnos: int, semilla: int, ciclo: str = "2026-2027/1") -> list[dict]:
    azar = random.Random(semilla)
    filas = []
    for i in range(1, alumnos + 1):
        semestre = azar.choice([1, 3, 5])
        turno = azar.choice(["matutino", "vespertino"])
        filas.append({
            "matricula": f"SIN{i:06d}",
            "nombre": azar.choice(NOMBRES),
            "apellidos": f"{azar.choice(APELLIDOS)} {azar.choice(APELLIDOS)}",
            "semestre": semestre,
            "grupo": f"{semestre}{'AB'[turno == 'vespertino']}{azar.randint(1, 3)}",
            "turno": turno,
            "ciclo": ciclo,
            "correo": f"alumno{i:06d}@ejemplo.invalid",
        })
    return filas


def a_csv(filas: list[dict]) -> str:
    salida = io.StringIO()
    escritor = csv.DictWriter(salida, fieldnames=CAMPOS)
    escritor.writeheader()
    escritor.writerows(filas)
    return salida.getvalue()
