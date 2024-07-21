# src/ui/content_view.py
import customtkinter as ctk
from ..config import Config
from .base_view import BaseView
from PIL import Image
from ..utils.debug import debug_print

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
                                      fg_color=("#EAEAEA", "#232323"),
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
                                    fg_color=("#FFFFFF", "#3A3A3A"),
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
        self.home_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+'menuBar/light/home-96.png'),
                                       dark_image=Image.open(Config.APP_IMAGES_PATH+'menuBar/dark/home-96.png'),
                                       size=(48, 48))
        self.players_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+"menuBar/light/person-90.png"),
                                          dark_image=Image.open(Config.APP_IMAGES_PATH+"menuBar/dark/person-90.png"),
                                          size=(48, 48))
        self.teams_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+"menuBar/light/user-groups-90.png"),
                                        dark_image=Image.open(Config.APP_IMAGES_PATH+"menuBar/dark/user-groups-90.png"),
                                        size=(48, 48))
        self.event_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+"menuBar/light/trophy-90.png"),
                                        dark_image=Image.open(Config.APP_IMAGES_PATH+"menuBar/dark/trophy-90.png"),
                                        size=(48, 48))
        self.leaderboard_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+"menuBar/light/leaderboard-90.png"),
                                              dark_image=Image.open(Config.APP_IMAGES_PATH+"menuBar/dark/leaderboard-90.png"),
                                              size=(48, 48))
        self.light_mode_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+"menuBar/light/light-mode-78.png"),
                                             dark_image=Image.open(Config.APP_IMAGES_PATH+"menuBar/dark/light-mode-78.png"),
                                             size=(48, 48))
        self.dark_mode_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+"menuBar/light/dark-mode-96.png"),
                                            dark_image=Image.open(Config.APP_IMAGES_PATH+"menuBar/dark/dark-mode-96.png"),
                                            size=(32, 32))

        self.logout_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+"menuBar/light/logout-90.png"),
                                         dark_image=Image.open(Config.APP_IMAGES_PATH+"menuBar/dark/logout-90.png"),
                                         size=(48, 48))

    def createMenuButtons(self):
        self.createImages()

        font = (Config.CUSTOM_FONTS_PATH+"Product-Sans-Regular.ttf", Config.MENUBAR_FONTSIZE, "bold")

        self.homeButton = ctk.CTkButton(self.menuBar,
                                        text="Inicio",
                                        font=font,
                                        text_color=("#000000", "#FFFFFF"),
                                        fg_color="transparent",
                                        image=self.home_image)
        self.homeButton.pack(pady=10, padx=10, fill='x')

        debug_print(self.homeButton._font)

        self.playersButton = ctk.CTkButton(self.menuBar,
                                           text="Jugadores",
                                           font=("Helvetica", Config.MENUBAR_FONTSIZE),
                                           text_color=("#000000", "#FFFFFF"),
                                           fg_color="transparent",
                                           image=self.players_image)
        self.playersButton.pack(pady=10, padx=10, fill='x')

        self.teamsButton = ctk.CTkButton(self.menuBar,
                                         text="Equipos",
                                         font=("Helvetica", Config.MENUBAR_FONTSIZE),
                                         text_color=("#000000", "#FFFFFF"),
                                         fg_color="transparent",
                                         image=self.teams_image)
        self.teamsButton.pack(pady=10, padx=10, fill='x')

        self.eventButton = ctk.CTkButton(self.menuBar,
                                         text="Eventos",
                                         font=("Helvetica", Config.MENUBAR_FONTSIZE),
                                         text_color=("#000000", "#FFFFFF"),
                                         fg_color="transparent",
                                         image=self.event_image)
        self.eventButton.pack(pady=10, padx=10, fill='x')

        self.leaderboardButton = ctk.CTkButton(self.menuBar,
                                               text="Clasificación",
                                               font=("Helvetica", Config.MENUBAR_FONTSIZE),
                                               text_color=("#000000", "#FFFFFF"),
                                               fg_color="transparent",
                                               image=self.leaderboard_image)
        self.leaderboardButton.pack(pady=10, padx=10, fill='x')

        themeFrame = ctk.CTkFrame(self.menuBar,
                                  fg_color="transparent",
                                  border_width=self.border_width,
                                  border_color=self.border_color)
        themeFrame.pack(pady=10, padx=10, fill='x')
        themeFrame.grid_columnconfigure(0, weight=1)
        themeFrame.grid_columnconfigure(1, weight=1)
        themeFrame.grid_rowconfigure(0, weight=0)
        # themeFrame.grid_propagate(False)

        self.lightModeButton = ctk.CTkButton(themeFrame,
                                             text="",
                                             fg_color="transparent",
                                             image=self.light_mode_image,
                                             width=48,
                                             height=48,
                                             command=lambda: self.toggle_theme("light"))
        self.lightModeButton.grid(row=0, column=0, pady=10, padx=10)
        self.lightModeButton.grid_propagate(False)

        self.darkModeButton = ctk.CTkButton(themeFrame,
                                            text="",
                                            fg_color="transparent",
                                            image=self.dark_mode_image,
                                            width=48,
                                            height=48,
                                            command=lambda: self.toggle_theme("dark"))
        self.darkModeButton.grid(row=0, column=1, pady=10, padx=10)
        self.darkModeButton.grid_propagate(False)

        self.update_theme_button()

        self.logoutButton = ctk.CTkButton(self.menuBar,
                                          text="Salir",
                                          font=("Helvetica", Config.MENUBAR_FONTSIZE),
                                          text_color=("#000000", "#FFFFFF"),
                                          fg_color="transparent",
                                          image=self.logout_image)
        self.logoutButton.pack(pady=10, padx=10, fill='x')

    def toggle_theme(self, new_theme: str):
        if new_theme not in ["light", "dark"]:
            debug_print("ROSSMAN USA LIGHT O DARK")
            return

        if Config.current_theme == new_theme:
            return

        Config.current_theme = new_theme
        self.update_theme_button()
        ctk.set_appearance_mode(new_theme)

    def update_theme_button(self):
        # Update button images and highlight the active theme
        if Config.current_theme == "light":
            self.lightModeButton.configure(border_color="#3A3A3A", border_width=2)
            self.darkModeButton.configure(border_color="#FFFFFF", border_width=0)
        elif Config.current_theme == "dark":
            self.lightModeButton.configure(border_color="#3A3A3A", border_width=0)
            self.darkModeButton.configure(border_color="#FFFFFF", border_width=2)
        else:
            debug_print("CURRENT THEME NOOOOOOO")
