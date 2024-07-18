# src/ui/app.py
import customtkinter as ctk
from ..config import Config
from ..utils.debug import debug_print
from .login_view import LoginView
from .sport_selection_view import SportSelectionView
from .base_view import BaseView


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(Config.APP_TITLE)
        self.geometry(Config.APP_GEOMETRY)
        self.minsize(Config.APP_MIN_WIDTH, Config.APP_MIN_HEIGHT)

        self.viewsContainer = None

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme(Config.APP_THEME_PATH)

        self.currentFrame: BaseView = None
        self.frames: dict[str, BaseView] = {}
        self.create_frames()

        # Make the main frame fill the entire window
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.bind('<Configure>', self._resize)

        self.show_frame("LoginView")

    def create_frames(self):
        self.viewsContainer = ctk.CTkFrame(self)
        self.viewsContainer.grid(row=0, column=0, sticky='nsew')

        for F in (LoginView, SportSelectionView):
            page_name = F.__name__
            frame = F(parent=self.viewsContainer, app=self)  # Pass the controller (self) to each view
            self.frames[page_name] = frame

    def show_frame(self, page_name):
        debug_print(f"Showing frame {page_name}")

        if self.currentFrame is not None:
            self.currentFrame.pack_forget()

        self.currentFrame = self.frames[page_name]

        self.currentFrame.showView()
        self.currentFrame.tkraise()
        self.currentFrame.pack(fill="both", expand=True)

    def _resize(self, event=None):
        if event:
            debug_print(f"Current app window size {self.winfo_width()}x{self.winfo_height()}")

    def run(self):
        self.mainloop()
