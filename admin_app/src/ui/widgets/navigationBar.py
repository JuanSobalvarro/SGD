import customtkinter as ctk
from ...config import Config
from ...utils.debug import debug_print
from PIL import Image
from typing import Literal


class NavigationBar(ctk.CTkFrame):

    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app

        self._border_color: str = None
        self._border_width: int = None

        self.__borderProperties("#123456", 1)

        self._createNavBar()

    def __borderProperties(self, color: str, width: int):
        # Set border properties for debugging
        self._border_color = color if Config.DEBUG else None
        self._border_width = width if Config.DEBUG else 0

    def _createNavBar(self):
        self.navBar = ctk.CTkFrame(self,
                                    fg_color=("#FFFFFF", "#3A3A3A"),
                                    width=200,
                                    corner_radius=31,
                                    border_width=0,)
        self.navBar.pack(fill="y", expand=True, padx=5, pady=5)
        self.navBar.grid_propagate(False)
        self.navBar.pack_propagate(False)

        # Add buttons or other widgets to the menu bar
        self._createMenuButtons()

    def _createImages(self):
        self.home_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+'navBar/light/home-96.png'),
                                       dark_image=Image.open(Config.APP_IMAGES_PATH+'navBar/dark/home-96.png'),
                                       size=(48, 48))
        self.players_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+"navBar/light/person-90.png"),
                                          dark_image=Image.open(Config.APP_IMAGES_PATH+"navBar/dark/person-90.png"),
                                          size=(48, 48))
        self.teams_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+"navBar/light/user-groups-90.png"),
                                        dark_image=Image.open(Config.APP_IMAGES_PATH+"navBar/dark/user-groups-90.png"),
                                        size=(48, 48))
        self.event_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+"navBar/light/trophy-90.png"),
                                        dark_image=Image.open(Config.APP_IMAGES_PATH+"navBar/dark/trophy-90.png"),
                                        size=(48, 48))
        self.leaderboard_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+"navBar/light/leaderboard-90.png"),
                                              dark_image=Image.open(Config.APP_IMAGES_PATH+"navBar/dark/leaderboard-90.png"),
                                              size=(48, 48))
        self.light_mode_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+"navBar/light/light-mode-78.png"),
                                             dark_image=Image.open(Config.APP_IMAGES_PATH+"navBar/dark/light-mode-78.png"),
                                             size=(48, 48))
        self.dark_mode_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+"navBar/light/dark-mode-96.png"),
                                            dark_image=Image.open(Config.APP_IMAGES_PATH+"navBar/dark/dark-mode-96.png"),
                                            size=(32, 32))

        self.logout_image = ctk.CTkImage(light_image=Image.open(Config.APP_IMAGES_PATH+"navBar/light/logout-90.png"),
                                         dark_image=Image.open(Config.APP_IMAGES_PATH+"navBar/dark/logout-90.png"),
                                         size=(48, 48))

    def _createMenuButtons(self):
        self._createImages()

        font = (Config.CUSTOM_FONTS_PATH+"Product-Sans-Regular.ttf", Config.MENUBAR_FONTSIZE, "bold")

        self.homeButton = ctk.CTkButton(self.navBar,
                                        text="Inicio",
                                        font=font,
                                        text_color=("#000000", "#FFFFFF"),
                                        fg_color="transparent",
                                        image=self.home_image)
        self.homeButton.pack(pady=10, padx=10, fill='x')

        debug_print(self.homeButton._font)

        self.playersButton = ctk.CTkButton(self.navBar,
                                           text="Jugadores",
                                           font=("Helvetica", Config.MENUBAR_FONTSIZE),
                                           text_color=("#000000", "#FFFFFF"),
                                           fg_color="transparent",
                                           image=self.players_image)
        self.playersButton.pack(pady=10, padx=10, fill='x')

        self.teamsButton = ctk.CTkButton(self.navBar,
                                         text="Equipos",
                                         font=("Helvetica", Config.MENUBAR_FONTSIZE),
                                         text_color=("#000000", "#FFFFFF"),
                                         fg_color="transparent",
                                         image=self.teams_image)
        self.teamsButton.pack(pady=10, padx=10, fill='x')

        self.eventButton = ctk.CTkButton(self.navBar,
                                         text="Eventos",
                                         font=("Helvetica", Config.MENUBAR_FONTSIZE),
                                         text_color=("#000000", "#FFFFFF"),
                                         fg_color="transparent",
                                         image=self.event_image)
        self.eventButton.pack(pady=10, padx=10, fill='x')

        self.leaderboardButton = ctk.CTkButton(self.navBar,
                                               text="Clasificación",
                                               font=("Helvetica", Config.MENUBAR_FONTSIZE),
                                               text_color=("#000000", "#FFFFFF"),
                                               fg_color="transparent",
                                               image=self.leaderboard_image)
        self.leaderboardButton.pack(pady=10, padx=10, fill='x')

        themeFrame = ctk.CTkFrame(self.navBar,
                                  fg_color="transparent",
                                  border_width=self._border_width,
                                  border_color=self._border_color)
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
                                             command=lambda: self.__toggle_theme_callback("light"))
        self.lightModeButton.grid(row=0, column=0, pady=10, padx=10)
        self.lightModeButton.grid_propagate(False)

        self.darkModeButton = ctk.CTkButton(themeFrame,
                                            text="",
                                            fg_color="transparent",
                                            image=self.dark_mode_image,
                                            width=48,
                                            height=48,
                                            command=lambda: self.__toggle_theme_callback("dark"))
        self.darkModeButton.grid(row=0, column=1, pady=10, padx=10)
        self.darkModeButton.grid_propagate(False)

        self._update_theme_button()

        self.logoutButton = ctk.CTkButton(self.navBar,
                                          text="Salir",
                                          font=("Helvetica", Config.MENUBAR_FONTSIZE),
                                          text_color=("#000000", "#FFFFFF"),
                                          fg_color="transparent",
                                          image=self.logout_image)
        self.logoutButton.pack(pady=10, padx=10, fill='x')

    def __toggle_theme_callback(self, theme: Literal["light", "dark"]):
        self.app.toggle_theme(theme)
        self._update_theme_button()

    def _update_theme_button(self):
        # Update button images and highlight the active theme
        if Config.current_theme == "light":
            self.lightModeButton.configure(border_color="#3A3A3A", border_width=2)
            self.darkModeButton.configure(border_color="#FFFFFF", border_width=0)
        elif Config.current_theme == "dark":
            self.lightModeButton.configure(border_color="#3A3A3A", border_width=0)
            self.darkModeButton.configure(border_color="#FFFFFF", border_width=2)
        else:
            debug_print("CURRENT THEME NOOOOOOO")

    def _destroy_navbar(self):
        self.navBar.destroy()
