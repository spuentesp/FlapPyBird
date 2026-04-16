# Ideas de misiones extra

## 1) Turbulencia
- Cada 7 puntos, invertir gravedad por 1 segundo.
- Pistas: usar contador de frames en `src/flappy.py` y bandera temporal en `game/player.py`.

## 2) Combo de riesgo
- Si pasa 3 tubos sin tocar borde de pantalla, bonus de score.
- Pistas: crear contador de racha en `src/flappy.py`.

## 3) Modo invisible
- El score sigue, pero ocultar los tubos 1 segundo cada cierto tiempo.
- Pistas: condicionar dibujo en `src/entities/pipe.py`.

## 4) Boton secreto
- Agregar tecla `R` que reinicia solo vidas y deja score.
- Pistas: manejar tecla en `src/flappy.py`.

## 5) Victoria troll
- Mostrar texto al pasar 30 puntos con mensaje personalizado.
- Pistas: `game/ui.py`.
