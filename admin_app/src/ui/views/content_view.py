# src/ui/contents/content_view.py
import customtkinter as ctk
from ...config import Config
from .base_view import BaseView
from ...utils.debug import debug_print, debug_print_widget_hierarchy
from typing import Literal, Any

# Import Contents
from ..contents.home_content import HomeContent
from ..contents.players_content import PlayersContent
from ..contents.teams_content import TeamsContent
from ..contents.events_content import EventsContent
from ..contents.leaderboard_content import LeaderboardContent

from ..widgets.navigationBar import NavigationBar


class RenderContents:
    """
    Manages all related to rendering contents.
    """
    def __init__(self, parent, contentFrame: ctk.CTkFrame, navigationButtons: dict[str, ctk.CTkButton]) -> None:
        self.parent = parent

        self._buttonsContent = navigationButtons

        self._content_frame = contentFrame

        self._contents_classes = [HomeContent, PlayersContent, TeamsContent, EventsContent, LeaderboardContent]

        self._contents: dict[str, Any] = {}
        self._current_content: Any = None

        self._create_contents()

    def _create_contents(self):
        for C in self._contents_classes:
            content_name = C.__name__
            content = C(parent=self._content_frame)  # Pass the controller (self) to each view
            self._contents[content_name] = content

    def show(self, content_name: str):
        debug_print(f"Showing content {content_name}")

        if self._current_content is not None:
            self._removeContent()

        self._current_content = self._contents[content_name]
        self._current_content.showContent()

        # Update button colors
        for button_name, button in self._buttonsContent.items():
            if button_name == content_name:
                button.configure(fg_color=("#96ff8e", "#016715"))
            else:
                button.configure(fg_color="transparent")

    def _removeContent(self):
        if self._current_content is not None:
            self._current_content.hideContent()


class ContentView(BaseView):
    def __init__(self, parent, app: ctk.CTk):
        super().__init__(parent, app)
        self.mainFrame: ctk.CTkFrame
        self.borderProperties("#9900FF", 1)

        self.navBarFrame: ctk.CTkFrame
        self.navBar: NavigationBar

        self.navButtons: dict[str, ctk.CTkButton]

    def _create_widgets(self):

        self.mainFrame = ctk.CTkFrame(self,
                                      fg_color=("#EAEAEA", "#232323"),
                                      border_width=self.border_width,
                                      border_color=self.border_color)
        self.mainFrame.pack(fill='both', expand=True)

        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=0)
        self.mainFrame.grid_columnconfigure(1, weight=1)

        self.navBarFrame = ctk.CTkFrame(self.mainFrame,
                                        fg_color="transparent",
                                        border_width=self.border_width,
                                        border_color=self.border_color)
        self.navBarFrame.grid(row=0, column=0, sticky="nsew", padx=50, pady=50)

        self.navBar = NavigationBar(self.navBarFrame,
                                    self.app)
        self.navBar.pack(fill="both", expand=True)

        self.navButtons = {
            "HomeContent": self.navBar.homeButton,
            "PlayersContent": self.navBar.playersButton,
            "TeamsContent": self.navBar.teamsButton,
            "EventsContent": self.navBar.eventsButton,
            "LeaderboardContent": self.navBar.leaderboardButton,
        }

        # from base view always initialize
        self.content_frame = ctk.CTkFrame(self.mainFrame,
                                          fg_color="transparent",
                                          border_width=self.border_width,
                                          border_color=self.border_color)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=50, pady=50)

        self._setCallbacksButtons()

        self.render_contents = RenderContents(self.mainFrame, self.content_frame, self.navButtons)
        self.render_contents.show(Config.CONTENT_VIEW_FIRST_CONTENT)
        # debug_print_widget_hierarchy(self.app)

    def _setCallbacksButtons(self):
        self.navBar.homeButton.configure(command=lambda: self.render_contents.show("HomeContent"))
        self.navBar.playersButton.configure(command=lambda: self.render_contents.show("PlayersContent"))
        self.navBar.teamsButton.configure(command=lambda: self.render_contents.show("TeamsContent"))
        self.navBar.eventsButton.configure(command=lambda: self.render_contents.show("EventsContent"))
        self.navBar.leaderboardButton.configure(command=lambda: self.render_contents.show("LeaderboardContent"))
        self.navBar.logoutButton.configure(command=lambda: self.app.showView("LoginView"))

    def showView(self):
        self._create_widgets()
