# src/ui/views/base_view.py
import customtkinter as ctk
from ...config import Config


class BaseView(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app

        self.mainFrame: ctk.CTkFrame = None

    def borderProperties(self, color: str, width: int):
        # Set border properties for debugging
        self.border_color = color if Config.DEBUG else None
        self.border_width = width if Config.DEBUG else 0

    def showView(self):
        """
        Function to be overridden by subclasses.
        """
        pass

    def unShowView(self):
        """
        To unshow the view it should forget the pack of itself,
        and destroy all the widgets inside the view to add
        new ones.
        """
        for widget in self.mainFrame.winfo_children():
            widget.destroy()
        self.mainFrame.destroy()
        self.pack_forget()
