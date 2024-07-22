# src/ui/views/login_view.py
import customtkinter as ctk
from PIL import Image
from ...auth.authentication import AuthService
from ...auth.user import User
from .base_view import BaseView
from ...utils.debug import debug_print
from ...config import Config
import os


class LoginView(BaseView):
    def __init__(self, parent, app):
        super().__init__(parent, app)
        self.auth_service = AuthService()
        self.user: User = None

        self.usernameEntry: ctk.CTkEntry = None
        self.passwordEntry: ctk.CTkEntry = None

        self.formFrame: ctk.CTkFrame = None
        self.imageFrame: ctk.CTkFrame = None

        self.image: Image = None
        self.img_copy: Image = None
        self.ctkimage: ctk.CTkImage = None
        self.imageLabel: ctk.CTkLabel = None

        self.borderProperties("#0000FF", 1)

    def create_widgets(self):
        # Main frame to hold all widgets
        self.mainFrame = ctk.CTkFrame(self,
                                      fg_color=("#FFFFFF", "#3A3A3A"),
                                      corner_radius=36,
                                      border_width=self.border_width,
                                      border_color=self.border_color)
        self.mainFrame.pack(padx=100, pady=100, fill='both', expand=True)

        # Configure row and column weights for responsiveness
        self.mainFrame.grid_rowconfigure(0, weight=1)
        self.mainFrame.grid_columnconfigure(0, weight=5)
        self.mainFrame.grid_columnconfigure(1, weight=5)

        self.createFormFrame()
        self.createImageFrame()

    def createFormFrame(self):
        # Left side frame for form
        self.formFrame = ctk.CTkFrame(self.mainFrame,
                                      fg_color=("#FFFFFF", "#3A3A3A"),
                                      border_width=self.border_width,
                                      border_color=self.border_color)
        self.formFrame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        self.formFrame.grid_propagate(False)  # Disable size propagatioon

        self.welcomeFrame = ctk.CTkFrame(self.formFrame,
                                         fg_color=("#FFFFFF", "#3A3A3A"),
                                         border_width=self.border_width,
                                         border_color=self.border_color)
        self.welcomeFrame.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

        # Title
        titleLabel = ctk.CTkLabel(self.welcomeFrame,
                                  text="Bienvenido \nal Sistema de Gestión \nDeportiva ULSA",
                                  font=("Inter", 48),
                                  anchor="nw",
                                  justify=ctk.LEFT,
                                  text_color=Config.COLOR_GREEN)
        titleLabel.grid(row=0, column=0, padx=20, pady=20)

        # Description
        descriptionLabel = ctk.CTkLabel(self.welcomeFrame,
                                        text="Inicie sesión como administrador con su usuario",
                                        font=("Inter", 16),
                                        anchor="nw",
                                        justify=ctk.LEFT,
                                        text_color=("#2C2C2C", "#FFFFFF"))
        descriptionLabel.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Username frame
        usernameFrame = ctk.CTkFrame(self.formFrame,
                                     fg_color=("#FFFFFF", "#3A3A3A"),
                                     border_width=self.border_width,
                                     border_color=self.border_color,)
        usernameFrame.grid(row=2, column=0, sticky='nsew', padx=10)

        usernameFrame.grid_columnconfigure(0, weight=1)

        passwordFrame = ctk.CTkFrame(self.formFrame,
                                     fg_color=("#FFFFFF", "#3A3A3A"),
                                     border_width=self.border_width,
                                     border_color=self.border_color,)
        passwordFrame.grid(row=3, column=0, sticky='nsew', padx=10)

        passwordFrame.grid_columnconfigure(0, weight=1)

        # Username label and entry
        usernameLabel = ctk.CTkLabel(usernameFrame,
                                     text="Usuario",
                                     font=("Body/Font Family", 16))
        usernameLabel.grid(row=0, column=0, sticky="w", padx=30, pady=10)
        self.usernameEntry = ctk.CTkEntry(usernameFrame,
                                          height=35,
                                          font=("Body/Font Family", 12),
                                          placeholder_text="Nombre de Usuario")
        self.usernameEntry.grid(row=1, column=0, sticky="nswe", padx=30)

        # Password label and entry
        password_label = ctk.CTkLabel(passwordFrame,
                                      text="Contraseña",
                                      font=("Body/Font Family", 16))
        password_label.grid(row=0, column=0, sticky="w", padx=30, pady=10)
        self.passwordEntry = ctk.CTkEntry(passwordFrame,
                                          height=35,
                                          font=("Body/Font Family", 12),
                                          placeholder_text="********",
                                          show="*")
        self.passwordEntry.grid(row=1, column=0, sticky="nswe", padx=30)

        # Login button
        login_button = ctk.CTkButton(self.formFrame,
                                     text="Login",
                                     command=self.validate_login)
        login_button.grid(row=4, column=0, pady=10)

    def createImageFrame(self):
        # Right side frame for image
        self.imageFrame = ctk.CTkFrame(self.mainFrame,
                                       fg_color=("#FFFFFF", "#3A3A3A"),
                                       border_width=self.border_width,
                                       border_color=self.border_color
                                       )
        self.imageFrame.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        self.imageFrame.grid_propagate(False)  # Disable size propagatioon

        # Load and display image
        image_path = os.path.join(Config.APP_IMAGES_PATH, "login_logo.png")  # Adjust the path as needed
        self.image = Image.open(image_path)
        self.img_copy = self.image.copy()
        # print(self.image, self.img_copy)
        self.ctkimage = ctk.CTkImage(self.image, size=(500, 500))

        self.imageLabel = ctk.CTkLabel(self.imageFrame, text="", image=self.ctkimage)
        self.imageLabel.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
        # self._resize_image(None)  # Initially resize the image
        #self.imageFrame.bind('<Configure>', self._resize_image)

    def _resize_image(self, event):
        if self.imageLabel:
            new_width = event.width - 10
            new_height = event.height - 10

            debug_print(f"Resizing image from {self.image.width}x{self.image.height} to {new_width}x{new_height}")

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
            error_label = ctk.CTkLabel(self, text="Invalid credentials, try again.", text_color='#FF0000')
            error_label.grid(row=3, column=0, columnspan=2, pady=5)

    def showView(self):
        self.create_widgets()
