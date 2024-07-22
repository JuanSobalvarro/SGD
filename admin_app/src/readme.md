# SGD Admin's Application

## Overview
This application is designed to manage various aspects of a sports management system, including user authentication, sport selection, and administration tasks. It is built using Python and `customtkinter` for the GUI.

## Configuration
The configuration for the application is stored in config.py. This file includes settings such as application title, geometry, theme paths, and debug options.

## Folder Descriptions
- **auth/**: Contains the AuthService class for user authentication.
- **themes/**: Contains JSON theme files for customizing the application's appearance.
- **ui/**: Contains the main application and view classes.
  - app.py: Main application class that initializes and manages views.
  - base_view.py: Base class for all views.
  - content_view.py: Main content view with a menu and content frame.
  - homepage_view.py: View for the homepage.
  - login_view.py: View for the login screen.
  - sport_selection_view.py: View for selecting sports. 
- **utils/**: Contains utility functions, such as the debug printer.

## Development
For development, ensure you follow best practices such as:

- Using virtual environments.
- Keeping dependencies updated.
- Following the project's code structure and conventions.

## License
This project is licensed under the MIT License.