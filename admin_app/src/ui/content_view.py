# src/ui/content_view.py
import customtkinter as ctk
from ..config import Config
from .base_view import BaseView
from PIL import Image

class ButtonsCommands:
    def __init__(self):
        pass



class ContentView(BaseView):
    def __init__(self, parent, app):
        super().__init__(parent, app)

        self.menuBar: ctk.CTkFrame = None
        self.contentFrame: ctk.CTkFrame = None

        self.borderProperties("#9900FF", 1)

        self.create_widgets()

    def create_widgets(self):
        self.mainFrame = ctk.CTkFrame(self,
                                      fg_color="#EAEAEA",
                                      border_width=self.border_width,
                                      border_color=self.border_color)
        self.mainFrame.pack(fill='both', expand=True)

        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=0)
        self.mainFrame.grid_columnconfigure(1, weight=1)

        self.createMenuBar()
        self.createContent()

    def createMenuBar(self):
        self.menuBarFrame = ctk.CTkFrame(self.mainFrame,
                                         fg_color="transparent",
                                         border_width=self.border_width,
                                         border_color=self.border_color)
        self.menuBarFrame.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)

        self.menuBar = ctk.CTkFrame(self.menuBarFrame,
                                    fg_color="#FFFFFF",
                                    width=200,
                                    corner_radius=31,
                                    border_width=self.border_width,
                                    border_color=self.border_color)
        self.menuBar.pack(fill="y", expand=True, padx=5, pady=5)
        self.menuBar.grid_propagate(False)
        self.menuBar.pack_propagate(False)

        # Add buttons or other widgets to the menu bar
        self.createMenuButtons()

    def createContent(self):
        self.contentFrame = ctk.CTkFrame(self.mainFrame,
                                         fg_color="transparent",
                                         border_width=self.border_width,
                                         border_color=self.border_color)
        self.contentFrame.grid(row=0, column=1, sticky="nsew", padx=50, pady=50)

    def createImages(self):
        self.default_avatar_image = ctk.CTkImage(Image.open(Config.APP_IMAGES_PATH+'menuBar/default_avatar.png'), size=(80, 80))

    def createMenuButtons(self):
        self.createImages()
        self.homeButton = ctk.CTkButton(self.menuBar,
                                        text="Home",
                                        font=("Helvetica", 25),
                                        text_color=("#000000", "#FFFFFF"),
                                        fg_color="transparent",
                                        image=self.default_avatar_image)
        self.homeButton.pack(pady=10, padx=10, fill='x')
