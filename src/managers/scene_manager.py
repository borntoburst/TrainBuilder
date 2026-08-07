"""
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

    def __init__(self, game):

        self.game = game

        self.current_scene = None

        self.scenes = {}

        self._register_scenes()

        self.change_scene(SCENE_MENU)

    def _register_scenes(self):

        self.scenes = {

            SCENE_MENU: MenuScene(self),

            SCENE_CONFIG: ConfigScene(self),

            SCENE_GAMEPLAY: GameplayScene(self),

            SCENE_RESULT: ResultScene(self),

        }

    def change_scene(self, scene_name):

        scene = self.scenes.get(scene_name)

        if scene is None:
            raise ValueError(f"Scene '{scene_name}' does not exist.")

        if self.current_scene is not None:
            self.current_scene.exit()

        self.current_scene = scene

        self.current_scene.enter()

    def handle_event(self, event):

        if self.current_scene:
            self.current_scene.handle_event(event)

    def update(self, dt):

        if self.current_scene:
            self.current_scene.update(dt)

    def draw(self, screen):

        if self.current_scene:
            self.current_scene.draw(screen)
