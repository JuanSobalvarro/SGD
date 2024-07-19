import customtkinter as ctk


class roundedFrame(ctk.CTkFrame):

    def __init__(self, parent, radius: int, *args, **kwargs):
        super().__init__(parent, border_radius=radius, *args, **kwargs)