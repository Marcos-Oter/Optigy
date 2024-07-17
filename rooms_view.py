import flet as ft
from __module__ import delete_element_display,bg_white_gradients,bg_grey_gradients,get_all_elements_consumtion, show_elements, compare_exp_and_current_consumtion, back_button, get_all_rooms_consumtion, show_rooms, data_base, particular_room_data_table, particular_elements_table, general_data_table, general_rooms_table, bg2_grey_gradients, profiles_containers_height, general_width, greens_gradients
import time

form_fields = 65

class elements(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)

        self.name = ft.TextField(label="Nombre", label_style= ft.TextStyle(color=ft.colors.GREY_900, weight= ft.FontWeight.W_500), height=form_fields, border_color=ft.colors.RED_50, max_length=10, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200)
        self.amount = ft.TextField(label="Cantidad", value="1", keyboard_type=ft.KeyboardType.NUMBER, label_style= ft.TextStyle(color=ft.colors.GREY_900, weight= ft.FontWeight.W_500), height=form_fields, border_color=ft.colors.RED_50, max_length=3, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200, input_filter= ft.NumbersOnlyInputFilter())
        self.watt = ft.TextField(label="Vatio/Watt (W)", suffix_text="W",suffix_style=ft.TextStyle(color="black"), keyboard_type=ft.KeyboardType.NUMBER, label_style= ft.TextStyle(color=ft.colors.GREY_900, weight= ft.FontWeight.W_500), height=form_fields, border_color=ft.colors.RED_50, max_length=6, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200, input_filter= ft.InputFilter(allow=True, regex_string= r'[.-0-1-2-3-4-5-6-7-8-9]'))
        self.hours = ft.TextField(label="Horas", suffix_text="hs",suffix_style=ft.TextStyle(color="black"), width=(general_width/2.5), on_focus=self.clean_hours_minutes, on_change= self.change_hours_minutes, keyboard_type=ft.KeyboardType.NUMBER,label_style= ft.TextStyle(color=ft.colors.GREY_900, weight= ft.FontWeight.W_500), height=form_fields, border_color=ft.colors.RED_50, max_length=2, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200, input_filter= ft.InputFilter(allow=True, regex_string= r'[.-0-1-2-3-4-5-6-7-8-9]'))
        self.minutes = ft.TextField(label="Minutos", suffix_text="min", suffix_style=ft.TextStyle(color="black"), width=(general_width/2.5), on_focus=self.clean_hours_minutes, on_change= self.change_hours_minutes, keyboard_type=ft.KeyboardType.NUMBER, label_style= ft.TextStyle(color=ft.colors.GREY_900, weight= ft.FontWeight.W_500), height=form_fields, border_color=ft.colors.RED_50, max_length=2, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200, input_filter= ft.InputFilter(allow=True, regex_string= r'[.-0-1-2-3-4-5-6-7-8-9]'))

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
                                        ft.Icon(ft.icons.ENERGY_SAVINGS_LEAF_SHARP, color="white", size=40),
                                        ft.Text("Registre un nuevo elemento de consumo", size=15,text_align= ft.TextAlign.CENTER, color=ft.colors.WHITE, weight=ft.FontWeight.W_700),
                                        self.name,
                                        self.amount,
                                        self.watt,
                                        ft.Row(alignment=ft.MainAxisAlignment.CENTER,vertical_alignment=ft.CrossAxisAlignment.CENTER,width=(general_width),controls=[self.hours,ft.Text(":",text_align=ft.TextAlign.CENTER,weight=ft.FontWeight.W_700,size=20,color=ft.colors.GREY_900),self.minutes]),
                                        ft.Container(
                                            content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_EVENLY,vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.TextButton("Guardar", ft.icons.SAVE, height=40, icon_color="#3fe39f", on_click=(lambda e: (self.add_element(e),self.CloseTheForm(e),get_all_elements_consumtion(),get_all_rooms_consumtion(), general_data_table.update, self.content.update(), get_all_elements_consumtion(), particular_room_data_table.update, show_rooms(lambda e: self.CloseTheForm(e)), compare_exp_and_current_consumtion(), general_data_table.update, general_rooms_table.update, e.page.update())), style= ft.ButtonStyle(bgcolor= ft.colors.WHITE, color="#3fe39f", shape=ft.RoundedRectangleBorder(radius=10))),
                                                    ft.TextButton("Cancelar", ft.icons.CANCEL, height=40, icon_color=ft.colors.WHITE, on_click=lambda e: self.CloseTheForm(e), style= ft.ButtonStyle(bgcolor=ft.colors.RED_400, color=ft.colors.WHITE, shape=ft.RoundedRectangleBorder(radius=10)))
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            )

        self.data_table =  ft.Container(
                        width=(general_width - 80),
                        border_radius=5,
                        padding=2,
                        height= (profiles_containers_height),
                        shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=10,
                                        color=ft.colors.GREY_500,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                    ),
                        gradient= ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg2_grey_gradients),
                        content= particular_room_data_table                       
        )

        self.table =  ft.Container(
                        width=(general_width - 25),
                        border_radius=5,
                        height= profiles_containers_height + 25,
                        content=ft.Column(
                            expand = True,
                            scroll = ft.ScrollMode.ALWAYS,
                            width=float("inf"),
                            disabled=False,
                            controls=[
                                    particular_elements_table
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
                                    on_click=lambda e: (self.RegisterAElement(e),),
                                    content= ft.Icon(name=ft.icons.ADD, size=30,color=ft.colors.WHITE)
                                )
        
        self.error_display = ft.Container(width=general_width,
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
                                    content= ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[ft.Image(src="assets/logos/caution_icon.png",width=40,color="white"),ft.Text("", text_align=ft.TextAlign.CENTER ,size=14, color="white")])
                                )
        self.footer = ft.Text("Optigy® Todos los derechos reservados", text_align= ft.TextAlign.CENTER, font_family="arial", size=12, weight=ft.FontWeight.W_700, color=ft.colors.GREY_900)
    
        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            spacing=20,
            scroll="auto",
            controls=[
                back_button("/general", (lambda e: self.CloseTheForm(e))),
                self.data_table,
                self.table,
                self.form,
                delete_element_display,
                self.button,
                self.error_display,
                self.footer,
            ]
        )

    def clean_fields(self):
        self.name.value=""
        self.amount.value="1"
        self.watt.value=""
        self.hours.value="00"
        self.minutes.value="00"

    def clean_hours_minutes(self,e):
        e.control.value = ""
        self.content.update()   

    def change_hours_minutes(self,e):
        if e.control.value == "":
            e.control.value = "00"

        self.content.update() 

    def RegisterAElement(self, e):
        if self.form.height != 550:
            self.form.height = 550
            self.form.width = general_width
            self.form.opacity = 1
            self.form.disabled=False
            self.button.visible=False
            self.footer.visible=False
            self.data_table.visible = False
            self.table.visible = False
            self.clean_fields()
            self.content.update()

    def CloseTheForm(self, e):
        if self.form.height != 0:
            self.form.height = 0
            self.form.width = 0
            self.form.opacity = 0
            self.form.disabled=True
            self.button.visible=True
            self.footer.visible=True
            self.data_table.visible = True
            self.table.visible = True
            self.clean_fields()
            self.content.update()

    def add_element(self,e):
        name = self.name.value
        amount = self.amount.value
        watt = self.watt.value
        hours= self.hours.value
        minutes= self.minutes.value

        rooms_id = self.data_table.content.controls[0].value

        if (len(name) and len(amount) and len(watt) and len(hours) and len(minutes) > 0) and (int(hours) > 24):
            print("hours exceded")
            self.CloseTheForm(e)
            self.button.visible = False
            self.error_display.visible = True
            self.error_display.content.controls[1].value = "La cantidad de horas deben ser igual o menor a 24."
            self.error_display.content.controls[1].size = 14
            self.update()
            time.sleep(3)
            self.button.visible = True
            self.error_display.visible = False
            self.update()

        elif (len(name) and len(amount) and len(watt) and len(hours) and len(minutes) > 0) and (int(minutes) > 59):
            print("day consumtion exceded")
            self.CloseTheForm(e)
            self.button.visible = False
            self.error_display.visible = True
            self.error_display.content.controls[1].value = "La cantidad de minutos deben ser menor a 60."
            self.error_display.content.controls[1].size = 14
            self.update()
            time.sleep(3)
            self.button.visible = True
            self.error_display.visible = False
            self.update()
        
        elif (len(name) and len(amount) and len(watt) and len(hours) and len(minutes) > 0) and (int(hours) and int(minutes) > 0):
            print("minutes exceded")
            self.CloseTheForm(e)
            self.button.visible = False
            self.error_display.visible = True
            self.error_display.content.controls[1].value = "El consumo no puede exceder las 24 horas."
            self.error_display.content.controls[1].size = 14
            self.update()
            time.sleep(3)
            self.button.visible = True
            self.error_display.visible = False
            self.update()

        elif len(name) and len(amount) and len(watt) > 0 and (len(hours) or len(minutes) > 0):

            time_r = (int(hours) + (int(minutes)/60))

            print(f"Total time is: {time_r}")

            kw = ((float(watt) * int(amount)) / 1000)
            kw_hours = (float(kw) * float(time_r))

            print(f'{kw_hours} es el consumo')

            self.clean_fields()
            data_base.add_element(rooms_id, name, amount, kw_hours)
            show_elements()
        else:
            print("one field is empty")
            self.CloseTheForm(e)
            self.button.visible = False
            self.error_display.visible = True
            self.error_display.content.controls[1].value = "Completa todos los campos para registrar un elemento"
            self.error_display.content.controls[1].size = 13
            self.update()
            time.sleep(3)
            self.button.visible = True
            self.error_display.visible = False
            self.update()

        self.content.update()
    
    def build(self):
        return self.content

def _view_():
        return ft.View("/rooms", bgcolor=ft.colors.GREY_200,
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
                                    content= elements()
                                )
                            ]),                 
                        )
                    ]       
                )