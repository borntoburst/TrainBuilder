"""
TrainBuilder
Asset Manager

Tự động quét toàn bộ thư mục assets.
Không Scene nào được phép gọi pygame.image.load().
"""

from pathlib import Path

import pygame


class AssetManager:

    IMAGE_EXTENSIONS = {
        ".png",
        ".jpg",
        ".jpeg",
        ".webp",
    }

    SOUND_EXTENSIONS = {
        ".wav",
        ".ogg",
        ".mp3",
    }

    FONT_EXTENSIONS = {
        ".ttf",
        ".otf",
    }

    def __init__(self, asset_root):

        self.asset_root = Path(asset_root)

        self.images = {}

        self.sounds = {}

        self.font_paths = {}

    # =====================================================
    # PUBLIC
    # =====================================================

    def load_all(self):
        """
        Quét toàn bộ thư mục assets.
        """

        if not self.asset_root.exists():
            raise FileNotFoundError(self.asset_root)

        for file in self.asset_root.rglob("*"):

            if not file.is_file():
                continue

            suffix = file.suffix.lower()

            key = file.stem

            if suffix in self.IMAGE_EXTENSIONS:

                self.images[key] = pygame.image.load(file).convert_alpha()

            elif suffix in self.SOUND_EXTENSIONS:

                self.sounds[key] = pygame.mixer.Sound(file)

            elif suffix in self.FONT_EXTENSIONS:

                self.font_paths[key] = file

    # =====================================================
    # IMAGE
    # =====================================================

    def get_image(self, name):

        try:
            return self.images[name]

        except KeyError:
            raise KeyError(f"Image '{name}' not found.")

    def has_image(self, name):

        return name in self.images

    # =====================================================
    # FONT
    # =====================================================

    def get_font(self, name, size):

        if name not in self.font_paths:
            raise KeyError(f"Font '{name}' not found.")

        return pygame.font.Font(self.font_paths[name], size)

    def get_system_font(self, name, size, bold=False):

        return pygame.font.SysFont(name, size, bold)

    # =====================================================
    # SOUND
    # =====================================================

    def get_sound(self, name):

        try:
            return self.sounds[name]

        except KeyError:
            raise KeyError(f"Sound '{name}' not found.")
