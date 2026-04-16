"""Reglas de derrota/supervivencia para uso docente."""

import config
import hacks


def starting_lives() -> int:
    if hacks.INFINITE_LIVES:
        return 999_999
    return max(1, config.START_LIVES)


def should_ignore_collision(entity: str, lives_left: int) -> bool:
    """Define si una colision debe ignorarse para no perder la partida."""
    # ===== HACKABLE AREA: GAME OVER RULES =====
    if hacks.GOD_MODE:
        return True
    if entity == "floor" and hacks.NO_FLOOR_DEATH:
        return True
    return lives_left > 1 or hacks.INFINITE_LIVES


def consume_life(lives_left: int) -> int:
    if hacks.INFINITE_LIVES:
        return lives_left
    return max(0, lives_left - 1)
