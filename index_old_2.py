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

class UserDisplay(ft.UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return UserTable

UserTable = ft.Container(
                        width= general_width,
                        height=250,
                        padding=10,
                        alignment=alignment.center,
                        bgcolor=ft.colors.TRANSPARENT,
                        border_radius=profiles_containers_border,
                        content=ft.Column(
                             [
                                ft.Container(
                                        width=general_width,
                                        height=profiles_containers_height,
                                        alignment=alignment.center,
                                        border_radius=profiles_containers_border,
                                        bgcolor=profiles_containers_bgcolor,
                                        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg2_grey_gradients),
                                        shadow=ft.BoxShadow(
                                            spread_radius=.1,
                                            blur_radius=5,
                                            color=ft.colors.BLACK,
                                            offset=ft.Offset(0, 0),
                                            blur_style=ft.ShadowBlurStyle.NORMAL,
                                        ),
                                        margin= ft.margin.only(top=5,bottom=5),
                                        content=ft.Text("Casa 1",text_align=ft.TextAlign.CENTER,color=ft.colors.BLACK)
                                ),
                            ],
                        ),
),

class FormContainer(ft.UserControl):
        def __init__(self):
            super().__init__()
        
            self.name = ft.TextField(label="Nombre", height=75 ,border_color= ft.colors.RED_50, max_length=10)
            self.type = ft.Dropdown(label="Tipo", height=75, options=[ft.dropdown.Option("Casa"),ft.dropdown.Option("Edificio"),ft.dropdown.Option("Nave")])

        def build(self):
            return form

form = ft.Container(
                        width=general_width,
                        height=80,
                        bgcolor="#3fe39f",
                        border_radius=40,
                        opacity=0,
                        alignment=alignment.center,
                        #margin=ft.margin.only(left=-20,right=-20),
                        animate=ft.animation.Animation(400, "decelerate"),
                        animate_opacity=200,
                        padding= ft.padding.only(top=45, bottom=45, left=10,right=10),
                        content=ft.Column
                        (
                        horizontal_alignment= ft.CrossAxisAlignment.CENTER, 
                        alignment= ft.MainAxisAlignment.CENTER,
                            controls=
                            [
                                ft.Text("Cree un nuevo perfil", text_align= ft.TextAlign.CENTER),
                                FormContainer().name,
                                FormContainer().type,
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

_main_column_ = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        controls=
        [
            ft.Column(
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                controls=[
                    #LOGO
                    ft.Container(
                            height=80,
                            width=80,
                            content=ft.Image(width=50,src="assets/logos/OptigyLogo.png"),
                            border_radius=18,
                            padding=10,
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
                    #TITLE
                    ft.Stack([
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
                    #SUBTITLE
                    ft.Text(text_align= ft.TextAlign.CENTER,
                            spans=[
                                ft.TextSpan("Cuida y optimiza tu enegía!",
                                ft.TextStyle(font_family="arial",size=16, weight=ft.FontWeight.W_700,color=ft.colors.GREY_900,),
                                ),
                            ],
                        ),
                        ft.Container(
                        width= general_width,
                        height=250,
                        padding=10,
                        alignment=alignment.center,
                        bgcolor=ft.colors.TRANSPARENT,
                        border_radius=profiles_containers_border,
                        content= ft.Column(
                             [
                            ft.Container(
                                    width=general_width,
                                    height=profiles_containers_height,
                                    alignment=alignment.center,
                                    border_radius=profiles_containers_border,
                                    bgcolor=profiles_containers_bgcolor,
                                    gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg2_grey_gradients),
                                    shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
                                        color=ft.colors.BLACK,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                    ),
                                    margin= ft.margin.only(top=5,bottom=5),
                                    content=ft.Text("Casa 1",text_align=ft.TextAlign.CENTER,color=ft.colors.BLACK)
                            ),
                                                        ft.Container(
                                    width=general_width,
                                    height=profiles_containers_height,
                                    alignment=alignment.center,
                                    border_radius=profiles_containers_border,
                                    bgcolor=profiles_containers_bgcolor,
                                    gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg2_grey_gradients),
                                    shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
                                        color=ft.colors.BLACK,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                    ),
                                    margin= ft.margin.only(top=5,bottom=5),
                                    content=ft.Text("Casa 1",text_align=ft.TextAlign.CENTER,color=ft.colors.BLACK)
                            ),
                                                        ft.Container(
                                    width=general_width,
                                    height=profiles_containers_height,
                                    alignment=alignment.center,
                                    border_radius=profiles_containers_border,
                                    bgcolor=profiles_containers_bgcolor,
                                    gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg2_grey_gradients),
                                    shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
                                        color=ft.colors.BLACK,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                    ),
                                    margin= ft.margin.only(top=5,bottom=5),
                                    content=ft.Text("Casa 1",text_align=ft.TextAlign.CENTER,color=ft.colors.BLACK)
                            ),
                        ],
                        scroll=ft.ScrollMode.ALWAYS,
                        spacing=5,
                        height=200,
                        wrap=False,
                        
                        ),
                            ),
                    ft.Container(width=80,
                                height=80,
                                margin=15,
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
                                    border_radius=20,
                                    content= ft.FloatingActionButton(icon=ft.icons.ADD, bgcolor=ft.colors.TRANSPARENT, autofocus=True, on_click=lambda e: CreateAPerfil(e)),
                                ),
                            ft.Text(text_align= ft.TextAlign.CENTER,
                            spans=[
                                ft.TextSpan("Optigyº Todos los derechos reservados",
                                ft.TextStyle(font_family="arial",size=12, weight=ft.FontWeight.W_800,color=ft.colors.GREY_900,),
                                ),
                            ],
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
                            width=1500,
                            height=700,
                            margin=-10,
                            alignment=alignment.center,
                            #bgcolor="bluegrey900",
                            gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg_grey_gradients),
                            content=
                            ft.Row(
                                 alignment=ft.MainAxisAlignment.CENTER,
                                 vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                 controls=[
                                      ft.Container(
                                           #bgcolor="#0f0f0f",
                                           border_radius=40,
                                           #width= 280,
                                           height= 660,
                                           #border=ft.border.all(0.5,"white"),
                                           padding=ft.padding.only(top=35, left=15, right=15),
                                           clip_behavior=ft.ClipBehavior.HARD_EDGE,
                                           content=ft.Column(
                                                alignment=ft.MainAxisAlignment.CENTER,
                                                horizontal_alignment=ft.MainAxisAlignment.CENTER,
                                                expand=True,
                                                spacing=5,
                                                #scroll="hidden",
                                                controls=
                                                [
                                                    _main_column_,
                                                    FormContainer()
                                                ]
                                           )

                                      )
                                 ]
                            )
                        )
                    ]
        )

        page.update()