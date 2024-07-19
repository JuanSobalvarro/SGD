# src/ui/homepage_view.py
import customtkinter as ctk
from ..config import Config
from .base_view import BaseView


class HomepageView(BaseView):
    def __init__(self, parent, app):
        super().__init__(parent, app)

        self.menuBar: ctk.CTkFrame = None

        self.borderProperties("#9900FF", 1)

    def create_widgets(self):
        self.mainFrame = ctk.CTkFrame(self,
                                      fg_color="#EAEAEA",
                                      border_width=self.border_width,
                                      border_color=self.border_color)
        self.mainFrame.pack(fill='both', expand=True)

        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_rowconfigure(1, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=0)
        self.mainFrame.grid_columnconfigure(1, weight=1)

        self.createMenuBar()
        self.createCalendar()
        self.createResume()

    def createMenuBar(self):
        self.menuBarFrame = ctk.CTkFrame(self.mainFrame,
                                         fg_color="transparent",
                                         border_width=self.border_width,
                                         border_color=self.border_color)
        self.menuBarFrame.grid(row=0, column=0, rowspan=2, sticky="nsew")

        self.menuBar = ctk.CTkFrame(self.menuBarFrame,
                                    fg_color="#FFFFFF",
                                    width=100,
                                    corner_radius=31,
                                    border_width=self.border_width,
                                    border_color=self.border_color)
        self.menuBar.pack(fill="y", expand=True, padx=50, pady=50)
        self.menuBar.grid_propagate(False)
        self.menuBar.pack_propagate(False)

        # Add buttons or other widgets to the menu bar
        self.createMenuButtons()

    def createMenuButtons(self):
        # Example menu buttons
        button1 = ctk.CTkButton(self.menuBar, text="Button 1")
        button1.pack(pady=10, padx=10, fill='x')

        button2 = ctk.CTkButton(self.menuBar, text="Button 2")
        button2.pack(pady=10, padx=10, fill='x')

        button3 = ctk.CTkButton(self.menuBar, text="Button 3")
        button3.pack(pady=10, padx=10, fill='x')

    def createCalendar(self):
        self.calendarFrame = ctk.CTkFrame(self.mainFrame,
                                          fg_color="#FFFFFF",
                                          corner_radius=31,
                                          border_width=self.border_width,
                                          border_color=self.border_color)
        self.calendarFrame.grid(row=0, column=1, sticky="nsew", pady=50)

    def createResume(self):
        self.resumeFrame = ctk.CTkFrame(self.mainFrame,
                                        fg_color="#FFFFFF",
                                        corner_radius=31,
                                        border_width=self.border_width,
                                        border_color=self.border_color)
        self.resumeFrame.grid(row=1, column=1, sticky="nsew", pady=50)

    def showView(self):
        self.create_widgets()

    def unShowView(self):
        self.destroy()
