"""
TrainBuilder
Scene Manager
"""

from src.core.constants import (
    SCENE_MENU,
    SCENE_CONFIG,
    SCENE_GAMEPLAY,
    SCENE_RESULT,
)

from src.scenes.menu_scene import MenuScene
from src.scenes.config_scene import ConfigScene
from src.scenes.gameplay_scene import GameplayScene
from src.scenes.result_scene import ResultScene


class SceneManager:
    """Quản lý toàn bộ Scene của game."""

    def __init__(self, app):
        self.app = app

        self.scenes = {}
        self.current_scene = None

        self._load_scenes()
        self.change_scene(SCENE_MENU)

    def _load_scenes(self):
        """Khởi tạo toàn bộ Scene."""

        self.scenes = {
            SCENE_MENU: MenuScene(self),
            SCENE_CONFIG: ConfigScene(self),
            SCENE_GAMEPLAY: GameplayScene(self),
            SCENE_RESULT: ResultScene(self),
        }

    def change_scene(self, scene_name):
        """
        Chuyển sang Scene mới.
        """

        scene = self.scenes.get(scene_name)

        if scene is None:
            raise ValueError(f"Scene '{scene_name}' does not exist.")

        # Rời Scene hiện tại
        if self.current_scene is not None:
            self.current_scene.exit()

        # Chuyển Scene
        self.current_scene = scene

        # Khởi tạo Scene mới
        self.current_scene.enter()

    def handle_event(self, event):
        """Chuyển Event cho Scene hiện tại."""

        if self.current_scene is not None:
            self.current_scene.handle_event(event)

    def update(self, dt):
        """Cập nhật Scene hiện tại."""

        if self.current_scene is not None:
            self.current_scene.update(dt)

    def draw(self, screen):
        """Vẽ Scene hiện tại."""

        if self.current_scene is not None:
            self.current_scene.draw(screen)
