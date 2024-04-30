from flet import View, Column, Container, Text, FilledButton, alignment, page, Page
import flet as ft
import math
from pages.index import _view_

index = _view_()

def _view_():
 return View("/index", bgcolor=ft.colors.GREY_400,
                controls=[
                ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/index")),
                ]
            )