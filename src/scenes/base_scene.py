"""
TrainBuilder
Base Scene
"""


class BaseScene:

    def __init__(self, scene_manager):
        self.scene_manager = scene_manager

    def enter(self):
        """
        Được gọi khi Scene được mở.
        """
        pass

    def exit(self):
        """
        Được gọi trước khi rời Scene.
        """
        pass

    def handle_event(self, event):
        """
        Xử lý sự kiện.
        """
        pass

    def update(self, dt):
        """
        Cập nhật logic.
        """
        pass

    def draw(self, screen):
        """
        Vẽ Scene.
        """
        pass
