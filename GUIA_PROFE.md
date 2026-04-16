# GUIA_PROFE - Uso en clase

## Ruta sugerida de clase

1. Correr el juego (`python main.py`).
2. Cambiar dos valores en `config.py`.
3. Activar un hack en `hacks.py`.
4. Revisar `game/player.py` y `game/pipes.py`.
5. Cerrar con una mision de logica (`game/collision.py`).

## Misiones mas faciles

- Cambiar gravedad (`GRAVITY`).
- Cambiar velocidad de tubos (`PIPE_SPEED`).
- Activar `GOD_MODE`.
- Activar `DOUBLE_SCORE`.

## Misiones medias

- Ajustar dificultad progresiva (`DIFFICULTY_*`).
- Cambiar regla de derrota por suelo (`NO_FLOOR_DEATH`).
- Partir con mas vidas (`START_LIVES`).

## Misiones dificiles

- Super salto con tecla nueva.
- Vida extra por umbral de score.
- Cambiar dinamica de spawn sin romper el loop.

## Bugs comunes y salida rapida

- "No abre el juego":
  - Falta instalar pygame en el entorno activo.
  - Solucion: activar `.venv` e instalar `requirements.txt`.

- "Se ve demasiado dificil/imposible":
  - `PIPE_SPEED` muy alto o `PIPE_GAP` muy bajo.
  - Solucion: volver a valores por defecto.

- "No se puede perder nunca":
  - `GOD_MODE` o `INFINITE_LIVES` activos.
  - Solucion: revisar `hacks.py`.

- "No cae el pajaro":
  - `NO_GRAVITY` activo.

## Donde esta cada comportamiento clave

- Movimiento del pajaro: `game/player.py`
- Tubos y dificultad: `game/pipes.py`
- Puntaje: `game/score.py`
- Derrota/supervivencia: `game/collision.py`
- HUD y mensajes: `game/ui.py`
- Loop principal: `src/flappy.py`

## Recomendacion didactica

- Empezar con cambios de parametros.
- Pasar luego a banderas en `hacks.py`.
- Cerrar con lectura de condiciones en colisiones.
- Pedir siempre una mini-explicacion: que tocaron, por que y que efecto tuvo.