# src/ui/contents/home_content.py
import customtkinter as ctk
from ..widgets.calendar import CustomCalendar
from .base_content import BaseContent
from ...utils.debug import debug_print, debug_print_widget_hierarchy


class HomeContent(BaseContent):
    """
    HomeContent. Inherits from BaseContent.
    """
    def __init__(self, parent):
        super().__init__(parent)

        self.border_properties("#0000FF", 1)

    def createContent(self):
        # Always call pack to parent
        self.pack_to_parent()
        self.createCalendar()

    def createCalendar(self):
        self.calendar_frame = ctk.CTkFrame(self,
                                           fg_color="transparent",
                                           border_width=self.border_width,
                                           border_color=self.border_color)
        self.calendar_frame.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)

        self.calendar = CustomCalendar(self.calendar_frame,
                                       fg_color=("#FFFFFF", "#3A3A3A"),
                                       border_width=self.border_width,
                                       border_color=self.border_color,
                                       corner_radius=31)
        self.calendar.pack(fill="both", expand=True, padx=5, pady=5)

    def showContent(self):
        debug_print("Showing Home Content")
        # debug_print_widget_hierarchy(self)
        self.createContent()

    def hideContent(self):
        self.clearContent()
