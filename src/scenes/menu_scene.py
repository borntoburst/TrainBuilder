"""
TrainBuilder
Menu Scene
"""

import pygame

from src.scenes.base_scene import BaseScene
from src.ui.button import Button

from src.core.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    SCENE_GAMEPLAY,
    SCENE_CONFIG,
    WHITE,
    BLACK,
)


class MenuScene(BaseScene):

    def __init__(self, scene_manager):

        super().__init__(scene_manager)

        self.title_font = pygame.font.SysFont("arial", 72, bold=True)
        self.button_font = pygame.font.SysFont("arial", 36)

        self.title_surface = self.title_font.render(
            "TRAINBUILDER",
            True,
            BLACK,
        )

        self.start_button = Button(
            text="BẮT ĐẦU",
            x=WINDOW_WIDTH // 2 - 150,
            y=320,
            width=300,
            height=70,
            callback=self.start_game,
            font=self.button_font,
        )

        self.config_button = Button(
            text="CẤU HÌNH",
            x=WINDOW_WIDTH // 2 - 150,
            y=420,
            width=300,
            height=70,
            callback=self.open_config,
            font=self.button_font,
        )

    def enter(self):
        pass

    def exit(self):
        pass

    def start_game(self):
        self.scene_manager.change_scene(SCENE_GAMEPLAY)

    def open_config(self):
        self.scene_manager.change_scene(SCENE_CONFIG)

    def handle_event(self, event):

        self.start_button.handle_event(event)
        self.config_button.handle_event(event)

    def update(self, dt):

        self.start_button.update()
        self.config_button.update()

    def draw(self, screen):

        screen.fill(WHITE)

        title_rect = self.title_surface.get_rect(
            center=(WINDOW_WIDTH // 2, 150)
        )

        screen.blit(self.title_surface, title_rect)

        self.start_button.draw(screen)
        self.config_button.draw(screen)
