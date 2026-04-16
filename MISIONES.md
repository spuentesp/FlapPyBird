# MISIONES - Flappy Bird Hackeable

Cada mision incluye:
- Objetivo
- Donde mirar
- Pista

## Nivel 1 - tocar numeros

### Mision 1: salto mas fuerte
Objetivo:
Haz que el pajaro suba mas cada vez que presionas `Space`.

Donde mirar:
- `config.py`
- `game/player.py`

Pista:
Busca la variable `JUMP_STRENGTH`.

### Mision 2: tubos mas lentos
Objetivo:
Haz que los tubos se muevan mas lento.

Donde mirar:
- `config.py`
- `game/pipes.py`

Pista:
Prueba con `PIPE_SPEED` y revisa `current_pipe_speed`.

### Mision 3: juego mas facil
Objetivo:
Haz mas grande el espacio entre tubos.

Donde mirar:
- `config.py`
- `game/pipes.py`

Pista:
Aumenta `PIPE_GAP`.

## Nivel 2 - cheats

### Mision 4: modo dios
Objetivo:
Evita perder al colisionar.

Donde mirar:
- `hacks.py`
- `game/collision.py`

Pista:
Activa `GOD_MODE` y observa `should_ignore_collision`.

### Mision 5: puntaje doble
Objetivo:
Haz que cada tubo entregue doble puntaje.

Donde mirar:
- `hacks.py`
- `game/score.py`

Pista:
Activa `DOUBLE_SCORE`.

### Mision 6: 3 vidas iniciales
Objetivo:
Partir con tres vidas.

Donde mirar:
- `config.py`
- `game/collision.py`

Pista:
Cambia `START_LIVES = 3`.

## Nivel 3 - entender logica

### Mision 7: no perder al tocar suelo
Objetivo:
Permitir tocar el suelo sin game over.

Donde mirar:
- `hacks.py`
- `game/collision.py`

Pista:
Activa `NO_FLOOR_DEATH`.

### Mision 8: segunda oportunidad
Objetivo:
Modificar la regla para sobrevivir una colision.

Donde mirar:
- `game/collision.py`
- `src/flappy.py`

Pista:
Revisa como se consumen vidas en `play`.

### Mision 9: dificultad progresiva
Objetivo:
Cada 10 puntos, aumentar dificultad.

Donde mirar:
- `config.py`
- `game/pipes.py`

Pista:
Juega con `DIFFICULTY_*`.

## Nivel 4 - agregar algo

### Mision 10: super salto
Objetivo:
Crear un salto especial al presionar una nueva tecla.

Donde mirar:
- `src/flappy.py`
- `game/player.py`

Pista:
Puedes crear otra funcion de fuerza en `game/player.py`.

### Mision 11: mensaje troll de victoria
Objetivo:
Agregar un mensaje cuando el score supere cierto valor.

Donde mirar:
- `game/ui.py`

Pista:
Usa `pygame.font.SysFont` y dibuja texto condicional.

### Mision 12: vida extra por score
Objetivo:
Ganar una vida cada cierta cantidad de puntos.

Donde mirar:
- `src/flappy.py`
- `game/collision.py`

Pista:
Puedes incrementar vidas al cruzar umbrales de puntaje.

## Nivel 5 - desafio libre

### Mision 13: mod propia
Objetivo:
Disenar una regla nueva y explicarla al curso.

Donde mirar:
- Cualquier modulo de `game/`

Pista:
Si la regla afecta comportamiento, intenta implementarla primero en
`config.py` o `hacks.py` para que sea facil de activar/desactivar.