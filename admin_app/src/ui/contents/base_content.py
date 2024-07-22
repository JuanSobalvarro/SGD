# src/ui/contents/base_content.py
import customtkinter as ctk


class BaseContent(ctk.CTkFrame):
    """
    Base content for all content types. It manages all the widgets in a frame
    """
    def __init__(self, parent):
        super().__init__(parent)

        self.border_color: str = None
        self.border_width: int = None

    def border_properties(self, color: str, width: int):
        self.border_color = color
        self.border_width = width

    def showContent(self):
        # Function to override
        pass

    def clearContent(self):
        for widget in self.winfo_children():
            widget.destroy()