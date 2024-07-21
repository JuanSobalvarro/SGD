# src/config.py
import os

from django.core.files import images


class Config(object):
    """
    Configuration settings and constants
    """
    APP_TITLE = "SGD Admin App"
    APP_GEOMETRY = "1280x720"
    APP_IMAGES_PATH = os.path.join(os.path.dirname(__file__), "images", "")
    APP_THEME_PATH = os.path.join(os.path.dirname(__file__), "themes\\moderntk.json")
    APP_MIN_WIDTH = 720
    APP_MIN_HEIGHT = 480
    APP_SPORTS_AVAILABLE = ["Tenis de Mesa", "Fútbol"]

    MENUBAR_FONTSIZE = 16
    COLOR_GREEN = "#238937"
    current_theme = "light"

    # Load custom font
    CUSTOM_FONTS_PATH = os.path.join(os.path.dirname(__file__), "fonts", "")

    DEBUG = False