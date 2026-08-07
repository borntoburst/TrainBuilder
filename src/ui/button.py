"""
TrainBuilder
Button UI Component
"""

import pygame


class Button:

    def __init__(
        self,
        text,
        x,
        y,
        width,
        height,
        callback,
        font,
        bg_color=(70, 130, 180),
        hover_color=(100, 160, 210),
        text_color=(255, 255, 255),
        border_radius=12,
    ):

        self.text = text

        self.rect = pygame.Rect(x, y, width, height)

        self.callback = callback

        self.font = font

        self.bg_color = bg_color

        self.hover_color = hover_color

        self.text_color = text_color

        self.border_radius = border_radius

        self.hover = False

    def handle_event(self, event):

        if event.type == pygame.MOUSEMOTION:
            self.hover = self.rect.collidepoint(event.pos)

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1 and self.hover:
                self.callback()

    def update(self):
        pass

    def draw(self, screen):

        color = self.hover_color if self.hover else self.bg_color

        pygame.draw.rect(
            screen,
            color,
            self.rect,
            border_radius=self.border_radius,
        )

        text_surface = self.font.render(
            self.text,
            True,
            self.text_color,
        )

        text_rect = text_surface.get_rect(
            center=self.rect.center
        )

        screen.blit(text_surface, text_rect)
