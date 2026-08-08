"""
TrainBuilder
Train System
"""

import pygame

from src.core.layout import TRAIN_AREA


class TrainSystem:
    """Quản lý đoàn tàu."""

    TRAIN_SPEED = 300  # pixel/giây

    def __init__(self, game):

        self.game = game

        # Asset
        self.engine = None
        self.wagon = None

        # Kích thước placeholder
        self.engine_size = (120, 80)
        self.wagon_size = (90, 70)

        # Vị trí
        self.engine_rect = pygame.Rect(
            TRAIN_AREA.left - 500,
            TRAIN_AREA.centery - 40,
            *self.engine_size
        )

        self.wagons = []

        self._create_wagons()

    # --------------------------------------------------
    # Initialize
    # --------------------------------------------------

    def _create_wagons(self):

        self.wagons.clear()

        spacing = 20

        x = self.engine_rect.left

        for _ in range(3):

            x -= self.wagon_size[0] + spacing

            wagon = pygame.Rect(
                x,
                TRAIN_AREA.centery - 35,
                *self.wagon_size
            )

            self.wagons.append(wagon)

    # --------------------------------------------------
    # Event
    # --------------------------------------------------

    def handle_event(self, event):
        pass

    # --------------------------------------------------
    # Update
    # --------------------------------------------------

    def update(self, dt):

        self.engine_rect.x += self.TRAIN_SPEED * dt

        spacing = 20

        x = self.engine_rect.left

        for wagon in self.wagons:

            x -= wagon.width + spacing

            wagon.x = x
            wagon.y = self.engine_rect.y + 5

    # --------------------------------------------------
    # Draw
    # --------------------------------------------------

    def draw(self, screen):

        # Đầu tàu
        pygame.draw.rect(
            screen,
            (220, 60, 60),
            self.engine_rect,
            border_radius=12
        )

        # Toa
        for wagon in self.wagons:

            pygame.draw.rect(
                screen,
                (80, 120, 220),
                wagon,
                border_radius=10
            )
