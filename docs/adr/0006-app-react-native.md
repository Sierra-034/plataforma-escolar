# ADR-0006 · App multiplataforma con React Native

- **Estado:** propuesta, espera al acceso al plantel
- **Fecha:** 2026-11-10

> Migrado el 2026-11-13 desde [Diseño del MVP: control de acceso escolar](https://claude.ai/artifact/8z2qFXRnnrty1u4cJAGH4R). Texto copiado sin cambios.

## Contexto

Una app web es ligera y no se instala (principio 70), pero no puede bloquear capturas ni guardar llaves de forma segura; una app nativa por plataforma duplica el trabajo.

## Opciones

(a) app web instalable; (b) multiplataforma con React Native; (c) nativa por plataforma.

## Propuesta

(b) React Native, una sola base de código para Android y iPhone.

## Consecuencias

En Android puede bloquear capturas en la pantalla de la credencial y en iPhone solo detectarlas; cámara para el escáner, almacenamiento local para trabajar sin red y llavero seguro para las llaves. El costo es que el alumno debe instalar la app y que hay que cuidar su tamaño en teléfonos sencillos (presupuesto con número, principio 70).

## Por confirmar

Si el escáner de la puerta y el tablero de dirección también van en React Native o el tablero queda como página web.

## Nota

El MVP de constancias se usa desde la web, así que esta decisión espera al subsistema de acceso al plantel.
