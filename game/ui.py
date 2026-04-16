"""Funciones de interfaz utiles para la version de clase."""

import pygame

import hacks


def draw_hud(screen: pygame.Surface, score: int, lives: int) -> None:
    """Dibuja HUD simple con score, vidas y hacks activos."""
    font = pygame.font.SysFont("Arial", 16, True)
    lives_text = "inf" if hacks.INFINITE_LIVES else str(lives)
    hud = font.render(f"Score: {score}  Vidas: {lives_text}", True, (255, 255, 255))
    shadow = font.render(f"Score: {score}  Vidas: {lives_text}", True, (0, 0, 0))
    screen.blit(shadow, (9, 9))
    screen.blit(hud, (8, 8))

    active = _active_hacks()
    if active:
        hacks_text = font.render(
            "Hacks: " + ", ".join(active), True, (255, 235, 140)
        )
        screen.blit(hacks_text, (8, 30))


def _active_hacks() -> list[str]:
    flags = []
    if hacks.GOD_MODE:
        flags.append("GOD_MODE")
    if hacks.DOUBLE_SCORE:
        flags.append("DOUBLE_SCORE")
    if hacks.NO_GRAVITY:
        flags.append("NO_GRAVITY")
    if hacks.SLOW_PIPES:
        flags.append("SLOW_PIPES")
    if hacks.BIG_GAP_MODE:
        flags.append("BIG_GAP_MODE")
    if hacks.NO_FLOOR_DEATH:
        flags.append("NO_FLOOR_DEATH")
    if hacks.INFINITE_LIVES:
        flags.append("INFINITE_LIVES")
    return flags
