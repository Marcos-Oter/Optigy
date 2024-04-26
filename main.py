from time import sleep
import math
import flet as ft
from flet import alignment
from flet import *

def main(page: ft.Page):

    page.title = "Optigy"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_resizable = True
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    #Color de fondo de la APP
    page.bgcolor = ft.colors.GREY_400

    general_weight= 325
    profiles_containers_height = 190
    profiles_containers_border = 12
    profiles_containers_bgcolor = ft.colors.WHITE

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View("/",[optigy_home],bgcolor=ft.colors.GREY_400)
        )
        if page.route == "/store":
            page.views.append(
                ft.View(
                    "/store",
                    [
                        ft.AppBar(title=ft.Text("Store"), bgcolor=ft.colors.SURFACE_VARIANT),
                        ft.ElevatedButton("Go Home", on_click=lambda _: page.go("/")),
                    ],bgcolor=ft.colors.GREY_400
                )
            )
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

    optigy_home = ft.Row(
            [
            ft.Column(
                [
                    ft.Container(
                        width=general_weight,
                        alignment=alignment.center,
                        content=
                        ft.Container(width=80,
                                height=80,
                                gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.Alignment(0.8, 1),
                                        colors=[
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3dc7a5",
                                            "#3dc7a5",
                                            "#3dc7a5",
                                        ],
                                        tile_mode=ft.GradientTileMode.MIRROR,
                                        rotation=math.pi / 3,
                                    ),
                                    shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
                                        color=ft.colors.BLACK,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                ),
                                #theme= ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.GREEN)),
                                border_radius=18,
                                padding=10,
                                #border= ft.border.all(1, ft.colors.BLUE),
                                content=ft.Image(width=30,src="assets/logos/OptigyLogo.png"),
                            ),
                    ),

                    ft.Container(
                        width=general_weight,
                        #height=500,
                        margin=1,
                        alignment=alignment.center,                     
                        content= ft.Stack(
                                        [
                                            ft.Text(text_align= ft.TextAlign.CENTER,
                                                spans=[
                                                    ft.TextSpan("OPTIGY", 
                                                        ft.TextStyle(font_family="arial", letter_spacing= 8, size=20, weight=ft.FontWeight.W_600,
                                                            foreground=ft.Paint(
                                                                color=ft.colors.BLACK,
                                                                stroke_width=4,
                                                                stroke_join=ft.StrokeJoin.ROUND,
                                                                style=ft.PaintingStyle.STROKE,
                                                            ),
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            ft.Text(text_align= ft.TextAlign.CENTER,
                                                spans=[
                                                    ft.TextSpan("OPTIGY",
                                                        ft.TextStyle(font_family="arial",letter_spacing= 8,size=20, weight=ft.FontWeight.W_600,color=ft.colors.WHITE,),
                                                    ),
                                                ],
                                            ),      
                                        ]
                                    ),
                        ),
                    ft.Container(
                        width=general_weight,
                        alignment=alignment.center,
                        content=ft.Text(text_align= ft.TextAlign.CENTER,
                            spans=[
                                ft.TextSpan("Cuida y optimiza tu enegía!",
                                    ft.TextStyle(font_family="arial",size=16, weight=ft.FontWeight.W_700,color=ft.colors.GREY_900,),
                                ),
                            ],
                        ),
                    ),

                    ft.Container(
                        width=general_weight,
                        height=250,
                        padding=2,
                        margin=5,
                        alignment=alignment.center,
                        bgcolor=ft.colors.TRANSPARENT,
                        content= ft.Column([
                            ft.Container(
                                    width=general_weight,
                                    height=profiles_containers_height,
                                    alignment=alignment.center,
                                    border_radius=profiles_containers_border,
                                    bgcolor=profiles_containers_bgcolor,
                                    margin=5,
                                    content=ft.Text("Casa 0",text_align=ft.TextAlign.CENTER)
                            ),
                            ft.Container(
                                    width=general_weight,
                                    height=profiles_containers_height,
                                    alignment=alignment.center,
                                    border_radius=profiles_containers_border,
                                    bgcolor=profiles_containers_bgcolor,
                                    margin=5,
                                    content=ft.Text("Casa 1",text_align=ft.TextAlign.CENTER)
                            ),

                                    ft.Container(
                                    width=general_weight,
                                    height=profiles_containers_height,
                                    alignment=alignment.center,
                                    border_radius=profiles_containers_border,
                                    bgcolor=profiles_containers_bgcolor,
                                    margin=5,
                                    content=ft.Text("Casa 2",text_align=ft.TextAlign.CENTER)
                            ),

                                    ft.Container(
                                    width=general_weight,
                                    height=profiles_containers_height,
                                    alignment=alignment.center,
                                    border_radius=profiles_containers_border,
                                    bgcolor=profiles_containers_bgcolor,
                                    margin=5,
                                    content=ft.Text("Casa 3",text_align=ft.TextAlign.CENTER)
                            ),
                        ],
                            spacing=10,
                            height=200,
                            width=float("inf"),
                            scroll=ft.ScrollMode.ALWAYS,
                        ),
                    ),
               
                    ft.Container(
                        width=general_weight,
                        alignment=alignment.center,
                        margin=5,
                        content=
                        ft.Container(width=80,
                                height=80,
                                gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.Alignment(0.8, 1),
                                        colors=[
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3fe39f",
                                            "#3dc7a5",
                                            "#3dc7a5",
                                            "#3dc7a5",
                                        ],
                                        tile_mode=ft.GradientTileMode.MIRROR,
                                        rotation=math.pi / 3,
                                    ),
                                    shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
                                        color=ft.colors.BLACK,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                ),
                                #theme= ft.Theme(color_scheme=ft.ColorScheme(primary=ft.colors.GREEN)),
                                border_radius=20,
                                #border= ft.border.all(1, ft.colors.BLUE),
                                content= ft.FloatingActionButton(icon=ft.icons.ADD, bgcolor=ft.colors.TRANSPARENT, autofocus=True, on_click=lambda _: page.go("/store")),
                            ),
                    ),

                    ft.Container(
                        width=general_weight,
                        alignment=alignment.center,
                        margin=5,
                        content=ft.Container(width=general_weight,
                                height=50,
                                border_radius=12,
                                border= ft.border.all(1, ft.colors.BLACK38),
                                content= ft.FloatingActionButton(content=ft.Container(margin=4, padding=4,content=ft.Row([ft.Image(width=35, src="assets/logos/LampIcon.png"), ft.Text("Aquí irán los Tips de eficiencia energética.", size=12,text_align=ft.TextAlign.CENTER)])), bgcolor=ft.colors.TRANSPARENT, autofocus=True, on_click=lambda _: page.go("/store")),
                            ),
                    ),

                    ft.Container(
                        width=general_weight,
                        alignment=alignment.center,
                        content=ft.Text("Optigyº todos los derechos reservados.",weight=ft.FontWeight.W_800,font_family="arial", size=13,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                    )
                ],
                alignment= ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.MainAxisAlignment.CENTER),
            ], alignment= ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

ft.app(main)