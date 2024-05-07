from flet import View, Column, Container, Text, ElevatedButton, FilledButton, alignment, page, Page
import flet as ft

def _view_():
    return View("/about", bgcolor=ft.colors.GREY_400,
                controls=[
                    ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                    ft.ElevatedButton("Go Home", on_click=lambda e: e.page.go("/index")),
                ]
            )