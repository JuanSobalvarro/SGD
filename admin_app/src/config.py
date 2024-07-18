# src/config.py
import os


class Config(object):
    """
    Configuration settings and constants
    """
    APP_TITLE = "SGD Admin App"
    APP_GEOMETRY = "1280x720"
    APP_THEME_PATH = os.path.join(os.path.dirname(__file__), "themes\\white.json")
    APP_MIN_WIDTH = 970
    APP_MIN_HEIGHT = 460
    DEBUG = True