import os

import pygame

import config

from .images import Images
from .sounds import Sounds
from .window import Window


class GameConfig:
    def __init__(
        self,
        screen: pygame.Surface,
        clock: pygame.time.Clock,
        fps: int,
        window: Window,
        images: Images,
        sounds: Sounds,
    ) -> None:
        self.screen = screen
        self.clock = clock
        self.fps = fps
        self.window = window
        self.images = images
        self.sounds = sounds
        env_debug = os.environ.get("DEBUG")
        self.debug = (
            env_debug.lower() == "true"
            if isinstance(env_debug, str)
            else config.DEBUG
        )

    def tick(self) -> None:
        self.clock.tick(self.fps)
