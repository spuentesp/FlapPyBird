"""Reglas del movimiento del pajaro para uso docente."""

import config
import hacks


def gravity() -> float:
    """Devuelve la gravedad efectiva."""
    # ===== HACKABLE AREA: PLAYER MOVEMENT =====
    return 0.0 if hacks.NO_GRAVITY else config.GRAVITY


def jump_strength() -> float:
    """Devuelve la fuerza del salto."""
    # ===== HACKABLE AREA: PLAYER MOVEMENT =====
    return config.JUMP_STRENGTH


def max_fall_speed() -> float:
    return config.MAX_FALL_SPEED


def min_rise_speed() -> float:
    return config.MIN_RISE_SPEED
