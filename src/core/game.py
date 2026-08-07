"""
TrainBuilder
Game Core
"""

import pygame

from src.core.constants import (
    GAME_TITLE,
    WINDOW_SIZE,
    FPS,
    ASSET_DIR,
)

from src.managers.asset_manager import AssetManager
from src.managers.scene_manager import SceneManager


class Game:

    def __init__(self):

        # -------------------------------------------------
        # Initialize pygame
        # -------------------------------------------------

        pygame.init()
        pygame.font.init()
        pygame.mixer.init()

        # -------------------------------------------------
        # Window
        # -------------------------------------------------

        self.screen = pygame.display.set_mode(WINDOW_SIZE)

        pygame.display.set_caption(GAME_TITLE)

        self.clock = pygame.time.Clock()

        self.running = True

        # -------------------------------------------------
        # Managers
        # -------------------------------------------------

        self.assets = AssetManager(ASSET_DIR)
        self.assets.load_all()

        self.scene_manager = SceneManager(self)

    def run(self):

        try:

            while self.running:

                dt = self.clock.tick(FPS) / 1000

                self._handle_events()

                self.scene_manager.update(dt)

                self.scene_manager.draw(self.screen)

                pygame.display.flip()

        finally:

            pygame.quit()

    def _handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                self.running = False

                return

            self.scene_manager.handle_event(event)

    def quit(self):

        self.running = False
