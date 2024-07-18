# src/ui/login_view.py
import customtkinter as ctk
from PIL import Image, ImageTk
from ..auth.authentication import AuthService
from ..auth.user import User
from .base_view import BaseView
from ..utils.debug import debug_print
import os


class LoginView(BaseView):
    def __init__(self, parent, app):
        super().__init__(parent, app)
        self.auth_service = AuthService()
        self.user: User = None

        self.usernameEntry: ctk.CTkEntry = None
        self.passwordEntry: ctk.CTkEntry = None

        self.mainFrame: ctk.CTkFrame = None

        self.formFrame: ctk.CTkFrame = None
        self.imageFrame: ctk.CTkFrame = None

        self.image: Image = None
        self.img_copy: Image = None
        self.ctkimage: ctk.CTkImage = None
        self.imageLabel: ctk.CTkLabel = None

    def create_widgets(self):
        # Main frame to hold all widgets
        self.mainFrame = ctk.CTkFrame(self, fg_color='white')
        self.mainFrame.pack(padx=100, pady=100, fill='both', expand=True)

        self.mainFrame.grid_columnconfigure(0, weight=3)
        self.mainFrame.grid_columnconfigure(1, weight=7)

        # Left side frame for form
        self.formFrame = ctk.CTkFrame(self.mainFrame)
        self.formFrame.grid(row=0, column=0, sticky="nsew", padx=20, pady=10)

        # Right side frame for image
        self.imageFrame = ctk.CTkFrame(self.mainFrame)
        self.imageFrame.grid(row=0, column=1, rowspan=5, sticky="nsew", padx=20, pady=10)

        # Title
        titleLabel = ctk.CTkLabel(self.formFrame,
                                  text="Bienvenido \nal Sistema de Gestión \nDeportiva ULSA",
                                  font=("Inter", 48),
                                  text_color="#65558F")
        titleLabel.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        # Description
        descriptionLabel = ctk.CTkLabel(self.formFrame, text="Inicie sesión como administrador con el usuario dado.", font=("Helvetica", 12))
        descriptionLabel.grid(row=1, column=0, columnspan=2, pady=(0, 20))

        # Username label and entry
        usernameLabel = ctk.CTkLabel(self.formFrame, text="Username:", font=("Helvetica", 14))
        usernameLabel.grid(row=2, column=0, sticky="w", pady=5)
        self.usernameEntry = ctk.CTkEntry(self.formFrame)
        self.usernameEntry.grid(row=2, column=1, padx=10, pady=5)

        # Password label and entry
        password_label = ctk.CTkLabel(self.formFrame, text="Password:", font=("Helvetica", 14))
        password_label.grid(row=3, column=0, sticky="w", pady=5)
        self.passwordEntry = ctk.CTkEntry(self.formFrame, show="*")
        self.passwordEntry.grid(row=3, column=1, padx=10, pady=5)

        # Login button
        login_button = ctk.CTkButton(self.formFrame, text="Login", command=self.validate_login)
        login_button.grid(row=4, column=0, columnspan=2, pady=20)

        # Load and display image
        image_path = os.path.join(os.path.dirname(__file__), '../../images/login_logo.png')  # Adjust the path as needed
        self.image = Image.open(image_path)
        self.img_copy = self.image.copy()
        self.ctkimage = ctk.CTkImage(self.image, size=(500, 500))

        self.imageLabel = ctk.CTkLabel(self.imageFrame, text="", image=self.ctkimage)
        self.imageLabel.grid(row=0, column=0)
        #self._resize_image(None)  # Initially resize the image
        self.imageFrame.bind('<Configure>', self._resize_image)

        # Configure row and column weights for responsiveness
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(1, weight=1)

    def showView(self):
       self.create_widgets()

    def _resize_image(self, event):
        if self.imageLabel:
            new_width = self.imageFrame.winfo_width()
            new_height = self.imageFrame.winfo_height()

            #debug_print(f"Resizing image from {self.image.width}x{self.image.height} to {new_width}x{new_height}")

            self.image = self.img_copy.resize((new_width, new_height))

            self.ctkimage = ctk.CTkImage(self.image, size=(new_width, new_height))
            self.imageLabel.configure(image=self.ctkimage)

    def validate_login(self):
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        if self.auth_service.authenticate(username, password):
            self.user = User(username)
            self.user.authenticate()
            self.app.show_frame("SportSelectionView")
        else:
            error_label = ctk.CTkLabel(self, text="Invalid credentials, try again.", text_color='red')
            error_label.grid(row=3, column=0, columnspan=2, pady=5)
