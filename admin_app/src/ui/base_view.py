import customtkinter as ctk
from ..config import Config

class BaseView(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.mainFrame: ctk.CTkFrame = None

        if Config.DEBUG:
            self._border_width = 1

    def showView(self):
        pass
