import flet as ft
<<<<<<< HEAD
from __module__ import delete_profile_display,profiles_containers_height,bg2_grey_gradients,bg_grey_gradients,bg_white_gradients, exp_consumition_field, settings_title_table, show_rooms, data_table, general_data_table, general_rooms_table, greens_gradients, bg_e_grey_gradients, general_width
import time

from profile_manager_db import ProfileManager
=======

general_width= 270
profiles_containers_height = 160
profiles_containers_border = 12

greens_gradients = ["#3FBB9D","#3dc7a5","#3dc7a5","#3dc7a5","#3dc7a5","#39D59A","#3fe39f","#3fe39f","#3fe39f", "#32FAA7"]
grey_gradients = ["#E5E7E9","#E5E7E9","#E5E7E9","#E5E7E9","#E5E7E9","#A6ACAF","#A6ACAF","#A6ACAF"]

bg_grey_gradients = [ft.colors.GREY_600, ft.colors.GREY_500,ft.colors.GREY_300, ft.colors.GREY_300, ft.colors.GREY_300, ft.colors.GREY_300, ft.colors.GREY_300]
bg2_grey_gradients = [ft.colors.GREY_500,ft.colors.GREY_400, ft.colors.GREY_200, ft.colors.GREY_200, ft.colors.GREY_200]

>>>>>>> a8bdfc93c1a9388b0fc3baed18ffd87274c70643

