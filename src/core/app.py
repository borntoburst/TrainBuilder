"""
TrainBuilder
Core Application
"""

import pygame

from src.core.constants import (
    GAME_TITLE,
    WINDOW_SIZE,
    FPS,
)

from src.managers.scene_manager import SceneManager


class TrainBuilderApp:

    def __init__(self):

        pygame.init()

        self.screen = pygame.display.set_mode(WINDOW_SIZE)

        pygame.display.set_caption(GAME_TITLE)

        self.clock = pygame.time.Clock()

        self.running = True

        self.scene_manager = SceneManager(self)

    def run(self):

        while self.running:

            dt = self.clock.tick(FPS) / 1000

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.running = False

                self.scene_manager.handle_event(event)

            self.scene_manager.update(dt)

            self.scene_manager.draw(self.screen)

            pygame.display.flip()

        pygame.quit()
