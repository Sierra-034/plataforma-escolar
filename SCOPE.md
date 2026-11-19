# Alcance

Qué cubre esta implementación de referencia, contra qué versión del estándar y qué tan lejos va.
Si este archivo y el estándar no coinciden, manda el estándar.

## Contra qué versión

| Qué | Versión | Dónde |
|---|---|---|
| Estándar fijado | `esp-con-v0.5.0` | submódulo `estandar/` (`git submodule status`) |
| ESP-CON · Constancias y verificación | 0.5.0 | `estandar/docs/especificaciones/ESP-CON.md` |
| ESP-IDP · Identidad (solo lo que ESP-CON pide) | 0.2.0 | `estandar/docs/especificaciones/ESP-IDP.md` |
| Contrato HTTP | 0.3.0 | `estandar/contratos/openapi.yaml` |

Las rutas, esquemas y errores del servidor salen del contrato. No se agrega ni se cambia una ruta
que no esté ahí: eso es un PCE en `especificaciones-escolares`.

## Objetivo y nivel

- **Objetivo:** ESP-CON **nivel 3** (adopción plena) con la institución sintética, como dice el
  [criterio de adopción](https://github.com/Sierra-034/especificaciones-escolares/blob/esp-con-v0.5.0/docs/especificaciones/ESP-CON.md#criterio-de-adopción).
- **Nivel declarado hoy: 0.** Todavía no pasa ninguna prueba de conformidad.

Un nivel se declara solo cuando pasan **todas** sus pruebas con `make conformidad`.

## Casos de uso que cubre

En el orden de la [ruta de implementación](https://github.com/Sierra-034/especificaciones-escolares/blob/esp-con-v0.5.0/docs/especificaciones/ESP-CON.md#ruta-de-implementación).
La columna **Estado** se actualiza en el mismo PR que hace pasar las pruebas de la fila.

| Paso | Historia | Qué puede hacer la persona | Pruebas | Nivel | Estado |
|---|---|---|---|---|---|
| 1 | ESC-44 | El padrón de la institución sintética queda cargado en el servidor, con los nombres en NFC | C-18 (parte del servidor) | 1 | Pendiente |
| 2 | ESC-63 | Cualquiera baja las llaves públicas del plantel | C-58 | 1 | Pendiente |
| 3 | ESC-19 | Cada persona solo hace lo que su rol permite | C-59 (se corre en el paso 4) | 2 | Pendiente |
| 4 | ESC-61 | El alumno entra con un código, sin contraseña; control escolar registra su contacto en persona | C-26..C-30, C-48..C-50, C-52, C-57, C-59 | 2 | Pendiente |
| 5 | ESC-08 | Control escolar crea y versiona la plantilla «constancia de estudios» | C-31, C-32 | 2 | Pendiente |
| 6 | ESC-05 | El alumno descarga su constancia firmada en PDF/A-2b, con folio y QR | C-33..C-37, C-45, C-51 | 2 | Pendiente |
| 7 | ESC-07 | Cualquiera verifica una constancia abriendo su QR, sin cuenta | C-38..C-42, C-46, C-47, C-53, C-55, C-56, C-60 | 3 | Pendiente |
| 8 | ESC-62 | Control escolar anula una constancia y la verificación lo muestra | C-43, C-44, C-54 | 3 | Pendiente |

## Lo que no cubre

| Qué | Por qué | Mientras tanto |
|---|---|---|
| La puerta: credencial en el teléfono, escáner, registro de entradas (ESP-PLA) | Va después del MVP de constancias | — |
| App móvil (ADR-0006) | Llega con la puerta | La interfaz de constancias es web (`web/`) |
| Importar el padrón por API (`POST /v0/padron/importaciones`) | No está en el contrato: faltan columnas y rol (P-22) | `make padron` genera el padrón sintético y el servidor lo lee de ese archivo |
| Administrar llaves por API: generar, rotar, retirar, revocar | No está especificado (P-16) | La llave `constancia-*` se crea por configuración |
| Asignar roles distintos de `alumno` | No está especificado (P-18) | Se cargan a mano en `institucion-sintetica/` |
| Vectores de prueba de ESP-CON | El del estándar contradice la especificación (P-13) | Las pruebas generan sus propias llaves de prueba |
| Entrar con OpenID Connect | Pendiente de decidir contra el código de ESC-61 (P-19) | Solo código de 6 dígitos |
| Cola de revisión, otros tipos de constancia, tutores, firma autógrafa | Fuera de ESP-CON 0.5 | — |
| Datos o llaves de un plantel real | Regla del proyecto | Solo la institución sintética |

Los pendientes `P-NN` están en `estandar/docs/especificaciones/pendientes.md`.

## Cómo se comprueba

```bash
make servidor        # en una terminal
make conformidad     # en otra: corre estandar/conformidad contra http://localhost:8000
```

## Cuándo cambia este archivo

- Cuando una fila de «Casos de uso» pasa sus pruebas: en el mismo PR, con las `C-NN` en la descripción.
- Cuando se fija otra versión del estándar (procedimiento C): en un PR propio justo después, revisando
  versiones, pasos y pruebas contra la especificación nueva.
