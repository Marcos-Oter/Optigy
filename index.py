from flet import View, Column, Container, Text, ElevatedButton, FilledButton, alignment, page, Page
import flet as ft
import math

general_width= 275
profiles_containers_height = 190
profiles_containers_border = 12
profiles_containers_bgcolor = ft.colors.WHITE

greens_gradients = ["#3fe39f","#3fe39f","#3fe39f","#3fe39f","#3fe39f","#3dc7a5","#3dc7a5","#3dc7a5"]
grey_gradients = ["#E5E7E9","#E5E7E9","#E5E7E9","#E5E7E9","#E5E7E9","#A6ACAF","#A6ACAF","#A6ACAF"]
bg_grey_gradients = [ft.colors.GREY_600, ft.colors.GREY_500,ft.colors.GREY_400, ft.colors.GREY_400, ft.colors.GREY_400]
bg2_grey_gradients = [ft.colors.GREY_600,ft.colors.GREY_500, ft.colors.GREY_300, ft.colors.GREY_300, ft.colors.GREY_300]

home_icon_size = 85

def CreateAPerfil(e):
    if form.height != 320:
        form.height = 320
        form.opacity = 100
        form.disabled=False
        form.update()

def CancelCreateAPerfil(e):
     if form.height !=80:
        form.height = 80
        form.opacity = 0
        form.disabled=True
        form.update()

class form(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)
        self.name = ft.TextField(label="Nombre", height=75 ,border_color= ft.colors.RED_50, max_length=10)
        self.type = ft.Dropdown(label="Tipo", height=75, options=[ft.dropdown.Option("Casa"),ft.dropdown.Option("Edificio"),ft.dropdown.Option("Nave")])
        
        self.main = ft.Container(
            bgcolor= "#222222",
            border_radius=10,
            col=4,
        )

        self.form = ft.Container(
                                width=general_width,
                                height=80,
                                #col=4,
                                adaptive=True,
                                bgcolor="#3fe39f",
                                border_radius=40,
                                opacity=1,
                                alignment=alignment.bottom_center,
                                #margin=ft.margin.only(left=-20,right=-20),
                                animate=ft.animation.Animation(400, "decelerate"),
                                animate_opacity=200,
                                padding= ft.padding.only(top=45, bottom=45, left=10,right=10),
                                content=ft.Column(
                                horizontal_alignment= ft.CrossAxisAlignment.END, 
                                alignment= ft.MainAxisAlignment.CENTER,
                                    controls=
                                    [
                                        ft.Text("Cree un nuevo perfil", text_align= ft.TextAlign.CENTER),
                                        self.name,
                                        self.type,
                                        ft.Container(
                                            content=ft.Row
                                            (alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.TextButton("Crear", ft.icons.SAVE, on_click=lambda e: CancelCreateAPerfil(e)),
                                                    ft.TextButton("Cancelar",ft.icons.CANCEL, on_click=lambda e: CancelCreateAPerfil(e))
                                                ]

                                            ),
                                        ),

                                    ]
                                ),
                            )


        self.table = ft.Container(
            #bgcolor="#222222",
            #border_radius=10,
            #col=4,
            #visible=False

        )

        self.content = ft.ResponsiveRow(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                self.main,
                self.form,
                #self.table,
            ]
        )
    def build(self):
         return self.content



def _view_():
        return View("/index", bgcolor=ft.colors.GREY_400,
                    controls=[
                        ft.Container
                        (
                            width=1500,
                            height=700,
                            margin=-10,
                            alignment=alignment.center,
                            #bgcolor="bluegrey900",
                            gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg_grey_gradients),
                            content=form()                       
                        )
                    ]       
                )

        page.update()