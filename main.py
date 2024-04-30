import flet as ft
from flet import alignment, Page
from pages.index import _view_ as optigyHome
from pages.about import _view_ as optigyAbout

def main(page: Page):

    page.title = "Optigy"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_resizable = True
    page.vertical_alignment = "center"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.bgcolor = ft.colors.GREY_400
    
    index = optigyHome
    about = optigyAbout

    page.views.append(index)
    page.views.append(about)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)