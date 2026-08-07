"""
TrainBuilder
Asset Manager
"""

from pathlib import Path
import pygame


class AssetManager:

    def __init__(self, asset_root):

        self.asset_root = Path(asset_root)

        self.images = {}

        self.fonts = {}

        self.sounds = {}

    # =====================================================
    # IMAGE
    # =====================================================

    def load_image(self, name, relative_path):

        path = self.asset_root / relative_path

        image = pygame.image.load(path).convert_alpha()

        self.images[name] = image

        return image

    def get_image(self, name):

        if name not in self.images:
            raise KeyError(f"Image '{name}' has not been loaded.")

        return self.images[name]

    # =====================================================
    # FONT
    # =====================================================

    def load_font(self, name, relative_path, size):

        path = self.asset_root / relative_path

        font = pygame.font.Font(path, size)

        self.fonts[name] = font

        return font

    def load_system_font(self, name, font_name, size, bold=False):

        font = pygame.font.SysFont(font_name, size, bold)

        self.fonts[name] = font

        return font

    def get_font(self, name):

        if name not in self.fonts:
            raise KeyError(f"Font '{name}' has not been loaded.")

        return self.fonts[name]

    # =====================================================
    # SOUND
    # =====================================================

    def load_sound(self, name, relative_path):

        path = self.asset_root / relative_path

        sound = pygame.mixer.Sound(path)

        self.sounds[name] = sound

        return sound

    def get_sound(self, name):

        if name not in self.sounds:
            raise KeyError(f"Sound '{name}' has not been loaded.")

        return self.sounds[name]
