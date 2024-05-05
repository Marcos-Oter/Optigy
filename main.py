import flet as ft
from flet import UserControl,alignment, Page
from pages.index import _view_ as optigyHome
from pages.about import _view_ as optigyAbout
from datetime import datetime
import sqlite3

async def main(page: Page):

    page.title = "Optigy"

    page.window_resizable = True
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = ft.ThemeMode.DARK

    page.scroll = ft.ScrollMode.ADAPTIVE
    page.bgcolor = ft.colors.GREY_400
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    index = optigyHome()
    about = optigyAbout()

    def route_change(route):
        page.views.clear()
        if page.route == "/about":
            page.views.append(about)
        
        if page.route == "/index":
            page.views.append(index)

        page.route = "/index"
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.views.append(about)
    page.views.append(index)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)