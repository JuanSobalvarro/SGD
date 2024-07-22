# src/ui/contents/players_content.py
from .base_content import BaseContent
import customtkinter as ctk


class PlayersContent(BaseContent):
    def __init__(self, parent):
        super().__init__(parent)

        self.border_properties("#777700", 1)

    def createContent(self):
        pass

    def showContent(self):
        self.createContent()

    def hideContent(self):
        self.clearContent()
