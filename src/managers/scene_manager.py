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

    def __init__(self, app):

        self.app = app

        self.scenes = {}

        self.current_scene = None

        self._load_scenes()

        self.change_scene(SCENE_MENU)

    def _load_scenes(self):

        self.scenes[SCENE_MENU] = MenuScene(self.app)

        self.scenes[SCENE_CONFIG] = ConfigScene(self.app)

        self.scenes[SCENE_GAMEPLAY] = GameplayScene(self.app)

        self.scenes[SCENE_RESULT] = ResultScene(self.app)

    def change_scene(self, scene_name):

        if scene_name not in self.scenes:
            raise ValueError(f"Scene '{scene_name}' does not exist.")

        self.current_scene = self.scenes[scene_name]

        self.current_scene.enter()

    def handle_event(self, event):

        self.current_scene.handle_event(event)

    def update(self, dt):

        self.current_scene.update(dt)

    def draw(self, screen):

        self.current_scene.draw(screen)
