import tkinter as tk
from tkinter import ttk


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.geometry('500x500')
        self.title('SGD Admin App')

        # style initialize
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.widgets()

    def widgets(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill='both', expand=True)


if __name__ == '__main__':
    app = App()
    app.mainloop()
