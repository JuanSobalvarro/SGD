import tkinter
from typing import Any
from customtkinter import CTkFrame, CTkLabel


class CustomCalendar(CTkFrame):
    def __init__(self,
                 parent: Any,
                 width: int = 350,
                 height: int = 350,
                 corner_radius: int = 31,
                 **kwargs):
        super().__init__(master=parent, width=width, height=height, corner_radius=corner_radius, **kwargs)

        self._create_widgets()

    def _create_widgets(self):

        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure(1, weight=1)

        self.header_frame = self._create_frame(self, 0, 0)

        self.days_frame = self._create_frame(self, 1, 0)

        # Additional setup can be done here, such as creating labels, buttons, etc.
        self._populate_header()
        self._populate_days()

    def _create_frame(self, parent, row, column):
        frame = CTkFrame(parent,
                         fg_color="transparent",
                         border_width=1,
                         border_color='black')
        frame.grid(row=row, column=column, sticky="nsew", padx=10, pady=10)
        return frame

    def _populate_header(self):
        self.month_year = CTkLabel(self.header_frame,
                                   text="Enero 2024",)
        self.month_year.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

    def _populate_days(self):
        # Placeholder for populating the days frame with calendar day buttons or labels
        pass
