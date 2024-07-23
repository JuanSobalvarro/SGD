# src/ui/widgets
import customtkinter as ctk


class HorizontalSeparator(ctk.CTkFrame):
    def __init__(self, parent: ctk.CTkFrame,
                 thick: int = 1,
                 color: tuple[str, str] | str = 'black',
                 *args, **kwargs) -> None:

        super().__init__(master=parent,
                         fg_color=color,
                         border_width=1,
                         border_color=color,
                         height=thick,
                         corner_radius=31,
                         *args,
                         **kwargs)
