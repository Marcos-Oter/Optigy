import flet as ft

general_width= 270
profiles_containers_height = 160
profiles_containers_border = 12
dark_color_items = ft.colors.GREY_900

greens_gradients = ["#3FBB9D","#3dc7a5","#3dc7a5","#3dc7a5","#3dc7a5","#39D59A","#3fe39f","#3fe39f","#3fe39f", "#32FAA7"]
grey_gradients = ["#E5E7E9","#E5E7E9","#E5E7E9","#E5E7E9","#E5E7E9","#A6ACAF","#A6ACAF","#A6ACAF"]

bg_grey_gradients = [ft.colors.GREY_600, ft.colors.GREY_500,ft.colors.GREY_300, ft.colors.GREY_300, ft.colors.GREY_300, ft.colors.GREY_300, ft.colors.GREY_300]
bg2_grey_gradients = [ft.colors.GREY_500,ft.colors.GREY_400, ft.colors.GREY_200, ft.colors.GREY_200, ft.colors.GREY_200]

home_icon_size = 85

class form(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)
        self.name = ft.TextField(label="Nombre", label_style= ft.TextStyle(color=ft.colors.WHITE), height=75, border_color=ft.colors.RED_50, max_length=10,color=ft.colors.GREY_800,bgcolor= ft.colors.GREY_600)
        self.type = ft.Dropdown(label="Tipo", label_style= ft.TextStyle(color=ft.colors.WHITE), height=75, bgcolor=ft.colors.GREY_600 ,options=[ft.dropdown.Option("Casa"),ft.dropdown.Option("Edificio"),ft.dropdown.Option("Nave")])
        
        self.main = ft.Column(
                    #expand=True,
                    #alignment=ft.MainAxisAlignment.CENTER,
                    controls=
                    [
                        ft.Column(
                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                            controls=[
                                #LOGO
                                ft.Container(
                                        height=85,
                                        width=85,
                                        content=ft.Image(width=50,src="assets/logos/OptigyLogo.png"),
                                        border_radius=18,
                                        padding=10,
                                        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=greens_gradients),
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
                                                            ft.TextStyle(font_family="arial", letter_spacing= 7, size=19, weight=ft.FontWeight.W_600,
                                                                        foreground=ft.Paint(
                                                                        color=dark_color_items,
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
                                                                        ft.TextStyle(font_family="arial",letter_spacing= 7,size=19, weight=ft.FontWeight.W_600,color=ft.colors.WHITE,),
                                                                    ),
                                                                ],
                                                        ),      
                                                    ]
                                            
                                ),
                                #SUBTITLE
                                ft.Text(text_align= ft.TextAlign.CENTER,
                                        spans=[
                                            ft.TextSpan("Cuida y optimiza tu enegía!",
                                            ft.TextStyle(font_family="arial",size=15, weight=ft.FontWeight.W_700,color=dark_color_items,),
                                            ),
                                        ],
                                    ),
                            ],
                        ),
                    ]
                )

        def CreateAPerfil(e):
            if self.form.height != 320:
                self.form.height = 320
                self.form.opacity = 100
                self.form.disabled=False
                self.form.update()
                self.button.visible=False
                self.button.update()
                self.footer.visible=False
                self.footer.update()
                self.main.visible=False
                self.main.update()
                

        def CancelCreateAPerfil(e):
            if self.form.height != 0:
                self.form.height = 0
                self.form.opacity = 0
                self.form.disabled=True
                self.form.update()
                self.button.visible=True
                self.button.update()
                self.footer.visible=True
                self.footer.update()
                self.main.visible=True
                self.main.update()
                
        self.form = ft.Container(
                                width=general_width,
                                height=0,
                                #col=4,
                                #adaptive=True,
                                #expand=True,
                                bgcolor="#3fe39f",
                                border_radius=40,
                                opacity=1,
                                #alignment=alignment.center,
                                #margin=ft.margin.only(left=-20,right=-20),
                                animate=ft.animation.Animation(400, "decelerate"),
                                animate_opacity=200,
                                padding= ft.padding.only(top=45, bottom=45, left=10,right=10),
                                content=ft.Column(
                                horizontal_alignment= ft.CrossAxisAlignment.CENTER, 
                                alignment= ft.MainAxisAlignment.CENTER,
                                    controls=
                                    [
                                        ft.Text("Cree un nuevo perfil", text_align= ft.TextAlign.CENTER, color=dark_color_items),
                                        self.name,
                                        self.type,
                                        ft.Container(
                                            content=ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.TextButton("Guardar", ft.icons.SAVE, icon_color=ft.colors.WHITE, on_click=lambda e: CancelCreateAPerfil(e), style= ft.ButtonStyle(bgcolor="#3fe39f", color=ft.colors.WHITE, shape=ft.RoundedRectangleBorder(radius=10))),
                                                    ft.TextButton("Cancelar", ft.icons.CANCEL, icon_color=ft.colors.WHITE, on_click=lambda e: CancelCreateAPerfil(e), style= ft.ButtonStyle(bgcolor=ft.colors.RED_400, color=ft.colors.WHITE, shape=ft.RoundedRectangleBorder(radius=10)))
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            )


        self.table =  ft.Column(
                            controls=[
                                ft.DataTable(
                                        width=(general_width - 40),
                                        border_radius=5,
                                        height= profiles_containers_height,
                                        gradient= ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg2_grey_gradients),
                                        columns=[ft.Text("No hay perfil.",size=12,color=dark_color_items)],
                                )
                            ]       
        )

        self.button = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
             controls=[
                  ft.Container(width=75,
                                height=75,
                                margin=0,
                                gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=greens_gradients),
                                shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
                                        color=ft.colors.BLACK,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                    ),
                                    border_radius=20,
                                    on_click=lambda e: CreateAPerfil(e),
                                    content= ft.Icon(name=ft.icons.ADD, size=20,color=ft.colors.WHITE)
                                ),
             ]
        )

        self.footer = ft.Text("Optigyº Todos los derechos reservados",text_align= ft.TextAlign.CENTER, font_family="arial",size=11, weight=ft.FontWeight.W_700,color=ft.colors.GREY_900)
        
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            spacing=20,
            scroll="auto",
            controls=[
                self.main,
                self.table,
                self.button,
                self.form,
                self.footer,
            ]
        )
        
    def build(self):
         return self.content
    

def _view_():
        return ft.View("/index", bgcolor=ft.colors.GREY_400,
                    controls=[
                        ft.Container
                        (
                            width=1500,
                            height=700,
                            margin=-10,
                            alignment=ft.alignment.center,
                            #bgcolor="bluegrey900",
                            gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg_grey_gradients),
                            content=form()                       
                        )
                    ]       
                )

        page.update()