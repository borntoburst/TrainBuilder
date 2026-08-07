"""
TrainBuilder
Gameplay Scene
"""

import pygame

from src.scenes.base_scene import BaseScene
from src.core.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WHITE,
    BLACK,
)


class GameplayScene(BaseScene):

    def __init__(self, scene_manager):

        super().__init__(scene_manager)

        self.game = scene_manager.game

        self.background = None

        self.title_font = None

        # Placeholder
        self.train_position = (150, 520)
        self.building_position = (950, 180)
        self.question_position = (WINDOW_WIDTH // 2, 70)
        self.material_position = (WINDOW_WIDTH // 2, 620)

    # --------------------------------------------------
    # Scene Lifecycle
    # --------------------------------------------------

    def enter(self):

        if self.title_font is None:

            self.title_font = self.game.assets.get_system_font(
                "arial",
                36,
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

        self._draw_placeholder(screen)

    # --------------------------------------------------
    # Debug Placeholder
    # --------------------------------------------------

    def _draw_placeholder(self, screen):

        # Question Area
        pygame.draw.rect(
            screen,
            (220, 220, 220),
            (240, 20, 800, 80),
            border_radius=10,
        )

        question = self.title_font.render(
            "QUESTION AREA",
            True,
            BLACK,
        )

        screen.blit(
            question,
            question.get_rect(center=self.question_position),
        )

        # Building Area
        pygame.draw.rect(
            screen,
            (210, 240, 210),
            (850, 130, 320, 250),
            border_radius=10,
        )

        building = self.title_font.render(
            "BUILDING",
            True,
            BLACK,
        )

        screen.blit(
            building,
            building.get_rect(center=self.building_position),
        )

        # Train Area
        pygame.draw.rect(
            screen,
            (210, 230, 255),
            (60, 450, 760, 170),
            border_radius=10,
        )

        train = self.title_font.render(
            "TRAIN",
            True,
            BLACK,
        )

        screen.blit(
            train,
            train.get_rect(center=self.train_position),
        )

        # Material Area
        pygame.draw.rect(
            screen,
            (255, 240, 200),
            (180, 600, 900, 90),
            border_radius=10,
        )

        material = self.title_font.render(
            "MATERIAL AREA",
            True,
            BLACK,
        )

        screen.blit(
            material,
            material.get_rect(center=self.material_position),
        )
