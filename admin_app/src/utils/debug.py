from ..config import Config


def debug_print(message: str):
    if Config.DEBUG:
        print(f"DEBUG: {message}")