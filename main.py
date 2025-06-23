"""
This is the landing page / home page / etc.
By default, load whatever the user chose as their default landing (e.g: ModsCRUD).
If not set, inform them of their ability to choose a default.
"""
import flet as ft
# import os

#region Constants
name = "Minecraft Lekker Modpack Builder"  # Name of the app, used in the title bar
#endregion Constants

#region Button Clicks

def menu_item_about_click(e):
    """Opens the about dialog."""
    print("About clicked")
    # Here you would typically open a dialog with information about the app
    # For now, we just print a message
    e.page.add(ft.Text("About functionality is not yet implemented."))

def menu_item_compare_folders_click(e):
    """Opens the folder compare view."""
    print("Compare Folders clicked")
    # Here you would typically navigate to the folder compare view
    # For now, we just print a message
    e.page.add(ft.Text("Folder Compare functionality is not yet implemented."))

def menu_item_quit_click(e):
    """Exits the application."""
    e.page.window.destroy()

#endregion Button Clicks

#region Build GUI

def create_menu_bar():
    """Returns a row containing a menu bar with some items.
    """

    menubar = ft.MenuBar(
        expand=True,
        style=ft.MenuStyle(
            alignment=ft.alignment.top_left,
            bgcolor=ft.Colors.GREY_300,
            mouse_cursor={
                ft.ControlState.HOVERED: ft.MouseCursor.WAIT,
                ft.ControlState.DEFAULT: ft.MouseCursor.ZOOM_OUT,
            },
        ),
        controls=[
            ft.SubmenuButton(
                content=ft.Text("File"),
                #region Submenu Items
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("Compare Folders"),
                        leading=ft.Icon(ft.Icons.FOLDER),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        on_click=menu_item_compare_folders_click,
                    ),
                    ft.MenuItemButton(
                        content=ft.Text("Quit"),
                        leading=ft.Icon(ft.Icons.CLOSE),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        on_click=menu_item_quit_click,
                    ),
                ],
                #endregion Submenu Items
            ),
            ft.SubmenuButton(
                content=ft.Text("Help"),
                #region Submenu Items
                controls=[
                    ft.MenuItemButton(
                        content=ft.Text("About"),
                        leading=ft.Icon(ft.Icons.INFO),
                        style=ft.ButtonStyle(
                            bgcolor={ft.ControlState.HOVERED: ft.Colors.GREEN_100}
                        ),
                        on_click=menu_item_about_click,
                    ),
                ],
                #endregion Submenu Items
            ),
        ],
    )
    return ft.Row([menubar])

def add_menu_bar(page: ft.Page):
    """Adds the menu bar to the page. Placed in function for easier calls when switching views."""
    page.add(create_menu_bar())

#endregion Build GUI

#region Main Function

def main(page: ft.Page) -> None:
    """Main function to set up the Flet app."""

    #region Page Setup
    page.title = name
    add_menu_bar(page)
    #endregion Page Setup

    #region Page/View Switching:

    def route_change(e: ft.RouteChangeEvent):
        """Handles route (page/view) changes."""
        print(f"Route changed to: {e.route}")

        page.views.clear()  # Clear existing views
        add_menu_bar(page)  # Always re-add the menu bar

        if e.route == "/":
            page.add(ft.Text("Welcome to the Minecraft Lekker Modpack Builder!"))
        elif e.route == "/folder_compare":
            page.add(ft.Text("Folder Compare Page"))
        else:
            page.add(ft.Text("Page not found."))

    def view_pop(e: ft.ViewPopEvent):
        """Handles view pop events."""
        page.views.pop()  # Remove the last view
        top_view = page.views[-1]
        page.go(top_view.route)  # Navigate to the last view

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.update()

    #endregion Page/View Switching

#endregion Main Function

if __name__ == "__main__":
    ft.app(target=main)

