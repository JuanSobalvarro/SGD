# src/ui/widgets/calendar.py
from typing import Any
import customtkinter as ctk
from datetime import datetime, timedelta
from ...utils.debug import debug_print


class CustomCalendar(ctk.CTkFrame):
    def __init__(self,
                 parent: Any,
                 width: int = 350,
                 height: int = 350,
                 corner_radius: int = 31,
                 **kwargs):
        super().__init__(master=parent,
                         width=width,
                         height=height,
                         corner_radius=corner_radius,
                         **kwargs)

        self.current_date = datetime.now()  # Start with current date

        self._create_widgets()

    def _create_widgets(self):
        debug_print(self)
        self.header_frame = ctk.CTkFrame(self,
                                         fg_color="transparent",)
        self.header_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.days_frame = ctk.CTkFrame(self,
                                       fg_color="transparent",)
        self.days_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        self._populate_header()
        self._populate_days()

    def _populate_header(self):
        text_month_year = self.current_date.strftime('%B %Y')
        self.month_year = ctk.CTkLabel(self.header_frame,
                                       font=("Roboto", 12, "bold"),
                                       text=text_month_year,)
        self.month_year.pack(fill='x', padx=10, pady=10)

    def _populate_days(self):
        # Day names
        day_names = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]
        for col, day_name in enumerate(day_names):
            label = ctk.CTkLabel(self.days_frame,
                                 text=day_name,
                                 font=("Roboto", 10, "bold"))
            label.grid(row=1, column=col, sticky="nsew")
        # Get the first and last day of the month
        first_day_of_month = self.current_date.replace(day=1)
        last_day_of_month = (first_day_of_month.replace(month=self.current_date.month + 1, day=1) - timedelta(days=1))

        # Find out what day of the week the first day of the month is
        start_day = first_day_of_month.weekday()  # Monday is 0 and Sunday is 6

        # Create buttons for each day
        day = 1
        for row in range(2, 8):  # Start from row 2 to row 7
            for col in range(7):  # Columns 0 to 6
                day_number = str(day)
                if (row == 2 and col < start_day) or day > last_day_of_month.day:
                    # Empty cells before the first day of the month or after the last day
                    day_number = ""
                else:
                    # if it is an actual day increase
                    day += 1

                day_button = ctk.CTkLabel(self.days_frame,
                                          text=day_number,
                                          font=("Roboto", 10, "bold"),
                                          width=20,
                                          height=10)
                day_button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

                if day-1 == self.current_date.day:
                    day_button.configure(text_color="#239837")

    def _on_day_click(self, day: int):
        # Handle the day click event
        print(f"Day {day} clicked!")
