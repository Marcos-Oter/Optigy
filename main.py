import flet as ft
from index import _view_ as optigyHome
from profile_general_view import _view_ as optigyProfile
from rooms_view import _view_ as optigyRooms
from tips import _view_ as optigyTips
from settings_view import _view_ as optigySettings

def mainPage(page: ft.Page):
    
    page.title = "Optigy"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.colors.GREY_400

    index = optigyHome()
    general = optigyProfile()
    tips = optigyTips()
    rooms = optigyRooms()
    settings = optigySettings()

    page.route = "/index"

    def route_change(route):
        page.views.clear()

        if page.route == "/settings":
            page.views.append(settings)
        
        if page.route == "/rooms":
            page.views.append(rooms)
        
        if page.route == "/general":
            page.views.append(general)

        if page.route == "/tips":
            page.views.append(tips)
        
        if page.route == "/index":
            page.views.append(index)

        page.update()
    

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    page.views.append(settings)
    page.views.append(rooms)
    page.views.append(tips)
    page.views.append(general)
    page.views.append(index)
    page.update()

if __name__ == "__main__":
    ft.app(target=mainPage)