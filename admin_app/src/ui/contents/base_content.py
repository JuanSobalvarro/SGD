# src/ui/contents/base_content.py
import customtkinter as ctk
from ...config import Config
from ...utils.debug import debug_print


class BaseContent(ctk.CTkFrame):
    """
    Base content for all content types. It manages all the widgets in a frame.
    Always call border_properties, and override showContent
    """
    def __init__(self, parent, *args, **kwargs):
        self.border_color: str = None
        self.border_width: int = None
        self.border_properties("#88113A", 1)
        super().__init__(parent,
                         border_width=self.border_width,
                         border_color=self.border_color,
                         *args, **kwargs)

        self.parent = parent

    def border_properties(self, color: str, width: int):
        self.border_color = color if Config.DEBUG else None
        self.border_width = width if Config.DEBUG else 0

    def pack_to_parent(self):
        self.pack(fill="both", expand=True, padx=5, pady=5)

        debug_print(f"Home content frame: {self}, parent: {self.parent}")

    def showContent(self):
        # Function to override
        pass

    def clearContent(self):
        if self is None:
            debug_print("Content frame is None")
            return

        for widget in self.winfo_children():
            debug_print(f"DESTROYING: {widget}")
            widget.destroy()

        self.pack_forget()
