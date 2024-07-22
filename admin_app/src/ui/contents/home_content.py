# src/ui/contents/home_content.py
import customtkinter as ctk
from ..widgets.calendar import CustomCalendar
from .base_content import BaseContent


class HomeContent(BaseContent):
    """
    HomeContent. Inherits from BaseContent.
    """
    def __init__(self, parent):
        super().__init__(parent)

        self.border_properties("#0000FF", 1)

    def createContent(self):
        self.createCalendar()

    def createCalendar(self):
        self.calendar_frame = ctk.CTkFrame(self,
                                           fg_color="transparent",
                                           border_width=self._border_width,
                                           border_color=self._border_color)
        self.calendar_frame.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)

        self.calendar = CustomCalendar(self.calendar_frame,
                                       corner_radius=31)
        self.calendar.pack(fill="both", expand=True, padx=5, pady=5)

    def showContent(self):
        self.createContent()

    def unShowContent(self):
        self.clearContent()
