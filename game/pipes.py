"""Reglas de tubos y dificultad para uso docente."""

import config
import hacks


def current_pipe_speed(score: int) -> float:
    """Velocidad horizontal de los tubos (positiva; luego se mueve a la izquierda)."""
    # ===== HACKABLE AREA: PIPE RULES =====
    speed = config.PIPE_SPEED
    if hacks.SLOW_PIPES:
        speed = max(1, speed - 2)
    speed += _difficulty_speed_bonus(score)
    return speed


def current_pipe_gap(score: int) -> int:
    """Separacion vertical entre tubos."""
    # ===== HACKABLE AREA: PIPE RULES =====
    if hacks.BIG_GAP_MODE:
        return config.PIPE_GAP + 40
    reduction = _difficulty_gap_reduction(score)
    return max(config.DIFFICULTY_MIN_GAP, config.PIPE_GAP - reduction)


def _difficulty_level(score: int) -> int:
    if config.DIFFICULTY_STEP_POINTS <= 0:
        return 0
    return score // config.DIFFICULTY_STEP_POINTS


def _difficulty_gap_reduction(score: int) -> int:
    return _difficulty_level(score) * config.DIFFICULTY_GAP_REDUCTION


def _difficulty_speed_bonus(score: int) -> float:
    return _difficulty_level(score) * config.DIFFICULTY_SPEED_INCREASE
