# Plataforma escolar

Implementación de referencia, libre, de las
[especificaciones escolares](https://github.com/Sierra-034/especificaciones-escolares).
Primer objetivo: el **MVP de constancias** (ESP-CON v0.2, nivel 2 y luego nivel 3).

Este repo dice **cómo** se construye. **Qué** debe hacer y **cómo se comprueba** viven en el estándar:
si algo aquí contradice la especificación, manda la especificación.

El estándar está dentro de este repo como submódulo de git, en `estandar/`, fijado a una versión.
Clona siempre con los submódulos:

```bash
git clone --recurse-submodules https://github.com/Sierra-034/plataforma-escolar.git
# si ya lo clonaste sin ellos:
git submodule update --init
```

## Piezas

| Carpeta | Qué es | Tecnología |
|---|---|---|
| `servidor/` | API del contrato: entrada con código, emisión y verificación de constancias, llaves del plantel | Python + FastAPI (ADR-0007) |
| `simulador/` | Genera la institución sintética: padrón, grupos, solicitudes | Python |
| `web/` | Interfaz del MVP de constancias (alumno, control escolar, página pública de verificación) | por decidir |
| `institucion-sintetica/` | Configuración del plantel de prueba; el padrón se genera, no se sube | YAML |
| `estandar/` | Submódulo: `especificaciones-escolares` en una versión fija (specs, historias, contrato, pruebas). No se edita aquí | git submodule |
| `docs/adr/` | Decisiones que solo afectan a esta implementación | Markdown |

La app móvil (React Native, ADR-0006) llega con el subsistema de acceso al plantel, después de constancias.

## Arrancar en tu máquina (WSL o Linux)

```bash
make instalar        # crea .venv e instala servidor y simulador
make padron          # genera institucion-sintetica/padron.csv
make servidor        # http://localhost:8000/docs
make probar          # pruebas unitarias
```

## Comprobar que cumple el estándar

Con el servidor corriendo, en otra terminal:

```bash
make conformidad     # corre estandar/conformidad contra http://localhost:8000
```

## Subir de versión el estándar

```bash
scripts/fijar-estandar.sh esp-con-v0.2.0
```

Mueve el submódulo `estandar/` a esa etiqueta y deja el cambio listo para commit. Entra en un PR propio.

## Desarrollo

### Clonar el repositorio

Este repo usa un submódulo. Clona con:

    git clone --recurse-submodules https://github.com/TU_USUARIO/plataforma-escolar

Si ya lo tienes clonado sin el submódulo:

    git submodule update --init

### Estándar de especificaciones

Las specs, ADRs y el contrato OpenAPI viven en `estandar/` (submódulo).
No edites nada en `estandar/` directamente — los cambios van por PCE en especificaciones-escolares.

Para actualizar el estándar a una versión etiquetada:

    scripts/fijar-estandar.sh esp-con-v0.2.0

## Licencia

Pendiente de su ADR. Se publica como software libre.
