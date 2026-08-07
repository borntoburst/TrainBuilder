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
    WHITE,
    BLACK,
    SCENE_GAMEPLAY,
    SCENE_CONFIG,
)


class MenuScene(BaseScene):

    def __init__(self, scene_manager):

        super().__init__(scene_manager)

        self.game = scene_manager.game

        self.background = None

        self.title_font = None

        self.button_font = None

        self.start_button = None

        self.config_button = None

    # --------------------------------------------------
    # Scene Lifecycle
    # --------------------------------------------------

    def enter(self):

        if self.title_font is None:

            self.title_font = self.game.assets.get_system_font(
                "arial",
                72,
                bold=True,
            )

            self.button_font = self.game.assets.get_system_font(
                "arial",
                36,
            )

            if self.game.assets.has_image("backgrounds/menu"):

                self.background = self.game.assets.get_image(
                    "backgrounds/menu"
                )

            self._create_buttons()

    def exit(self):
        pass

    # --------------------------------------------------
    # UI
    # --------------------------------------------------

    def _create_buttons(self):

        button_width = 300
        button_height = 70

        center_x = (WINDOW_WIDTH - button_width) // 2

        self.start_button = Button(
            text="BẮT ĐẦU",
            x=center_x,
            y=320,
            width=button_width,
            height=button_height,
            callback=self.start_game,
            font=self.button_font,
        )

        self.config_button = Button(
            text="CẤU HÌNH",
            x=center_x,
            y=420,
            width=button_width,
            height=button_height,
            callback=self.open_config,
            font=self.button_font,
        )

    # --------------------------------------------------
    # Button Callback
    # --------------------------------------------------

    def start_game(self):

        self.scene_manager.change_scene(
            SCENE_GAMEPLAY
        )

    def open_config(self):

        self.scene_manager.change_scene(
            SCENE_CONFIG
        )

    # --------------------------------------------------
    # Event
    # --------------------------------------------------

    def handle_event(self, event):

        self.start_button.handle_event(event)

        self.config_button.handle_event(event)

    # --------------------------------------------------
    # Update
    # --------------------------------------------------

    def update(self, dt):

        self.start_button.update()

        self.config_button.update()

    # --------------------------------------------------
    # Draw
    # --------------------------------------------------

    def draw(self, screen):

        if self.background:

            screen.blit(self.background, (0, 0))

        else:

            screen.fill(WHITE)

        title = self.title_font.render(
            "TRAINBUILDER",
            True,
            BLACK,
        )

        title_rect = title.get_rect(
            center=(WINDOW_WIDTH // 2, 140)
        )

        screen.blit(title, title_rect)

        self.start_button.draw(screen)

        self.config_button.draw(screen)
