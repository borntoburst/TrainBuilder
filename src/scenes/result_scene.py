"""
TrainBuilder
Result Scene
"""

from src.scenes.base_scene import BaseScene
from src.ui.button import Button

from src.core.constants import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WHITE,
    BLACK,
    SCENE_MENU,
    SCENE_GAMEPLAY,
)


class ResultScene(BaseScene):

    def __init__(self, scene_manager):

        super().__init__(scene_manager)

        self.game = scene_manager.game

        self.title_font = None
        self.button_font = None

        self.play_again_button = None
        self.menu_button = None

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

        button_width = 260
        button_height = 70

        center_x = (WINDOW_WIDTH - button_width) // 2

        self.play_again_button = Button(
            text="CHƠI LẠI",
            x=center_x,
            y=320,
            width=button_width,
            height=button_height,
            callback=self.play_again,
            font=self.button_font,
        )

        self.menu_button = Button(
            text="VỀ MENU",
            x=center_x,
            y=420,
            width=button_width,
            height=button_height,
            callback=self.back_to_menu,
            font=self.button_font,
        )

    # --------------------------------------------------
    # Callback
    # --------------------------------------------------

    def play_again(self):

        self.scene_manager.change_scene(
            SCENE_GAMEPLAY
        )

    def back_to_menu(self):

        self.scene_manager.change_scene(
            SCENE_MENU
        )

    # --------------------------------------------------
    # Event
    # --------------------------------------------------

    def handle_event(self, event):

        self.play_again_button.handle_event(event)

        self.menu_button.handle_event(event)

    # --------------------------------------------------
    # Update
    # --------------------------------------------------

    def update(self, dt):

        self.play_again_button.update()

        self.menu_button.update()

    # --------------------------------------------------
    # Draw
    # --------------------------------------------------

    def draw(self, screen):

        screen.fill(WHITE)

        title = self.title_font.render(
            "HOÀN THÀNH!",
            True,
            BLACK,
        )

        title_rect = title.get_rect(
            center=(WINDOW_WIDTH // 2, 150)
        )

        screen.blit(title, title_rect)

        self.play_again_button.draw(screen)

        self.menu_button.draw(screen)
