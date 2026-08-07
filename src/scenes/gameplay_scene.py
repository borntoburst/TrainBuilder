"""
TrainBuilder
Gameplay Scene
"""

import pygame

from src.scenes.base_scene import BaseScene

from src.core.constants import (
    WHITE,
    BLACK,
)

from src.core.layout import (
    QUESTION_AREA,
    BUILDING_AREA,
    TRAIN_AREA,
    MATERIAL_AREA,
)


class GameplayScene(BaseScene):

    def __init__(self, scene_manager):

        super().__init__(scene_manager)

        self.game = scene_manager.game

        self.background = None
        self.font = None

    # --------------------------------------------------
    # Scene Lifecycle
    # --------------------------------------------------

    def enter(self):

        if self.font is None:

            self.font = self.game.assets.get_system_font(
                "arial",
                32,
                bold=True,
            )

        if self.game.assets.has_image("backgrounds/gameplay"):

            self.background = self.game.assets.get_image(
                "backgrounds/gameplay"
            )

    def exit(self):
        pass

    # --------------------------------------------------
    # Event
    # --------------------------------------------------

    def handle_event(self, event):
        pass

    # --------------------------------------------------
    # Update
    # --------------------------------------------------

    def update(self, dt):
        pass

    # --------------------------------------------------
    # Draw
    # --------------------------------------------------

    def draw(self, screen):

        if self.background:

            screen.blit(self.background, (0, 0))

        else:

            screen.fill(WHITE)

        self.draw_question_area(screen)
        self.draw_building_area(screen)
        self.draw_train_area(screen)
        self.draw_material_area(screen)

    # --------------------------------------------------
    # Draw Area
    # --------------------------------------------------

    def draw_question_area(self, screen):

        pygame.draw.rect(
            screen,
            (230, 230, 230),
            QUESTION_AREA,
            border_radius=12,
        )

        self.draw_text(
            screen,
            "QUESTION AREA",
            QUESTION_AREA.center,
        )

    def draw_building_area(self, screen):

        pygame.draw.rect(
            screen,
            (210, 240, 210),
            BUILDING_AREA,
            border_radius=12,
        )

        self.draw_text(
            screen,
            "BUILDING",
            BUILDING_AREA.center,
        )

    def draw_train_area(self, screen):

        pygame.draw.rect(
            screen,
            (210, 225, 255),
            TRAIN_AREA,
            border_radius=12,
        )

        self.draw_text(
            screen,
            "TRAIN",
            TRAIN_AREA.center,
        )

    def draw_material_area(self, screen):

        pygame.draw.rect(
            screen,
            (255, 240, 200),
            MATERIAL_AREA,
            border_radius=12,
        )

        self.draw_text(
            screen,
            "MATERIAL",
            MATERIAL_AREA.center,
        )

    # --------------------------------------------------
    # Helper
    # --------------------------------------------------

    def draw_text(self, screen, text, center):

        surface = self.font.render(
            text,
            True,
            BLACK,
        )

        rect = surface.get_rect(center=center)

        screen.blit(surface, rect)
