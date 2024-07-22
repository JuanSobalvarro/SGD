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
        super().__init__(parent, *args, **kwargs)

        self.parent = parent

        self.main_frame: ctk.CTkFrame = None

        self.border_color: str = None
        self.border_width: int = None

    def border_properties(self, color: str, width: int):
        self.border_color = color if Config.DEBUG else None
        self.border_width = width if Config.DEBUG else 0

    def create_main_frame(self):
        self.main_frame = ctk.CTkFrame(self.parent,
                                       fg_color="transparent",
                                       border_width=self.border_width,
                                       border_color=self.border_color,)
        self.pack(fill="both", expand=True)

    def showContent(self):
        # Function to override
        pass

    def clearContent(self):
        if self.main_frame is None:
            debug_print("Content frame is None")
            return

        for widget in self.winfo_children():
            debug_print(f"DESTROYING: {widget}")
            widget.destroy()
        self.main_frame.destroy()
        self.pack_forget()
