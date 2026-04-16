# Flappy Bird - edicion hackeable para clase

Este repositorio es una version docente de FlapPyBird pensada para trabajar
en clases practicas. El objetivo es que puedas:

1. correr el juego rapido,
2. encontrar variables importantes,
3. entender que modulo controla cada comportamiento,
4. resolver misiones sin leer todo el proyecto.

## Como correr

1. Crea entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Instala dependencias:

```bash
pip install -r requirements.txt
```

3. Ejecuta el juego:

```bash
python main.py
```

Controles:
- `Space` o `ArrowUp`: saltar
- `Esc`: cerrar

## Estructura rapida

- `main.py`: punto de entrada
- `config.py`: valores editables del juego
- `hacks.py`: cheats y modos especiales
- `game/player.py`: reglas de movimiento del pajaro
- `game/pipes.py`: velocidad, gap y dificultad de tubos
- `game/score.py`: reglas de puntaje
- `game/collision.py`: reglas de derrota/supervivencia
- `game/ui.py`: HUD (score, vidas, hacks activos)
- `src/`: motor real del juego (render, entidades, loop)

## Si quieres hackear el juego, parte por config.py

Cambios rapidos sugeridos:

- `GRAVITY`: cuanto cae el pajaro
- `JUMP_STRENGTH`: cuanto sube al saltar
- `PIPE_SPEED`: velocidad base de tubos
- `PIPE_GAP`: espacio entre tubos
- `START_LIVES`: vidas iniciales
- `SCORE_PER_PIPE`: puntaje por tubo cruzado

## Cheats listos para usar (hacks.py)

Pon `True` en cualquiera de estas banderas:

- `GOD_MODE`
- `INFINITE_LIVES`
- `DOUBLE_SCORE`
- `NO_GRAVITY`
- `SLOW_PIPES`
- `BIG_GAP_MODE`
- `NO_FLOOR_DEATH`

## Primeras misiones sugeridas

- Hacer el salto mas fuerte
- Hacer los tubos mas lentos
- Activar modo dios
- Duplicar puntaje
- Cambiar la regla de derrota

Revisa [MISIONES.md](MISIONES.md) para el itinerario completo.

## Comportamientos y donde mirar

- El pajaro cae:
	- `config.py` (`GRAVITY`)
	- `game/player.py` (`gravity`)
- El pajaro salta:
	- `config.py` (`JUMP_STRENGTH`)
	- `game/player.py` (`jump_strength`)
- Los tubos avanzan:
	- `config.py` (`PIPE_SPEED`)
	- `game/pipes.py` (`current_pipe_speed`)
- Los tubos aparecen con distinto gap:
	- `config.py` (`PIPE_GAP` y dificultad)
	- `game/pipes.py` (`current_pipe_gap`)
- El score sube:
	- `config.py` (`SCORE_PER_PIPE`)
	- `hacks.py` (`DOUBLE_SCORE`)
	- `game/score.py` (`points_per_pipe`)
- Se decide si pierdes o sobrevives:
	- `game/collision.py` (`should_ignore_collision`)
	- `hacks.py` (`GOD_MODE`, `NO_FLOOR_DEATH`, `INFINITE_LIVES`)

## Archivos para clase

- [MISIONES.md](MISIONES.md): misiones por nivel con objetivo, donde mirar y pista
- [GUIA_PROFE.md](GUIA_PROFE.md): ruta sugerida de clase, dificultad y desbloqueos
- [extras/soluciones_base.md](extras/soluciones_base.md): ideas de solucion guiadas
- [extras/ideas_misiones_extra.md](extras/ideas_misiones_extra.md): desafios extendidos
