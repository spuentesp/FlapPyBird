"""Reglas de puntaje para uso docente."""

import config
import hacks


def points_per_pipe() -> int:
    """Retorna cuantos puntos suma cruzar un tubo."""
    # ===== HACKABLE AREA: SCORE RULES =====
    points = config.SCORE_PER_PIPE
    if hacks.DOUBLE_SCORE:
        points *= 2
    return points
