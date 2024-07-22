# src/ui/contents/teams_content.py
from .base_content import BaseContent
import customtkinter as ctk


class TeamsContent(BaseContent):
    def __init__(self, parent):
        super().__init__(parent)

        self.border_properties("#11AADD", 1)

    def createContent(self):
        pass

    def showContent(self):
        self.createContent()

    def hideContent(self):
        self.clearContent()
