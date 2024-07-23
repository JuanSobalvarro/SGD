import customtkinter as ctk
from PIL import Image, ImageTk


class CircularButton(ctk.CTkButton):
    def __init__(self,
                 parent,
                 light_image_path: str,
                 dark_image_path: str,
                 size: int = 50,
                 bg_color: tuple[str, str] = None,
                 command=None,
                 *args,
                 **kwargs):
        self.size = size  # Size of the circular button

        # Load and resize the image
        self.photo = ctk.CTkImage(light_image=Image.open(light_image_path),
                                  dark_image=Image.open(dark_image_path),
                                  size=(self.size-self.size//2, self.size-self.size//2),)

        super().__init__(parent,
                         image=self.photo,
                         text="",
                         command=command,
                         *args,
                         **kwargs)

        # Set the background color and make the button circular
        self.configure(fg_color=bg_color, corner_radius=self.size//2, width=self.size, height=self.size)

