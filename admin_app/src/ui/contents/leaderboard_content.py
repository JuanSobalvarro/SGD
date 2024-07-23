# src/ui/contents/leaderboard_content.py
from .base_content import BaseContent
import customtkinter as ctk
from ..widgets.separator import HorizontalSeparator


class LeaderboardContent(BaseContent):
    def __init__(self, parent):
        super().__init__(parent)

        self.right_frame: ctk.CTkFrame = None
        self.left_frame: ctk.CTkFrame = None

        self.border_properties("#FFCF00", 1)

    def _createContent(self):
        # always pack to parent
        self.pack_to_parent()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.configure(fg_color=("#FFFFFF", "#3A3A3A"),
                       corner_radius=31,)

        self.__createLeftFrame()
        self.__createRightFrame()

    def __createLeftFrame(self):
        self.left_frame = ctk.CTkFrame(self,
                                       corner_radius=31,
                                       border_width=self.border_width,
                                       border_color=self.border_color)
        self.left_frame.grid(row=0, column=1, sticky="nsew", padx=50, pady=50)

        self.left_frame.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(self.left_frame,
                                   fg_color="transparent",
                                   text="Top De Jugadores",
                                   font=("Arial", 26, "bold"),)
        title_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        separator = HorizontalSeparator(self.left_frame,
                                        thick=2,
                                        color=("#49454F", "#FFFFFF"))
        separator.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    def __createRightFrame(self):
        self.right_frame = ctk.CTkFrame(self,
                                        corner_radius=31,
                                        border_width=self.border_width,
                                        border_color=self.border_color)
        self.right_frame.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)

        self.right_frame.grid_columnconfigure(0, weight=1)
        # self.right_frame.grid_columnconfigure(1, weight=0)

        title_label = ctk.CTkLabel(self.right_frame,
                                   fg_color="transparent",
                                   text="Top De Equipos",
                                   font=("Arial", 26, "bold"),)
        title_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        separator = HorizontalSeparator(self.right_frame,
                                        thick=2,
                                        color=("#49454F", "#FFFFFF"))
        separator.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    def showContent(self):
        self._createContent()

    def hideContent(self):
        self.clearContent()
