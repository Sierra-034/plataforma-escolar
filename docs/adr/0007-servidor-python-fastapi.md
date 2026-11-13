# ADR-0007 · Servidor y simulador en Python con FastAPI

- **Estado:** aceptada (Samuel, 2026-11-12; la fuente todavía dice «propuesto»)
- **Fecha:** 2026-11-10

> Migrado el 2026-11-13 desde [Diseño del MVP: control de acceso escolar](https://claude.ai/artifact/8z2qFXRnnrty1u4cJAGH4R). Texto copiado sin cambios.

## Contexto

La demo tiene tres piezas: la app (React Native), el servidor y el simulador de datos sintéticos y llegadas.

## Opciones

(a) servidor en Python, por ejemplo con FastAPI; (b) servidor en JavaScript para compartir lenguaje con la app.

## Decisión

(a). Un solo lenguaje para servidor, simulador y análisis de colas; buenas librerías para JWS y validación contra OpenAPI; monolito modular con una API y un proceso de fondo (principio 11).

## Consecuencias

El OpenAPI se escribe primero desde la [especificación v0.1](https://claude.ai/artifact/7T3STEZ5im4PVvaH1LJSBQ) y las pruebas verifican que el servidor lo cumple; no se usa el OpenAPI que el framework genera desde el código como fuente (principio 12). El simulador manda sus escaneos por la misma API que los teléfonos.

