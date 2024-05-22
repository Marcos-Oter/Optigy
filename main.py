#from flet import Page, app, colors, ThemeMode
import flet as ft
from index import _view_ as optigyHome
from tips import _view_ as optigyTips
from profile_general_view import _view_ as optigyProfile

def mainPage(page: ft.Page):
    page.title = "Optigy"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.GREY_400

    index = optigyHome()
    tips = optigyTips()
    general = optigyProfile()

    def route_change(route):
        page.views.clear()
        
        if page.route == "/general":
            page.views.append(general)

        if page.route == "/tips":
            page.views.append(tips)
        
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

    page.views.append(tips)
    page.views.append(general)
    page.views.append(index)
    page.update()
    
if __name__ == "__main__":
    ft.app(target=mainPage)