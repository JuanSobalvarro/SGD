# src/ui/contents/content_view.py
import customtkinter as ctk
from ...config import Config
from .base_view import BaseView
from ...utils.debug import debug_print
from typing import Literal, Any

# Import Contents
from ..contents.home_content import HomeContent
from ..widgets.navigationBar import NavigationBar

class ButtonsCommands:
    def __init__(self):
        pass


class ContentView(BaseView):
    def __init__(self, parent, app: ctk.CTk):
        super().__init__(parent, app)

        self.mainFrame: ctk.CTkFrame

        self.navBarFrame: ctk.CTkFrame
        self.contentFrame: ctk.CTkFrame

        self.borderProperties("#9900FF", 1)

        self.contents: dict[str, Any] = {}
        self.currentContent: Any = None

        self._create_widgets()

    def _create_widgets(self):
        self.mainFrame = ctk.CTkFrame(self,
                                      fg_color=("#EAEAEA", "#232323"),
                                      border_width=self.border_width,
                                      border_color=self.border_color)
        self.mainFrame.pack(fill='both', expand=True)

        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=0)
        self.mainFrame.grid_columnconfigure(1, weight=1)

        self.navBarFrame = ctk.CTkFrame(self.mainFrame,
                                         fg_color="transparent",
                                         border_width=self.border_width,
                                         border_color=self.border_color)
        self.navBarFrame.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)

        self.navBar = NavigationBar(self.navBarFrame,
                                    self.app)
        self.navBar.pack(fill="both", expand=True)

        self._createContentFrame()
        self._create_contents()

    def _createContentFrame(self):
        self.contentFrame = ctk.CTkFrame(self.mainFrame,
                                         fg_color="transparent",
                                         border_width=self.border_width,
                                         border_color=self.border_color)
        self.contentFrame.grid(row=0, column=1, sticky="nsew", padx=50, pady=50)

    def _create_contents(self):
        for C in (HomeContent, ):
            content_name = C.__name__
            content = C(parent=self.contentFrame)  # Pass the controller (self) to each view
            self.contents[content_name] = content

    def _showContent(self, content_name: str):
        debug_print(f"Showing content {content_name}")

        if self.currentContent is not None:
            self._removeContent(content_name)

        self.currentContent = self.contents[content_name]

        self.currentContent.showContent()
        self.currentContent.pack(fill='both', expand=True)

    def _removeContent(self, content_name: str):
        self.contents[content_name].destroy()

    def showView(self):
        self._showContent("HomeContent")
