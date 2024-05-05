from flet import View, Column, Container, Text, ElevatedButton, FilledButton, alignment, page, Page
import flet as ft
import math 

#Color de fondo de la APP

general_weight= 325
profiles_containers_height = 190
profiles_containers_border = 12
profiles_containers_bgcolor = ft.colors.WHITE

greens_gradients = ["#3fe39f","#3fe39f","#3fe39f","#3fe39f","#3fe39f","#3dc7a5","#3dc7a5","#3dc7a5"]
grey_gradients = ["#E5E7E9","#E5E7E9","#E5E7E9","#E5E7E9","#E5E7E9","#A6ACAF","#A6ACAF","#A6ACAF"]

home_icon_size = 85

def _view_():
    return View("/index", bgcolor=ft.colors.GREY_400,
                controls=[
                    Column([
                        ft.Row(
            [
            ft.Column(
                [
                    ft.Container(
                        width=general_weight,
                        alignment=alignment.center,
                        content=ft.Container(width=80,
                                             #offset=ft.transform.Offset(-1,-1),
                                height=80,
                                gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.Alignment(0.8, 1),
                                        colors=greens_gradients,
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
                        #margin=1,
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
                        #margin=5,
                        alignment=alignment.center,
                        bgcolor=ft.colors.TRANSPARENT,
                        content= ft.Column([
                            ft.Container(
                                    width=general_weight,
                                    gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.Alignment(0.8, 1),
                                        colors=grey_gradients),
                                    height=profiles_containers_height,
                                    alignment=alignment.center,
                                    border_radius=profiles_containers_border,
                                    bgcolor=profiles_containers_bgcolor,
                                    margin=5,
                                    content= ft.Row([ft.Column([ft.Image(width=home_icon_size, src="assets/logos/home-icon.png"), ft.Text("Casa 1",text_align=ft.TextAlign.CENTER, size=16, weight=ft.FontWeight.W_700,color=ft.colors.GREY_900)],alignment=ft.MainAxisAlignment.CENTER)
                        ],alignment=ft.MainAxisAlignment.CENTER)),
                            ft.Container(
                                    width=general_weight,
                                    gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.Alignment(0.8, 1),
                                        colors=grey_gradients),
                                    height=profiles_containers_height,
                                    alignment=alignment.center,
                                    border_radius=profiles_containers_border,
                                    bgcolor=profiles_containers_bgcolor,
                                    margin=5,
                                    content= ft.Row([ft.Column([ft.Image(width=home_icon_size, src="assets/logos/home-icon.png"), ft.Text("Casa 2",text_align=ft.TextAlign.CENTER, size=16, weight=ft.FontWeight.W_700,color=ft.colors.GREY_900)],alignment=ft.MainAxisAlignment.CENTER)
                        ],alignment=ft.MainAxisAlignment.CENTER)
                            ),

                                    ft.Container(
                                    width=general_weight,
                                    gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.Alignment(0.8, 1),
                                        colors=grey_gradients),
                                    height=profiles_containers_height,
                                    alignment=alignment.center,
                                    border_radius=profiles_containers_border,
                                    bgcolor=profiles_containers_bgcolor,
                                    margin=5,
                                    content= ft.Row([ft.Column([ft.Image(width=home_icon_size, src="assets/logos/home-icon.png"), ft.Text("Casa 3",text_align=ft.TextAlign.CENTER, size=16, weight=ft.FontWeight.W_700,color=ft.colors.GREY_900)],alignment=ft.MainAxisAlignment.CENTER)
                        ],alignment=ft.MainAxisAlignment.CENTER)
                            ),

                                    ft.Container(
                                    width=general_weight,
                                    gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.Alignment(0.8, 1),
                                        colors=grey_gradients),
                                    height=profiles_containers_height,
                                    alignment=alignment.center,
                                    border_radius=profiles_containers_border,
                                    bgcolor=profiles_containers_bgcolor,
                                    margin=5,
                                    content= ft.Row([ft.Column([ft.Image(width=home_icon_size, src="assets/logos/home-icon.png"), ft.Text("Casa 4",text_align=ft.TextAlign.CENTER, size=16, weight=ft.FontWeight.W_700,color=ft.colors.GREY_900)],alignment=ft.MainAxisAlignment.CENTER)
                        ],alignment=ft.MainAxisAlignment.CENTER)
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
                        #margin=5,
                        content=
                        ft.Container(width=80,
                                height=80,
                                gradient=ft.LinearGradient(
                                        begin=ft.alignment.top_center,
                                        end=ft.Alignment(0.8, 1),
                                        colors=greens_gradients,
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
                                content= ft.FloatingActionButton(icon=ft.icons.ADD, bgcolor=ft.colors.TRANSPARENT, autofocus=True, on_click=lambda e: e.page.go("/about")),
                            ),
                    ),

                    ft.Container(
                        width=general_weight,
                        alignment=alignment.center,
                        #margin=5,
                        content=ft.Container(width=general_weight,
                                height=50,
                                border_radius=12,
                                border= ft.border.all(1, ft.colors.BLACK38),
                                content= ft.FloatingActionButton(content=ft.Container(margin=4, padding=4,content=ft.Row([ft.Image(width=35, src="assets/logos/LampIcon.png"), ft.Text("Aquí irán los Tips de eficiencia energética.", size=12,text_align=ft.TextAlign.CENTER)])), bgcolor=ft.colors.TRANSPARENT, autofocus=True, on_click=lambda e: e.page.go("/about")),
                            ),
                    ),

                    ft.Container(
                        width=general_weight,
                        #top=0,
                        alignment=alignment.center,
                        content=ft.Text("Optigyº todos los derechos reservados.",weight=ft.FontWeight.W_800,font_family="arial", size=13,color=ft.colors.BLACK,text_align=ft.TextAlign.CENTER),
                    )
                ],
                alignment= ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.MainAxisAlignment.CENTER),
            ], alignment= ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.CENTER,
        
                    ),
                ]
            
            ),]
    )