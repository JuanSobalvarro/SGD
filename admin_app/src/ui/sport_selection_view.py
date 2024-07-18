# src/ui/sport_selection_view.py
import customtkinter as ctk
from .base_view import BaseView


class SportSelectionView(BaseView):
    def __init__(self, parent, app):
        super().__init__(parent, app)

    def create_widgets(self):
        label = ctk.CTkLabel(self, text="Select a Sport")
        label.pack(pady=10)

        ping_pong_button = ctk.CTkButton(self, text="Ping Pong", command=lambda: self.select_sport("Ping Pong"))
        ping_pong_button.pack(pady=5)

        football_button = ctk.CTkButton(self, text="Football", command=lambda: self.select_sport("Football"))
        football_button.pack(pady=5)

    def showView(self):
        self.create_widgets()

    def unShowView(self):
        self.destroy()

    def select_sport(self, sport):
        print(f"Selected sport: {sport}")
        # Implement the logic to switch to the sport-specific view
