# src/ui/sport_selection_view.py
import customtkinter as ctk
from ...config import Config
from .base_view import BaseView


class SportSelectionView(BaseView):
    def __init__(self, parent, app):
        super().__init__(parent, app)

        self.sports: list[str] = Config.APP_SPORTS_AVAILABLE

        self.labelFrame: ctk.CTkFrame = None
        self.buttonsFrame: ctk.CTkFrame = None

        self.borderProperties("#FF0000", 1)

    def create_widgets(self):
        self.mainFrame = ctk.CTkFrame(self,
                                      fg_color="#FFFFFF",
                                      corner_radius=36,
                                      border_width=self.border_width,
                                      border_color=self.border_color)
        self.mainFrame.pack(padx=100, pady=100, fill='both', expand=True)

        self.mainFrame.grid_columnconfigure(0, weight=1)
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_rowconfigure(1, weight=1)

        self.labelFrame = ctk.CTkFrame(self.mainFrame,
                                       border_width=self.border_width,
                                       border_color=self.border_color)
        self.labelFrame.grid(row=0, column=0, sticky='s', padx=10, pady=10)

        self.buttonsFrame = ctk.CTkFrame(self.mainFrame,
                                         border_width=self.border_width,
                                         border_color=self.border_color)
        self.buttonsFrame.grid(row=1, column=0, sticky='n', padx=10, pady=10)

        titleLabel = ctk.CTkLabel(self.labelFrame,
                                  text="Escoja un deporte",
                                  font=("Inter", 36),
                                  justify=ctk.CENTER)
        titleLabel.grid(row=0, column=0, sticky='s', padx=10, pady=10)

        self.createButtons()

    def createButtons(self):
        for i, sport in enumerate(self.sports):
            button = ctk.CTkButton(self.buttonsFrame,
                                   text=sport,
                                   command=lambda: self.select_sport(sport))
            button.grid(row=0, column=i, padx=10, pady=10)

    def showView(self):
        self.create_widgets()

    def unShowView(self):
        self.destroy()

    def select_sport(self, sport):
        print(f"Selected sport: {sport}")
        # Implement the logic to switch to the sport-specific view
