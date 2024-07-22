# src/ui/app.py
import customtkinter as ctk
from ..config import Config
from ..utils.debug import debug_print
from .views.login_view import LoginView
from .views.sport_selection_view import SportSelectionView
from .views.content_view import ContentView
from .views.base_view import BaseView


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(Config.APP_TITLE)
        self.geometry(Config.APP_GEOMETRY)
        self.minsize(Config.APP_MIN_WIDTH, Config.APP_MIN_HEIGHT)

        self.viewsContainer: BaseView = None
        self.statusBar: ctk.CTkFrame = None

        ctk.set_appearance_mode(Config.current_theme)
        ctk.set_default_color_theme(Config.APP_THEME_PATH)

        self.border_width: int = None
        self.border_color: str = None
        self.__borderProperties("#00FF00", 1)

        self.currentFrame: BaseView = None
        self.frames: dict[str, BaseView] = {}
        self.create_frames()

        # Make the main frame fill the entire window
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #self.bind('<Configure>', self._resize)

    def create_frames(self):
        self.setUp()

        for F in (LoginView, SportSelectionView, ContentView):
            page_name = F.__name__
            frame = F(parent=self.viewsContainer, app=self)  # Pass the controller (self) to each view
            self.frames[page_name] = frame

    def setUp(self):
        # create ViewsContainer
        self.viewsContainer = ctk.CTkFrame(self,
                                           border_color=self.border_color,
                                           border_width=self.border_width)
        self.viewsContainer.grid(row=0, column=0, sticky='nsew')

        # create Status Bar
        self.statusBar = ctk.CTkFrame(self,
                                      height=30)
        self.statusBar.grid(row=1, column=0, sticky='nsew')
        self.statusBar.grid_propagate(False)

    def show_frame(self, frame_name: str):
        debug_print(f"Showing frame {frame_name}")

        # If there is a frame unshowit
        if self.currentFrame is not None:
            self.currentFrame.unShowView()

        self.currentFrame = self.frames[frame_name]

        self.currentFrame.showView()
        self.currentFrame.tkraise()
        self.currentFrame.pack(fill="both", expand=True)

    def _resize(self, event=None):
        if event:
            debug_print(f"Current app window size {self.winfo_width()}x{self.winfo_height()}")

    def __borderProperties(self, color: str, width: int):
        # Set border properties for debugging
        self.border_color = color if Config.DEBUG else None
        self.border_width = width if Config.DEBUG else 0

    @staticmethod
    def toggle_theme(new_theme: str):
        if new_theme not in ["light", "dark"]:
            debug_print("ROSSMAN USA LIGHT O DARK")
            return

        if Config.current_theme == new_theme:
            return

        Config.current_theme = new_theme
        ctk.set_appearance_mode(new_theme)

    def run(self):
        self.show_frame("ContentView")
        self.mainloop()
