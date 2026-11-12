# CLAUDE.md · plataforma-escolar

Este repo es la **implementación de referencia** del estándar `especificaciones-escolares`.
El estándar dice qué debe hacer el sistema y cómo se comprueba; aquí solo se decide cómo se construye.
Si algo de este repo contradice al estándar, manda el estándar.

## El estándar está en `estandar/`

`estandar/` es un submódulo de git: el repo `especificaciones-escolares` fijado en una versión.
Esa versión es contra la que se construye este código. Léelo siempre desde ahí, no desde
GitHub ni desde enlaces externos.

| Qué | Dónde |
|---|---|
| Especificaciones (ESP-CON es el MVP en curso) | `estandar/docs/especificaciones/` |
| Historias de usuario, una por archivo | `estandar/docs/historias/ESC-NN.md` |
| Decisiones del estándar (ADR) | `estandar/docs/adr/` |
| Contrato HTTP | `estandar/contratos/openapi.yaml` |
| Pruebas de conformidad | `estandar/conformidad/` |
| Vectores de prueba | `estandar/vectores/` |

Si `estandar/` no existe o está vacío, avisa a la persona: falta `git submodule update --init`
(o correr `setup-submodulo.sh` si el submódulo aún no se agrega). No lo sustituyas con otra fuente.

## Reglas

1. **No edites nada dentro de `estandar/`.** Si una tarea necesita cambiar una historia, una
   especificación, el contrato o una prueba, eso es un PCE (pull request) en el repo
   `especificaciones-escolares`. Detente, explícale a la persona qué cambio hace falta y por qué,
   y ofrece redactar la propuesta; no la apliques aquí.
2. **Antes de implementar una historia**, lee su archivo en `estandar/docs/historias/`, la sección
   de su especificación y sus pruebas `C-NN`. Si el texto todavía dice «por migrar», dilo y pregunta;
   no inventes el comportamiento.
3. **El contrato manda.** Rutas, esquemas y códigos de error salen de `estandar/contratos/openapi.yaml`.
   No agregues ni cambies endpoints que no estén ahí.
4. **No muevas el submódulo** a otra versión salvo que la persona lo pida. Para hacerlo:
   `scripts/fijar-estandar.sh <etiqueta>`, en un PR propio.
5. **Trazabilidad.** Cada commit y cada PR cita las historias y pruebas que atiende (`ESC-05`, `C-31`).
6. **Decisiones de implementación** (lenguaje, framework, base de datos, despliegue) van en
   `docs/adr/NNNN-titulo.md`. La numeración se comparte con el estándar: revisa el número más alto
   en `docs/adr/` y en `estandar/docs/adr/` antes de elegir uno.
7. **Sin datos reales.** Usa la institución sintética (`institucion-sintetica/`) y el simulador.
   Ninguna llave, contraseña ni padrón real entra al repo.

## Comandos

```bash
make instalar      # .venv con servidor y simulador
make probar        # pruebas unitarias
make servidor      # http://localhost:8000/docs
make conformidad   # con el servidor corriendo: pruebas del estándar contra esta implementación
```

## Mapa del código

- `servidor/src/servidor/api/`: rutas FastAPI, una por grupo del contrato.
- `servidor/src/servidor/dominio/`: reglas del negocio, sin FastAPI ni base de datos.
- `servidor/src/servidor/firma/`: llaves del plantel, JWS (EdDSA) y JWKS.
- `servidor/src/servidor/pdf/`: PDF/A-2b con el JWS adjunto y el QR.
- `servidor/src/servidor/notificador/`: puerto Notificador y sus adaptadores (ADR-0009).
- `simulador/`: padrón sintético reproducible.
- `web/`: interfaz del MVP de constancias (tecnología por decidir en una ADR).
