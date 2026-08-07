"""
TrainBuilder
Config Scene
"""

import pygame

from src.scenes.base_scene import BaseScene
from src.ui.button import Button

from src.core.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WHITE,
    BLACK,
    SCENE_MENU,
)


class ConfigScene(BaseScene):

    def __init__(self, scene_manager):

        super().__init__(scene_manager)

        self.game = scene_manager.game

        self.title_font = None
        self.button_font = None

        self.back_button = None

    # --------------------------------------------------
    # Scene Lifecycle
    # --------------------------------------------------

    def enter(self):

        if self.title_font is None:

            self.title_font = self.game.assets.get_system_font(
                "arial",
                64,
                bold=True,
            )

            self.button_font = self.game.assets.get_system_font(
                "arial",
                32,
            )

            self._create_ui()

    def exit(self):
        pass

    # --------------------------------------------------
    # UI
    # --------------------------------------------------

    def _create_ui(self):

        self.back_button = Button(
            text="QUAY LẠI",
            x=40,
            y=40,
            width=180,
            height=60,
            callback=self.back_to_menu,
            font=self.button_font,
        )

    # --------------------------------------------------
    # Callback
    # --------------------------------------------------

    def back_to_menu(self):

        self.scene_manager.change_scene(SCENE_MENU)

    # --------------------------------------------------
    # Event
    # --------------------------------------------------

    def handle_event(self, event):

        self.back_button.handle_event(event)

    # --------------------------------------------------
    # Update
    # --------------------------------------------------

    def update(self, dt):

        self.back_button.update()

    # --------------------------------------------------
    # Draw
    # --------------------------------------------------

    def draw(self, screen):

        screen.fill(WHITE)

        title = self.title_font.render(
            "CẤU HÌNH",
            True,
            BLACK,
        )

        title_rect = title.get_rect(
            center=(WINDOW_WIDTH // 2, 100)
        )

        screen.blit(title, title_rect)

        info = self.button_font.render(
            "Teacher Config sẽ được xây dựng ở PR-008",
            True,
            BLACK,
        )

        info_rect = info.get_rect(
            center=(WINDOW_WIDTH // 2, 220)
        )

        screen.blit(info, info_rect)

        self.back_button.draw(screen)
