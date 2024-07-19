import customtkinter as ctk
from ..config import Config


class BaseView(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.mainFrame: ctk.CTkFrame = None

        if Config.DEBUG:
            self._border_width = 1

    def borderProperties(self, color: str, width: int):
        # Set border properties for debugging
        self.border_color = color if Config.DEBUG else None
        self.border_width = width if Config.DEBUG else 0

    def showView(self):
        pass