class form(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)
<<<<<<< HEAD

        self.data_base = ProfileManager()

        self.name_profile = ft.TextField(label="Nombre", label_style= ft.TextStyle(color=ft.colors.GREY_900, weight= ft.FontWeight.W_500), height=75, border_color=ft.colors.RED_50, max_length=10, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200)
        self.type_profile = ft.Dropdown(label="Icono", label_style= ft.TextStyle(color=ft.colors.GREY_900, weight= ft.FontWeight.W_500), height=75, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200 ,options=[ft.dropdown.Option("Casa"),ft.dropdown.Option("Edificio"),ft.dropdown.Option("Nave"),ft.dropdown.Option("Otro")])
        
        self.selected_profile = None

        self.edit_name_profile = ft.TextField(label="Nombre", label_style= ft.TextStyle(color=ft.colors.GREY_900, weight= ft.FontWeight.W_500), height=75, border_color=ft.colors.RED_50, max_length=10, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200)
        self.edit_type_profile = ft.Dropdown(label="Icono", label_style= ft.TextStyle(color=ft.colors.GREY_900, weight= ft.FontWeight.W_500), height=75, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200 ,options=[ft.dropdown.Option("Casa"),ft.dropdown.Option("Edificio"),ft.dropdown.Option("Nave"),ft.dropdown.Option("Otro")])

        self.profile_table = ft.DataTable(
            divider_thickness=0,
            expand=False,
            heading_row_color=ft.colors.TRANSPARENT,
            column_spacing=0,
            data_row_max_height=profiles_containers_height,
            data_row_min_height=profiles_containers_height,
            data_row_color={ft.MaterialState.SELECTED: ft.colors.GREEN_100, ft.MaterialState.PRESSED: ft.colors.GREY_800},
            width=float("inf"),
            border_radius=10,
            show_bottom_border=False,
            heading_row_height=0,
            data_text_style= ft.TextStyle(color=ft.colors.RED),
            columns=[
                ft.DataColumn(ft.Text("Nombre", color="red", weight="bold", size=10,)),
            ]
        )

        self.table =  ft.Container(
                        width=(general_width - 80),
                        border_radius=5,
                        height= profiles_containers_height - 2,
                        shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=10,
                                        color=ft.colors.GREY_500,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                    ),
                        gradient= ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg2_grey_gradients),
                        content=ft.Column(
                            expand = True,
                            scroll = ft.ScrollMode.ALWAYS,
                            width=float("inf"),
                            disabled=False,
                            controls=[
                                    self.profile_table,
                            ]
                        )                                        
        )

        self.void_table =  ft.Column(
                            controls=[
                                ft.Container(
                                        width=(general_width + 40),
                                        border_radius=5,
                                        height= (profiles_containers_height + 40),
                                        content=ft.Image(width=(general_width + 40),src="assets/images/Void01.png")
                                )
                            ]       
        )

        
        self.show_profiles()
        self.main = ft.Column(
=======
        self.name = ft.TextField(label="Nombre", label_style= ft.TextStyle(color=ft.colors.WHITE), height=75, border_color=ft.colors.RED_50, max_length=10,color=ft.colors.GREY_800,bgcolor= ft.colors.GREY_600)
        self.type = ft.Dropdown(label="Tipo", label_style= ft.TextStyle(color=ft.colors.WHITE), height=75, bgcolor=ft.colors.GREY_600 ,options=[ft.dropdown.Option("Casa"),ft.dropdown.Option("Edificio"),ft.dropdown.Option("Nave")])
        
        self.main = ft.Column(
                    #expand=True,
                    #alignment=ft.MainAxisAlignment.CENTER,
>>>>>>> a8bdfc93c1a9388b0fc3baed18ffd87274c70643
                    controls=
                    [
                        ft.Column(
                            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
<<<<<<< HEAD
                            spacing=3,
                            controls=[
                                #LOGO
                                ft.Container(
                                        height=100,
                                        width=100,
                                        content=ft.Image(width=50,src="assets/logos/OptigyLogo.png"),
                                        border_radius=16,
=======
                            controls=[
                                #LOGO
                                ft.Container(
                                        height=85,
                                        width=85,
                                        content=ft.Image(width=50,src="assets/logos/OptigyLogo.png"),
                                        border_radius=18,
>>>>>>> a8bdfc93c1a9388b0fc3baed18ffd87274c70643
                                        padding=10,
                                        gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=greens_gradients),
                                        shadow=ft.BoxShadow(
                                            spread_radius=.1,
                                            blur_radius=5,
<<<<<<< HEAD
                                            color=ft.colors.GREY_900,
=======
                                            color=ft.colors.BLACK,
>>>>>>> a8bdfc93c1a9388b0fc3baed18ffd87274c70643
                                            offset=ft.Offset(0, 0),
                                            blur_style=ft.ShadowBlurStyle.NORMAL,
                                        ),
                                    ),
                                #TITLE
                                ft.Stack([
                                    ft.Text(text_align= ft.TextAlign.CENTER,
                                                    spans=[
                                                        ft.TextSpan("OPTIGY", 
<<<<<<< HEAD
                                                            ft.TextStyle(font_family="arial", letter_spacing= 6, size=22, weight=ft.FontWeight.W_600,
                                                                        foreground=ft.Paint(
                                                                        color=ft.colors.GREY_900,
                                                                        stroke_width=3.5,
=======
                                                            ft.TextStyle(font_family="arial", letter_spacing= 7, size=19, weight=ft.FontWeight.W_600,
                                                                        foreground=ft.Paint(
                                                                        color=ft.colors.GREY_900,
                                                                        stroke_width=4,
>>>>>>> a8bdfc93c1a9388b0fc3baed18ffd87274c70643
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
<<<<<<< HEAD
                                                                        ft.TextStyle(font_family="arial",letter_spacing= 6,size=22, weight=ft.FontWeight.W_600,color=ft.colors.WHITE,),
=======
                                                                        ft.TextStyle(font_family="arial",letter_spacing= 7,size=19, weight=ft.FontWeight.W_600,color=ft.colors.WHITE,),
>>>>>>> a8bdfc93c1a9388b0fc3baed18ffd87274c70643
                                                                    ),
                                                                ],
                                                        ),      
                                                    ]
                                ),
                                #SUBTITLE
                                ft.Text(text_align= ft.TextAlign.CENTER,
                                        spans=[
                                            ft.TextSpan("Cuida y optimiza tu enegía!",
<<<<<<< HEAD
                                            ft.TextStyle(font_family="arial",size=18, weight=ft.FontWeight.W_700,color=ft.colors.GREY_900),
=======
                                            ft.TextStyle(font_family="arial",size=15, weight=ft.FontWeight.W_700,color=ft.colors.GREY_900),
>>>>>>> a8bdfc93c1a9388b0fc3baed18ffd87274c70643
                                            ),
                                        ],
                                    ),
                            ],
                        ),
                    ]
                )

<<<<<<< HEAD
        self.form = ft.Container(
                                width=0,
                                height=0,
                                bgcolor="#3fe39f",
                                border_radius=30,
                                opacity=1,
                                margin=ft.margin.only(top=-10,bottom=-10),
                                animate=ft.animation.Animation(400, "decelerate"),
                                animate_opacity=200,
                                padding= ft.padding.only(top=25, bottom=45, left=25,right=25),
=======
        def CreateAPerfil(e):
            if self.form.height != 320:
                self.form.height = 320
                self.form.opacity = 100
                self.form.disabled=False
                self.button.visible=False
                self.footer.visible=False
                self.main.visible=False
                self.content.update()
                

        def CancelCreateAPerfil(e):
            if self.form.height != 1:
                self.form.height = 1
                self.form.opacity = 1
                self.form.disabled=True
                self.button.visible=True
                self.footer.visible=True
                self.main.visible=True
                self.content.update()
                
        self.form = ft.Container(
                                width=general_width,
                                height=1,
                                bgcolor="#3fe39f",
                                border_radius=40,
                                opacity=1,
                                #alignment=alignment.center,
                                #margin=ft.margin.only(left=-20,right=-20),
                                animate=ft.animation.Animation(400, "decelerate"),
                                animate_opacity=200,
                                padding= ft.padding.only(top=45, bottom=45, left=10,right=10),
>>>>>>> a8bdfc93c1a9388b0fc3baed18ffd87274c70643
                                content=ft.Column(
                                horizontal_alignment= ft.CrossAxisAlignment.CENTER, 
                                alignment= ft.MainAxisAlignment.CENTER,
                                    controls=
                                    [
<<<<<<< HEAD
                                        ft.Icon(ft.icons.ADD,color="white",size=40),
                                        ft.Text("Crea un nuevo perfil", size=20,text_align= ft.TextAlign.CENTER, color=ft.colors.WHITE, weight=ft.FontWeight.W_700),
                                        self.name_profile,
                                        self.type_profile,
                                        ft.Container(
                                            content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_EVENLY,vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.TextButton("Guardar", ft.icons.SAVE, height=40, icon_color="#3fe39f", on_click=(lambda e: (self.add_profile(e), self.CloseTheForm(e), self.checkIfProfiles(), self.show_profiles(),)), style= ft.ButtonStyle(bgcolor= ft.colors.WHITE, color="#3fe39f", shape=ft.RoundedRectangleBorder(radius=10))),
                                                    ft.TextButton("Cancelar", ft.icons.CANCEL, height=40, icon_color=ft.colors.WHITE, on_click=lambda e: self.CloseTheForm(e), style= ft.ButtonStyle(bgcolor=ft.colors.RED_400, color=ft.colors.WHITE, shape=ft.RoundedRectangleBorder(radius=10)))
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            )
        
        self.edit_form = ft.Container(
                                width=0,
                                height=0,
                                bgcolor="#3fe39f",
                                border_radius=30,
                                opacity=1,
                                margin=ft.margin.only(top=-10,bottom=-10),
                                animate=ft.animation.Animation(400, "decelerate"),
                                animate_opacity=200,
                                padding= ft.padding.only(top=25, bottom=45, left=25,right=25),
                                content=ft.Column(
                                horizontal_alignment= ft.CrossAxisAlignment.CENTER, 
                                alignment= ft.MainAxisAlignment.CENTER,
                                    controls=
                                    [
                                        ft.Icon(ft.icons.EDIT,color="white",size=40),
                                        ft.Text("Editar perfil", size=20,text_align= ft.TextAlign.CENTER, color=ft.colors.WHITE, weight=ft.FontWeight.W_700),
                                        self.edit_name_profile,
                                        self.edit_type_profile,
                                        ft.Container(
                                            content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_EVENLY,vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.TextButton("Guardar", ft.icons.SAVE, height=40, icon_color="#3fe39f", on_click=(lambda e: (self.update_data(e), e.page.update())), style= ft.ButtonStyle(bgcolor= ft.colors.WHITE, color="#3fe39f", shape=ft.RoundedRectangleBorder(radius=10))),
                                                    ft.TextButton("Cancelar", ft.icons.CANCEL, height=40, icon_color=ft.colors.WHITE, on_click=lambda e: self.CloseTheEditForm(e), style= ft.ButtonStyle(bgcolor=ft.colors.RED_400, color=ft.colors.WHITE, shape=ft.RoundedRectangleBorder(radius=10)))
=======
                                        ft.Text("Cree un nuevo perfil", text_align= ft.TextAlign.CENTER, color=ft.colors.GREY_900),
                                        self.name,
                                        self.type,
                                        ft.Container(
                                            content=ft.Row(alignment=ft.MainAxisAlignment.CENTER,
                                                controls=[
                                                    ft.TextButton("Guardar", ft.icons.SAVE, icon_color=ft.colors.WHITE, on_click=lambda e: CancelCreateAPerfil(e), style= ft.ButtonStyle(bgcolor="#3fe39f", color=ft.colors.WHITE, shape=ft.RoundedRectangleBorder(radius=10))),
                                                    ft.TextButton("Cancelar", ft.icons.CANCEL, icon_color=ft.colors.WHITE, on_click=lambda e: CancelCreateAPerfil(e), style= ft.ButtonStyle(bgcolor=ft.colors.RED_400, color=ft.colors.WHITE, shape=ft.RoundedRectangleBorder(radius=10)))
>>>>>>> a8bdfc93c1a9388b0fc3baed18ffd87274c70643
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            )

<<<<<<< HEAD
        self.button = ft.Container(width=80,
                                height=80,
=======

        self.table =  ft.Column(
                            controls=[
                                ft.DataTable(
                                        width=(general_width - 40),
                                        border_radius=5,
                                        height= profiles_containers_height,
                                        gradient= ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg2_grey_gradients),
                                        
                                )
                            ]       
        )

        self.button = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
             controls=[
                  ft.Container(width=75,
                                height=75,
>>>>>>> a8bdfc93c1a9388b0fc3baed18ffd87274c70643
                                margin=0,
                                gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=greens_gradients),
                                shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
<<<<<<< HEAD
                                        color=ft.colors.GREY_900,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                    ),
                                    border_radius=16,
                                    on_click=lambda e: self.CreateAProfile(e),
                                    content= ft.Icon(name=ft.icons.ADD, size=30,color=ft.colors.WHITE)
                                )

        self.done_display = ft.Container(width=general_width,
                                height=80,
                                margin=0,
                                padding=8,
                                visible=False,
                                bgcolor="#3fe39f",
                                shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
                                        color=ft.colors.GREY_900,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                    ),
                                    border_radius=16,
                                    content= ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[ft.Image(src="assets/logos/check_icon.png",width=40,color="white"),ft.Text("Los cambios en el perfil se han guardado con éxito.", text_align=ft.TextAlign.CENTER ,size=13, color="white")])
                                )

        self.fields_error = ft.Container(width=general_width,
                                height=80,
                                margin=0,
                                padding=10,
                                visible=False,
                                bgcolor=ft.colors.RED_400,
                                shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
                                        color=ft.colors.GREY_900,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                    ),
                                    border_radius=16,
                                    content= ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[ft.Image(src="assets/logos/caution_icon.png",width=40,color="white"),ft.Text("Completa todos los campos para crear perfil", text_align=ft.TextAlign.CENTER ,size=15, color="white")])
                                )
        self.footer = ft.Text("Optigy® Todos los derechos reservados", text_align= ft.TextAlign.CENTER, font_family="arial", size=12, weight=ft.FontWeight.W_700, color=ft.colors.GREY_900)

        self.checkIfProfiles()
    
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            spacing=30,
=======
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
>>>>>>> a8bdfc93c1a9388b0fc3baed18ffd87274c70643
            scroll="auto",
            controls=[
                self.main,
                self.table,
<<<<<<< HEAD
                self.void_table,
                self.form,
                self.edit_form,
                delete_profile_display,
                self.button,
                self.done_display,
                self.fields_error,
                self.footer,
            ]
        )

    def checkIfProfiles(self):
        datas = self.data_base.get_profile()
        for x in range(1):
            if len(datas) == 0:
                self.void_table.visible=True
                self.table.visible=False
                break
            else:
                self.void_table.visible=False
                self.table.visible=True
                break


    def show_profiles(self):

        self.profile_table.rows.clear()
        
        for x in self.data_base.get_profile():
            logo_show = ft.Image(src="assets/logos/IconGeneric01.png", width=100,)

            if x[2] == "Casa":
                logo_show = ft.Image(src="assets/logos/home_icon_test_3.png", width=100)
            if x[2] == "Edificio":
                logo_show = ft.Image(src="assets/logos/IconEstabl01.png", width=100)
            if x[2] == "Nave":
                logo_show = ft.Image(src="assets/logos/Iconfabri01.png", width=100)
            if x[2] == "Otro":
                logo_show = ft.Image(src="assets/logos/IconGeneric01.png", width=100)

            self.profile_table.rows.append(
                  ft.DataRow(
                      on_select_changed=lambda e: (self.get_index(e), self.CloseTheForm(e), self.CloseTheEditForm(e) , general_data_table.update, general_rooms_table.update, e.page.update, e.page.go("/general")),
                      on_long_press=lambda e: (self.EditAProfile(e), self.get_index_to_edit(e), self.edit_filed_text(e)),
                       cells=[
                        ft.DataCell(content=ft.Column(width=(general_width-120),alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,spacing=15,controls=[ft.Text(value=x[0],size=0,color=ft.colors.TRANSPARENT),logo_show, ft.Text(value=x[1], text_align= ft.TextAlign.CENTER, font_family="arial",size=15, color= ft.colors.GREY_700, weight=ft.FontWeight.W_700)]),),
                       ]
                  )
            )

        

    def CreateAProfile(self, e):
        if self.form.height != 375:
            self.update()
            self.form.height = 375
            self.form.width = general_width
            self.form.opacity = 1
            self.form.disabled=False
            self.button.visible=False
            self.profile_table.expand = True
            self.footer.visible=False
            self.main.visible=False
            self.clean_fields()
            self.update()
            self.content.update()

    def CloseTheForm(self,e):
        if self.form.height != 0:
            self.update()
            self.form.height = 0
            self.form.width = 0
            self.form.opacity = 0
            self.form.disabled=True
            self.button.visible=True
            self.profile_table.expand = False
            self.footer.visible=True
            self.main.visible=True
            self.clean_fields()
            self.update()
            self.content.update()

    def EditAProfile(self, e):
        if self.edit_form.height != 375:
            self.update()
            self.edit_form.height = 375
            self.edit_form.width = general_width
            self.edit_form.opacity = 1
            self.edit_form.disabled=False
            self.button.visible=False
            self.profile_table.expand = True
            self.footer.visible=False
            self.main.visible=False
            self.clean_fields()
            self.update()
            self.content.update()

    def CloseTheEditForm(self,e):
        if self.edit_form.height != 0:
            self.update()
            self.edit_form.height = 0
            self.edit_form.width = 0
            self.edit_form.opacity = 0
            self.edit_form.disabled=True
            self.button.visible=True
            self.footer.visible=True
            self.profile_table.expand = False
            self.main.visible=True
            self.clean_edit_fields()
            self.update()
            self.content.update()
    
    def Done_Edit(self, e):
        if self.edit_form.height != 0:
            self.update()
            self.clean_edit_fields()
            self.edit_form.height = 0
            self.edit_form.width = 0
            self.edit_form.opacity = 0
            self.edit_form.disabled=True
            self.done_display.visible = True
            self.footer.visible=True
            self.main.visible=True
            self.update()
            time.sleep(3)
            self.done_display.visible = False
            self.button.visible = True
            self.profile_table.expand = False
            self.update()
            self.content.update()

    
    def get_index_to_edit(self,e):
        #if e.control.selected:
           #e.control.selected = False
        #else:
           #e.control.selected = True
        
        name = e.control.cells[0].content.controls[2].value

        for x in self.data_base.get_profile():
            if x[1] == name:
                self.selected_profile = x
                break
        
        #self.update()

    def edit_filed_text(self,e):
        try:
            self.edit_name_profile.value = self.selected_profile[1]
            self.edit_type_profile.value = self.selected_profile[2]
            self.update()
        except:
            print("ERROR TO CATCH EDIT")

    def update_data(self, e):
        name = self.edit_name_profile.value
        type = self.edit_type_profile.value

        if len(name) and len(type) > 0:
            self.clean_edit_fields()
            self.data_base.update_profile(name, type, self.selected_profile[0])
            self.show_profiles()
            self.Done_Edit(e)
            self.update()


    def get_index(self,e):
        
        id = e.control.cells[0].content.controls[0].value

        to_general_name= e.control.cells[0].content.controls[2].value
        to_general_consumtion = self.data_base.get_general_consumtion(id)

        new_general_consumtion = 0

        for x in self.data_base.get_rooms_consumtion(id):
            new_general_consumtion += x

        if new_general_consumtion == 0:
            pp = "0.00"
            int_part, decimal_part  = pp.split('.')

        elif new_general_consumtion != 0:
            format_new_general_consumtion = "{:.2f}".format(to_general_consumtion)
            int_part, decimal_part  = format_new_general_consumtion.split('.')

        exp = self.data_base.get_consumtion_esp(id)

        if to_general_consumtion > exp:
            data_table.border= ft.border.all(color=ft.colors.RED_400, width=2)
            text_color = ft.colors.RED_400
        elif to_general_consumtion > (exp * 0.9) and to_general_consumtion < exp:
            data_table.border= ft.border.all(color=ft.colors.YELLOW_800, width=2)
            text_color = ft.colors.YELLOW_800
        else:
            data_table.border= ft.border.all(color=ft.colors.GREEN_500, width=2)
            text_color = ft.colors.GREEN_500
        
        print(f'The consumtion is {to_general_consumtion}')

        name_to_settings = e.control.cells[0].content.controls[2].value
        exp_consumition_db_value = self.data_base.get_consumtion_esp(id)

        def display_settings():
            settings_title_table.content.controls[1].value = name_to_settings
            exp_consumition_field.value = exp_consumition_db_value

        general_data_table.controls.clear()
        general_data_table.controls.append(ft.Text(f'{id}', size=0, color=ft.colors.TRANSPARENT))
        general_data_table.controls.append(ft.Row(vertical_alignment=ft.CrossAxisAlignment.CENTER, controls=[ft.Container(gradient= ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center, colors= bg_e_grey_gradients), border_radius=100, padding=6, height=38, width=38, on_click= lambda e: (display_settings(), e.page.go("/settings"), e.page.update()), content=ft.Image(src="assets/logos/Engranaje_icon.png", height=15,width=15, color=ft.colors.GREY_800)), ft.Text("Consumo Mensual:", size=20, color=ft.colors.GREY_800, font_family="arial", weight=ft.FontWeight.BOLD)]))
        general_data_table.controls.append(ft.Row(spacing=2, alignment="center",vertical_alignment=ft.CrossAxisAlignment.END,controls=[ft.Text(f"\t\t{int_part}", size=45, color=text_color, font_family="arial"), ft.Text(f".{decimal_part}", size=15, color=text_color, font_family="arial")])),

        general_data_table.controls.append(ft.Text("kWh/mes", size=15, color=text_color, font_family="arial",weight=ft.FontWeight.W_600))
        general_data_table.controls.append(ft.Text(f'SOBRE: {to_general_name}', size=12, color=ft.colors.GREY_800, font_family="arial", weight=ft.FontWeight.W_700))

        show_rooms(lambda e: self.CloseTheForm(e))

        print(f"Enter to {to_general_name}, is the Profile {id}")

        self.update()

    def add_profile(self,e):
        name = self.name_profile.value
        type = self.type_profile.value

        if len(name) and len(type) >0:
            profile_exist = False
            for row in self.data_base.get_profile():
                if row[1] == name:
                    profile_exist = True
                    break

            if not profile_exist:
                self.clean_fields()
                self.data_base.add_profile(name,type)
                self.checkIfProfiles()
                self.show_profiles()
        else:
            print("one field is empty")
            self.update()
            self.CloseTheForm(e)
            self.button.visible = False
            self.fields_error.visible = True
            self.update()
            time.sleep(3)
            self.button.visible = True
            self.fields_error.visible = False
            self.update()

        self.content.update()

    def clean_fields(self):
        self.name_profile.value=""
        self.type_profile.value=""

    def clean_edit_fields(self):
        self.edit_name_profile.value=""
        self.edit_type_profile.value=""

    def build(self):
         return self.content


def _view_():
        return ft.View("/index", bgcolor=ft.colors.GREY_200,
                    controls=[
                        ft.Container(    width=1500,
=======
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
>>>>>>> a8bdfc93c1a9388b0fc3baed18ffd87274c70643
                            height=700,
                            margin=-10,
                            alignment=ft.alignment.center,
                            gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg_grey_gradients),
<<<<<<< HEAD
                            content=
                            ft.Stack([
                                ft.Image(src="assets/images/Rayo03_2.png", width=1500, height=150, repeat=ft.ImageRepeat.REPEAT, opacity=.2),
                                ft.Container(
                                    width=1500,
                                    height=700,
                                    margin=-10,
                                    alignment=ft.alignment.center,
                                    gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg_white_gradients),
                                    content= form()
                                )
                            ]),                 
                        )
                    ]       
                )
=======
                            content=form()                       
                        )
                    ]       
                )

        page.update()
>>>>>>> a8bdfc93c1a9388b0fc3baed18ffd87274c70643
