import flet as ft
from __module__ import delete_profile_apears,bg_grey_gradients,bg_white_gradients,delete_profile, generate_new_settings_button,back_button, exp_consumition_field, settings_title_table, compare_exp_and_current_consumtion, show_rooms, data_base, general_data_table, profiles_containers_height, general_width
import time

def square_color(color_r, size_r):
     return ft.Container(bgcolor= color_r, width= size_r, height= size_r)
            
class settings(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)

        self.saveButton = ft.TextButton("Guardar cambios", ft.icons.SAVE, width=200, height=40, icon_color="white", on_click=lambda e: (self.update_profile_exp(e), e.page.update()), style= ft.ButtonStyle(bgcolor="#3fe39f" , color=ft.colors.WHITE, shape=ft.RoundedRectangleBorder(radius=10)))
        self.deleteButton = ft.TextButton("Eliminar perfil", ft.icons.DELETE, width=200, height=40, icon_color=ft.colors.WHITE, on_click=lambda e: (delete_profile(e), e.page.go("/index"), delete_profile_apears(), e.page.update()), style= ft.ButtonStyle(bgcolor="red", color=ft.colors.WHITE, shape=ft.RoundedRectangleBorder(radius=10)))

        self.title=ft.Container(
                        border_radius=5,
                        padding=10,
                        bgcolor=ft.colors.GREY_700,
                        height= profiles_containers_height - 125,
                        content=
                            ft.Column(
                                expand = True,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                disabled=False,
                                spacing=1,
                                controls=[
                                        settings_title_table
                                ]
                        )                                        
        )
        
        self.range_logo = ft.Column(alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment= ft.CrossAxisAlignment.CENTER, controls=[ft.Image(src="assets/images/Rango01.png", width=90)])

        self.body =  ft.Container(
                        width=(general_width - 30),
                        padding=20,
                        border_radius=5,
                        bgcolor=ft.colors.GREY_700,
                        height= profiles_containers_height + 60,
                        content=ft.Column(
                            expand = True,
                            scroll = ft.ScrollMode.ALWAYS,
                            width=float("inf"),
                            disabled=False,
                            controls=[
                                 ft.Column(alignment=ft.MainAxisAlignment.CENTER,
                                           horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                           spacing = 1,
                                           controls=
                                           [
                                                ft.Column(alignment=ft.MainAxisAlignment.START,
                                                          spacing=1, 
                                                          horizontal_alignment= ft.CrossAxisAlignment.START,
                                                          controls=[
                                                                exp_consumition_field,
                                                                ft.Text("*Establece el valor máximo de consumo mensual*", font_family="arial", size=11, color="#3fe39f"),
                                                                ft.Text("Al superar este valor establecido significará que tu consumo no es óptimo bajo tu criterio.", font_family="arial", size=11, color="white"),
                                                                ft.Text("\nEl consumo promedio de un hogar es de 300-400kWh/mes.", font_family="arial", size=10.5, color="white"),
                                                                ft.Row(alignment= ft.MainAxisAlignment.START, vertical_alignment= ft.CrossAxisAlignment.CENTER, controls=[square_color("#3fe39f",10), ft.Text("Consumo óptimo", size=10,color="#3fe39f")]),
                                                                ft.Row(alignment= ft.MainAxisAlignment.START, vertical_alignment= ft.CrossAxisAlignment.CENTER, controls=[square_color(ft.colors.YELLOW_800,10), ft.Text("Consumo regular", size=10,color=ft.colors.YELLOW_800)]),
                                                                ft.Row(alignment= ft.MainAxisAlignment.START, vertical_alignment= ft.CrossAxisAlignment.CENTER, controls=[square_color("red",10), ft.Text("Consumo ineficiente", size=10,color="red")]),

                                                          ]
                                                          )
                                           ]),
                            ]
                        )                                        
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
            spacing=15,
            scroll="auto",
            controls=[
                back_button("/general",(lambda e: e.page.update())),
                self.title,
                self.range_logo,
                self.body,
                self.done_display,
                self.error_display,
                self.saveButton,
                self.deleteButton,
                self.footer,
            ]
        )

    def update_profile_exp(self,e):
        new_exp_consumition = exp_consumition_field.value
        id = general_data_table.controls[0].value

        if len(new_exp_consumition) > 0:
            self.update()
            data_base.update_consumtion_esp(new_exp_consumition, id)
            exp_consumition_field.value = new_exp_consumition
            compare_exp_and_current_consumtion()
            show_rooms(lambda e: e.page.update())
            generate_new_settings_button()
            print("DONE: Change exp")
            self.done_display.visible = True
            self.saveButton.visible = False
            self.deleteButton.visible = False
            self.update()
            time.sleep(3)
            self.done_display.visible = False
            self.saveButton.visible = True
            self.deleteButton.visible = True
            self.update()
        else:
            print("ERROR: change exp value")
            self.update()
            exp_consumition_field.value = new_exp_consumition
            compare_exp_and_current_consumtion()
            self.error_display.visible = True
            self.saveButton.visible = False
            self.deleteButton.visible = False
            self.error_display.content.controls[1].value = "El valor de consumo óptimo no puede quedar vacío."
            self.error_display.content.controls[1].size = 14
            exp_consumition_field.value = data_base.get_consumtion_esp(id)
            self.update()
            time.sleep(3)
            self.error_display.visible = False
            self.saveButton.visible = True
            self.deleteButton.visible = True
            self.update()

    def build(self):
        return self.content

def _view_():
        return ft.View("/settings", bgcolor=ft.colors.GREY_200,
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
                                    content= settings()
                                )
                            ]),                 
                        )
                    ]       
                )