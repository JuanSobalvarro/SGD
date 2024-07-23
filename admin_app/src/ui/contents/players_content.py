# src/ui/contents/players_content.py
from .base_content import BaseContent
import customtkinter as ctk
from ...config import Config
from PIL import Image
from ..widgets.circularButton import CircularButton


class PlayersContent(BaseContent):
    def __init__(self, parent):
        super().__init__(parent)

        self.border_properties("#777700", 1)

    def createContent(self):
        self.pack_to_parent()

        self.configure(fg_color=("#FFFFFF", "#3A3A3A"),
                       corner_radius=31)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.__createHeaderFrame()
        self.__createListFrame()

    def __createHeaderFrame(self):
        self.header_frame = ctk.CTkFrame(self,
                                         fg_color="transparent",
                                         border_width=self.border_width,
                                         border_color=self.border_color)
        self.header_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.header_frame.grid_columnconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(1, weight=3)

        title_label = ctk.CTkLabel(self.header_frame,
                                   text="Lista de Jugadores",
                                   font=("Inter", 36, "bold"),)
        title_label.grid(row=0, column=0, sticky="nsew", padx=20, pady=30)

        ################## CHANGE TO CUSTOM WIDGETS
        self.search_bar = ctk.CTkEntry(self.header_frame,
                                       placeholder_text="Buscar jugador",
                                       corner_radius=20,
                                       height=50,
                                       fg_color=("#F0F0F0", "#333333"),
                                       border_width=self.border_width,
                                       border_color=self.border_color)
        self.search_bar.grid(row=0, column=1, sticky="ew", padx=20, pady=20)

        # self.add_player_button = CircularButton(self.header_frame,
        #                                         light_image_path=Config.APP_IMAGES_PATH+"add/light/add-user-64.png",
        #                                         dark_image_path=Config.APP_IMAGES_PATH+"add/dark/add-user-64.png",
        #                                         size=50,
        #                                         bg_color=("#89ff7f", "#066b00"),)
        # self.add_player_button.grid(row=0, column=2, sticky="ew", padx=20, pady=20)

        add_player_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+"add/light/add-user-64.png"),
                                        dark_image=Image.open(Config.APP_IMAGES_PATH+"add/dark/add-user-64.png"),
                                        size=(30, 30))
        self.add_player_button = ctk.CTkButton(self.header_frame,
                                               text="",
                                               width=30,
                                               height=30,
                                               corner_radius=20,
                                               fg_color=("#89ff7f", "#066b00"),
                                               image=add_player_image,)
        self.add_player_button.grid(row=0, column=2, padx=20, pady=20)

    def __createListFrame(self):
        self.list_frame = ctk.CTkFrame(self,
                                       fg_color="transparent",
                                       border_width=self.border_width,
                                       border_color=self.border_color)
        self.list_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    def showContent(self):
        self.createContent()

    def hideContent(self):
        self.clearContent()
