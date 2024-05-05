from flet import View, Column, Container, Text, ElevatedButton, FilledButton, alignment, page, Page
import flet as ft
import math 

#Color de fondo de la APP

general_width= 325
profiles_containers_height = 190
profiles_containers_border = 12
profiles_containers_bgcolor = ft.colors.WHITE

greens_gradients = ["#3fe39f","#3fe39f","#3fe39f","#3fe39f","#3fe39f","#3dc7a5","#3dc7a5","#3dc7a5"]
grey_gradients = ["#E5E7E9","#E5E7E9","#E5E7E9","#E5E7E9","#E5E7E9","#A6ACAF","#A6ACAF","#A6ACAF"]

home_icon_size = 85

class FormContainer(ft.UserControl):
    def __init__(self):
        super().__init__()
    
    def build(self):
        return ft.Container(
            width=280,
            height=80,
            bgcolor=ft.colors.BLUE,
            border_radius=40,
            opacity=1,
            margin=ft.margin.only(left=-20,right=-20),
            animate=ft.animation.Animation(400, "decelerate"),
            animate_opacity=200,
            padding= ft.padding.only(top=45, bottom=45),



        )


_main_column_ = ft.Column(
    scroll="hidden",
    expand=True,
    alignment=ft.MainAxisAlignment.START,
    controls=
    [
        ft.Column(
            alignment= ft.MainAxisAlignment.CENTER,
            controls=[
                #LOGO
                ft.Container(
                    width=general_width,
                    height=80,
                    alignment=alignment.center,
                    content=ft.Container(
                        height=80,
                        width=80,
                        content=ft.Image(width=50,src="assets/logos/OptigyLogo.png"),
                        border_radius=18,
                        padding=5,
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
                    ),
                ),
                #TITLE
                ft.Container(
                    width=general_width,
                    alignment=alignment.center,                     
                    content= ft.Stack([
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
                #SUBTITLE
                ft.Container(
                    width=general_width,
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
                        width=general_width,
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
                        width=general_width,
                        alignment=alignment.center,
                        #margin=5,
                        content=ft.Container(width=general_width,
                                height=50,
                                border_radius=12,
                                border= ft.border.all(1, ft.colors.BLACK38),
                                content= ft.FloatingActionButton(content=ft.Container(margin=4, padding=4,content=ft.Row([ft.Image(width=35, src="assets/logos/LampIcon.png"), ft.Text("Aquí irán los Tips de eficiencia energética.", size=12,text_align=ft.TextAlign.CENTER)])), bgcolor=ft.colors.TRANSPARENT, autofocus=True, on_click=lambda e: e.page.go("/about")),
                            ),
                    ),
            ],

        ),

    ]
)


def _view_():
    return View("/index", bgcolor=ft.colors.GREY_400,
                controls=[
                    ft.Container
                    (
                        width=1300,
                        height=750,
                        margin=10,
                        bgcolor="#888888",
                        alignment=alignment.center,
                        content=ft.Row(
                            alignment= ft.MainAxisAlignment.CENTER,
                            vertical_alignment= ft.CrossAxisAlignment.CENTER,
                            controls=[
                                ft.Container(
                                    width=280,
                                    height=525,
                                    margin=5,
                                    border=ft.border.all(0.8,ft.colors.GREEN_400),
                                    border_radius=40,
                                    padding=ft.padding.only(top=35, left=20, right=20),
                                    clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                    content=ft.Column(
                                        alignment=ft.MainAxisAlignment.CENTER,
                                        expand=True,
                                        controls=
                                        [
                                            _main_column_,
                                            FormContainer()
                                        ]
                                    )
                                )
                                ],
                        ),
                    )
                ]
    )