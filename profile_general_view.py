<<<<<<< HEAD
import flet as ft
from __module__ import delete_room_display, bg_white_gradients, bg_grey_gradients, dinamic_tips_bar, edit_form, back_button, get_all_rooms_consumtion, show_rooms, data_base, data_table, general_data_table, general_rooms_table, profiles_containers_height, general_width, greens_gradients
import time

class general(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)

        self.name = ft.TextField(label="Nombre", label_style= ft.TextStyle(color=ft.colors.GREY_900, weight= ft.FontWeight.W_500), height=75, border_color=ft.colors.RED_50, max_length=10, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200)
        self.type = ft.Dropdown(label="Icono", label_style= ft.TextStyle(color=ft.colors.GREY_900, weight= ft.FontWeight.W_500), height=75, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200, options=[ft.dropdown.Option("Living"), ft.dropdown.Option("Cocina"), ft.dropdown.Option("Baño"), ft.dropdown.Option("Dormitorio"), ft.dropdown.Option("Pasillo"), ft.dropdown.Option("Baño"), ft.dropdown.Option("Garaje"), ft.dropdown.Option("Otro")])

        self.selected_room = None
        
        self.edit_name = ft.TextField(label="Nombre", label_style= ft.TextStyle(color=ft.colors.GREY_900, weight= ft.FontWeight.W_500), height=75, border_color=ft.colors.RED_50, max_length=10, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200)
        self.edit_type = ft.Dropdown(label="Icono", label_style= ft.TextStyle(color=ft.colors.GREY_900, weight= ft.FontWeight.W_500), height=75, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200, options=[ft.dropdown.Option("Casa"), ft.dropdown.Option("Edificio"), ft.dropdown.Option("Nave"), ft.dropdown.Option("Otro")])

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
                                content=ft.Column(
                                horizontal_alignment= ft.CrossAxisAlignment.CENTER, 
                                alignment= ft.MainAxisAlignment.CENTER,
                                    controls=
                                    [
                                        ft.Icon(ft.icons.ADD, color="white", size=40),
                                        ft.Text("Registre un nueva habitación", size=20,text_align= ft.TextAlign.CENTER, color=ft.colors.WHITE, weight=ft.FontWeight.W_700),
                                        self.name,
                                        self.type,
                                        ft.Container(
                                            content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_EVENLY,vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.TextButton("Guardar", ft.icons.SAVE, height=40, icon_color="#3fe39f", on_click=(lambda e: (self.add_room(e), self.CloseTheForm(e),get_all_rooms_consumtion(),general_data_table.update,show_rooms(lambda e: self.CloseTheForm(e)),)), style= ft.ButtonStyle(bgcolor= ft.colors.WHITE, color="#3fe39f", shape=ft.RoundedRectangleBorder(radius=10))),
                                                    ft.TextButton("Cancelar", ft.icons.CANCEL, height=40, icon_color=ft.colors.WHITE, on_click=lambda e: self.CloseTheForm(e), style= ft.ButtonStyle(bgcolor=ft.colors.RED_400, color=ft.colors.WHITE, shape=ft.RoundedRectangleBorder(radius=10)))
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            )

        self.table =  ft.Container(
                        width=(general_width - 30),
                        border_radius=5,
                        height= profiles_containers_height + 25,
                        content=ft.Column(
                            expand = True,
                            scroll = ft.ScrollMode.ALWAYS,
                            width=float("inf"),
                            disabled=False,
                            controls=[
                                    general_rooms_table
                            ]
                        )                                        
        )

        self.button = ft.Container(width=80,
                                height=80,
                                margin=0,
                                gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=greens_gradients),
                                shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
                                        color=ft.colors.GREY_900,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                    ),
                                    border_radius=16,
                                    on_click=lambda e: (self.RegisterARoom(e),get_all_rooms_consumtion(),general_data_table.update),
                                    content= ft.Icon(name=ft.icons.ADD, size=30,color=ft.colors.WHITE)
                                )

        self.fields_error = ft.Container(width=general_width,
                                height=80,
                                margin=0,
                                padding=8,
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
                                    content= ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[ft.Image(src="assets/logos/caution_icon.png",width=40,color="white"),ft.Text("Completa todos los campos para registrar una habitación", text_align=ft.TextAlign.CENTER ,size=13, color="white")])
                                )
        self.footer = ft.Text("Optigy® Todos los derechos reservados", text_align= ft.TextAlign.CENTER, font_family="arial", size=12, weight=ft.FontWeight.W_700, color=ft.colors.GREY_900)
        
                  
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            spacing=13,
            scroll="auto",
            controls=[
                back_button("/index",(lambda e: self.CloseTheForm(e))),
                data_table,
                dinamic_tips_bar,
                self.table,
                self.form,
                edit_form,
                delete_room_display,
                self.button,
                self.fields_error,
                self.footer,
            ]
        )

    def clean_fields(self):
        self.name.value=""
        self.type.value=""

    def add_room(self,e):
        name = self.name.value
        type = self.type.value

        profile_id = data_table.content.controls[0].value

        if len(name) and len(type) > 0:
            room_exist = False
            for row in data_base.get_rooms(profile_id):
                if row[1] == name:
                    room_exist = True
                    break

            if not room_exist:
                self.clean_fields()
                data_base.add_room(profile_id, name, type)
                show_rooms(lambda e: self.CloseTheForm(e))
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

    def RegisterARoom(self, e):
        if self.form.height != 375:
            self.update()
            self.form.height = 375
            self.form.width = general_width
            self.form.opacity = 1
            dinamic_tips_bar.visible = False
            self.form.disabled=False
            self.button.visible=False
            self.footer.visible=False
            data_table.visible = False
            self.clean_fields()
            self.update()
            self.content.update()

    def CloseTheForm(self, e):
        if self.form.height != 0:
            self.update()
            self.form.height = 0
            self.form.width = 0
            self.form.opacity = 0
            dinamic_tips_bar.visible = True
            self.form.disabled=True
            self.button.visible=True
            self.footer.visible=True
            data_table.visible = True
            self.clean_fields()
            self.update()
            self.content.update()

    def build(self):
        return self.content

def _view_():
        return ft.View("/general", bgcolor=ft.colors.GREY_200,
                    controls=[
                        ft.Container(    width=1500,
                            height=700,
                            margin=-10,
                            alignment=ft.alignment.center,
                            gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg_grey_gradients),
                            content=
                            ft.Stack([
                                ft.Image(src="assets/images/Rayo03_2.png", width=1500, height=150, repeat=ft.ImageRepeat.REPEAT, opacity=.2),
                                ft.Container(
                                    width=1500,
                                    height=700,
                                    margin=-10,
                                    alignment=ft.alignment.center,
                                    gradient=ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg_white_gradients),
                                    content= general()
                                )
                            ]),                 
                        )
                    ]       
                )
=======
from flet import View, Text, ElevatedButton, colors, AppBar

def _view_():
    return View("/general", bgcolor=colors.GREY_400,
                controls=[
                    AppBar(title=Text("Profile"), bgcolor=colors.SURFACE_VARIANT),
                    ElevatedButton("Go Home", on_click=lambda e: e.page.go("/index")),
                ]
            )
>>>>>>> a8bdfc93c1a9388b0fc3baed18ffd87274c70643
