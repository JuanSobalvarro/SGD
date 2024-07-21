# src/ui/homepage_view.py
from .content_view import ContentView
import customtkinter as ctk
from .calendar import CustomCalendar


class HomepageView(ContentView):
    """
    Homepage view. Inherits ContentView from ContentView, so we only need
    to add all the widgets to contentFrame
    """
    def __init__(self, parent, app):
        super().__init__(parent, app)

        self.borderProperties("#0000FF", 1)

    def create_content(self):
        self.createCalendar()

    def createCalendar(self):
        self.calendar_frame = ctk.CTkFrame(self.contentFrame,
                                           fg_color="transparent",
                                           border_width=self.border_width,
                                           border_color=self.border_color)
        self.calendar_frame.grid(row=0, column=0, sticky="nswe", padx=5, pady=5)
        # self.calendar_frame.pack_propagate(False)

        self.calendar = CustomCalendar(self.calendar_frame,
                                       corner_radius=31)
        self.calendar.pack(fill="both", expand=True, padx=5, pady=5)


    def showView(self):
        self.create_content()

    def unShowView(self):
        self.destroy()
