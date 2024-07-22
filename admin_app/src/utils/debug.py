# src/utils/debug.py
from ..config import Config
from functools import wraps


def debug_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if Config.DEBUG:
            return func(*args, **kwargs)
    return wrapper


@debug_only
def debug_print(message: str):
    print(f"DEBUG: {message}")


def print_widget_hierarchy(widget, level=0):
    """
    Recursively prints the hierarchy of children widgets.
    :param widget: The parent widget.
    :param level: The current level in the hierarchy (used for indentation).
    """
    indent = "  " * level
    widget_info = f"{indent}{widget.winfo_class()} - {widget.winfo_name()}"
    print(widget_info)

    for child in widget.winfo_children():
        print_widget_hierarchy(child, level + 1)


@debug_only
def debug_print_widget_hierarchy(widget):
    """
    Wrapper function to print widget hierarchy starting from the given widget.
    :param widget: The root widget to start printing hierarchy from.
    """
    print("Widget Hierarchy:")
    print_widget_hierarchy(widget)
