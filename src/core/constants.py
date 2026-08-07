"""
TrainBuilder
Core Constants

Author: Minh Thắng & ChatGPT
"""

from pathlib import Path

# ============================================================
# Game Information
# ============================================================

GAME_TITLE = "TrainBuilder"

GAME_VERSION = "0.1.0-alpha"

FPS = 60

# ============================================================
# Window
# ============================================================

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

# ============================================================
# Assets
# ============================================================

ROOT_DIR = Path(__file__).resolve().parents[2]

ASSET_DIR = ROOT_DIR / "assets"

BACKGROUND_DIR = ASSET_DIR / "backgrounds"
TRAIN_DIR = ASSET_DIR / "train"
BUILDING_DIR = ASSET_DIR / "buildings"
MATERIAL_DIR = ASSET_DIR / "materials"
UI_DIR = ASSET_DIR / "ui"
AUDIO_DIR = ASSET_DIR / "audio"
EFFECT_DIR = ASSET_DIR / "effects"

# ============================================================
# Config
# ============================================================

CONFIG_DIR = ROOT_DIR / "config"

GAME_CONFIG = CONFIG_DIR / "game_config.json"

TEACHER_CONFIG = CONFIG_DIR / "teacher_config.json"

# ============================================================
# Data
# ============================================================

DATA_DIR = ROOT_DIR / "data"

BUILDING_DATA = DATA_DIR / "buildings.json"

MATERIAL_DATA = DATA_DIR / "materials.json"

# ============================================================
# Scene IDs
# ============================================================

SCENE_MENU = "menu"

SCENE_CONFIG = "config"

SCENE_GAMEPLAY = "gameplay"

SCENE_RESULT = "result"

# ============================================================
# Game States
# ============================================================

STATE_MENU = "menu"

STATE_INTRO = "intro"

STATE_BUILDING = "building"

STATE_COUNTDOWN = "countdown"

STATE_QUESTION = "question"

STATE_BUILD = "build"

STATE_RESULT = "result"

# ============================================================
# Colors
# ============================================================

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

RED = (255, 0, 0)

GREEN = (0, 220, 0)

BLUE = (0, 120, 255)

YELLOW = (255, 220, 0)

GRAY = (180, 180, 180)

LIGHT_GRAY = (230, 230, 230)

# ============================================================
# Animation
# ============================================================

TRAIN_SPEED = 280

COUNTDOWN_TIME = 3

BUILD_TIME = 3

SHAKE_DISTANCE = 8

SHAKE_DURATION = 0.25

# ============================================================
# Audio
# ============================================================

DEFAULT_VOLUME = 0.8

# ============================================================
# Gameplay
# ============================================================

DEFAULT_WAGON_COUNT = 3

MAX_MATERIAL_OPTIONS = 10

MATERIAL_MIN_NUMBER = 0

MATERIAL_MAX_NUMBER = 9

# ============================================================
# Font
# ============================================================

DEFAULT_FONT_SIZE = 36

TITLE_FONT_SIZE = 64

QUESTION_FONT_SIZE = 56
