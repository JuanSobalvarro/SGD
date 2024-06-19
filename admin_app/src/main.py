import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs.dialogs import Messagebox

THEME_NAME = 'superhero'

class App(ttk.Window):

    def __init__(self):
        super().__init__(themename=THEME_NAME)
        self.geometry('1280x720')
        self.title('Sistema de Gestion Deportiva | ULSA | Administracion')
        self.resizable(False, False)

        self.current_user = None
        self.sport = None

        self.show_login_screen()

    def show_login_screen(self):
        self.clear_screen()

        login_frame = ttk.Frame(self)
        login_frame.pack(pady=100)

        ttk.Label(login_frame, text="Usuario").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = ttk.Entry(login_frame)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        ttk.Label(login_frame, text="Contraseña").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = ttk.Entry(login_frame, show='*')
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        ttk.Button(login_frame, text="Iniciar sesión", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Simulating login validation
        if username == 'admin' and password == 'admin':
            self.current_user = username
            self.show_sport_selection()
        else:
            Messagebox.show_error('Usuario o contraseña incorrectos', alert=True)


    def show_sport_selection(self):
        self.clear_screen()

        selection_frame = ttk.Frame(self)
        selection_frame.pack(pady=100)

        ttk.Label(selection_frame, text="Selecciona un deporte").pack(pady=10)

        ttk.Button(selection_frame, text="Ping Pong", command=lambda: self.select_sport("Ping Pong")).pack(pady=5)
        ttk.Button(selection_frame, text="Fútbol", command=lambda: self.select_sport("Fútbol")).pack(pady=5)

    def select_sport(self, sport):
        self.sport = sport
        self.show_main_screen()

    def show_main_screen(self):
        self.clear_screen()
        self.create_widgets()

    def create_widgets(self):
        # Main frame
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill='both', expand=True)

        # Navigation menu
        self.nav_frame = ttk.Frame(self.main_frame)
        self.nav_frame.pack(side='left', fill='y')

        # Content frame
        self.content_frame = ttk.Frame(self.main_frame)
        self.content_frame.pack(side='right', fill='both', expand=True)

        self.create_nav_menu()
        self.create_content_area()

    def create_nav_menu(self):
        nav_items = ['Usuarios', 'Equipos', 'Torneos', 'Partidos', 'Noticias']

        self.nav_tree = ttk.Treeview(self.nav_frame)
        self.nav_tree.pack(fill='y', expand=True)

        for item in nav_items:
            self.nav_tree.insert('', 'end', item, text=item)

        self.nav_tree.bind('<<TreeviewSelect>>', self.on_nav_select)

    def create_content_area(self):
        self.content_label = ttk.Label(self.content_frame, text="Seleccione una opción del menú", font=("Arial", 16))
        self.content_label.pack(pady=20)

        self.form_frame = ttk.Frame(self.content_frame)
        self.form_frame.pack(fill='x', padx=20, pady=10)

        self.table_frame = ttk.Frame(self.content_frame)
        self.table_frame.pack(fill='both', expand=True, padx=20, pady=10)

    def on_nav_select(self, event):
        selected_item = self.nav_tree.selection()[0]
        self.content_label.config(text=f"Gestionar {selected_item}")

        # Clear form and table frame
        for widget in self.form_frame.winfo_children():
            widget.destroy()

        for widget in self.table_frame.winfo_children():
            widget.destroy()

        # Based on selected item, show relevant form and table
        if selected_item == 'Usuarios':
            self.show_users_management()
        elif selected_item == 'Equipos':
            self.show_teams_management()
        elif selected_item == 'Torneos':
            self.show_tournaments_management()
        elif selected_item == 'Partidos':
            self.show_matches_management()
        elif selected_item == 'Noticias':
            self.show_news_management()

    def show_users_management(self):
        # Form for adding/editing users
        ttk.Label(self.form_frame, text="Nombre").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(self.form_frame).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.form_frame, text="Email").grid(row=1, column=0, padx=5, pady=5)
        ttk.Entry(self.form_frame).grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(self.form_frame, text="Guardar").grid(row=2, column=0, columnspan=2, pady=10)

        # Table for displaying users
        columns = ('Nombre', 'Email')
        self.users_table = ttk.Treeview(self.table_frame, columns=columns, show='headings')
        for col in columns:
            self.users_table.heading(col, text=col)
        self.users_table.pack(fill='both', expand=True)

    def show_teams_management(self):
        # Similar form and table for teams
        ttk.Label(self.form_frame, text="Nombre del Equipo").grid(row=0, column=0, padx=5, pady=5)
        ttk.Entry(self.form_frame).grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(self.form_frame, text="Guardar").grid(row=1, column=0, columnspan=2, pady=10)

        columns = ('Nombre del Equipo', 'Deporte')
        self.teams_table = ttk.Treeview(self.table_frame, columns=columns, show='headings')
        for col in columns:
            self.teams_table.heading(col, text=col)
        self.teams_table.pack(fill='both', expand=True)

    def show_tournaments_management(self):
        # Similar form and table for tournaments
        pass

    def show_matches_management(self):
        # Similar form and table for matches
        pass

    def show_news_management(self):
        # Similar form and table for news
        pass

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

if __name__ == '__main__':
    app = App()
    app.mainloop()
