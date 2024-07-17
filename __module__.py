# LAS DIFERENTES VIEWS HARÁN REFERENCIA A ESTAS VARIABLES PARA INTERACTUAR DINÁMICAMENTE ENTRE ELLAS. 
# CAMBIANDO ASÍ EN TIEMPO REAL EL CONTENIDO DE CADA SECCIÓN O VIEW

import flet as ft
from profile_manager_db import ProfileManager
import time

#-----------------Vars

general_width= 360
profiles_containers_height = 180
greens_gradients = ["#3dc7a5","#3dc7a5","#3dc7a5","#3dc7a5","#3dc7a5","#3dc7a5","#3dc7a5","#3dc7a5","#3ADAAC","#39EEA3", "#39EEA3","#32FAA7","#32FAA7"]
grey_gradients = ["#E5E7E9","#E5E7E9","#E5E7E9","#E5E7E9","#E5E7E9","#A6ACAF","#A6ACAF","#A6ACAF"]
bg_grey_gradients = [ft.colors.GREY_500, ft.colors.GREY_500, ft.colors.GREY_400, ft.colors.GREY_300,ft.colors.GREY_200, ft.colors.GREY_200, ft.colors.GREY_200, ft.colors.GREY_200, ft.colors.GREY_200, ft.colors.GREY_200, ft.colors.GREY_200, ft.colors.GREY_200, ft.colors.GREY_200]
bg_e_grey_gradients = [ft.colors.GREY_400, ft.colors.GREY_400, ft.colors.GREY_400, ft.colors.GREY_300,ft.colors.GREY_200,]
bg2_grey_gradients = [ft.colors.GREY_400,ft.colors.GREY_300,ft.colors.GREY_200, ft.colors.WHITE, ft.colors.WHITE, ft.colors.WHITE, ft.colors.WHITE, ft.colors.WHITE]
bg_white_gradients = [ft.colors.TRANSPARENT, ft.colors.TRANSPARENT, ft.colors.TRANSPARENT, ft.colors.TRANSPARENT,ft.colors.TRANSPARENT, ft.colors.TRANSPARENT, ft.colors.TRANSPARENT, ft.colors.TRANSPARENT, ft.colors.TRANSPARENT, ft.colors.TRANSPARENT]

#-----------------BACK_BUTTON

def back_button(route, close_form):
    return ft.Row([ft.ElevatedButton(icon=ft.icons.ARROW_BACK,text="\tAtrás",icon_color="#3dc7a5", color="white", bgcolor=ft.colors.GREY_800,on_click=lambda e: (e.page.go(route), close_form(e),))])

#-----------------IN ALL VIEWS

footer = ft.Text("Optigy® Todos los derechos reservados", text_align= ft.TextAlign.CENTER, font_family="arial", size=12, weight=ft.FontWeight.W_700, color=ft.colors.GREY_900)

#-----------------GENERAL PROFILE VIEW

general_data_table= ft.Column(
                                expand = True,
                                scroll = ft.ScrollMode.ALWAYS,
                                width=float("inf"),
                                disabled=False,
                                spacing=3,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[]) 
 
general_rooms_table = ft.GridView(
                                expand=False,
                                padding= ft.padding.only(left=20,right=20,top=5,bottom=5),
                                runs_count=20,
                                max_extent=150,
                                spacing=20,
                                run_spacing=25,
                                child_aspect_ratio=1.15,
                                controls=[])

data_table =  ft.Container(
                        width=(general_width - 80),
                        #border=ft.border.all(color="green",width=2),
                        border_radius=5,
                        padding=5,
                        height= (profiles_containers_height-15),
                        shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=10,
                                        color=ft.colors.GREY_500,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                    ),
                        gradient= ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg2_grey_gradients),
                        content= general_data_table                        
        )

#-----------------------ROOM VIEW

particular_room_data_table= ft.Column(
                                expand = True,
                                scroll = ft.ScrollMode.ALWAYS,
                                width=float("inf"),
                                disabled=False,
                                spacing=5,
                                alignment=ft.MainAxisAlignment.CENTER,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[]) 
 
particular_elements_table = ft.Column(
                                expand=False,
                                spacing=20,
                                run_spacing=25,
                                controls=[])

#-----------------------SETTINGS VIEW

settings_title_table = ft.Container(width=general_width, content=ft.Column(spacing=1,alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[ft.Text(value="Configurar valores de consumo de:",  color="white", size=15, weight="bold"), ft.Text(value=f"{'profile'}", color="#3fe39f", size=15, weight="bold")]))

exp_consumition_field = ft.TextField(label="Valor máximo esperado de kWh/mes", counter_style=ft.TextStyle(color=ft.colors.TRANSPARENT,size=0), width= general_width, suffix_text="kWh/mes", suffix_style=ft.TextStyle(color="black"), keyboard_type=ft.KeyboardType.NUMBER, label_style= ft.TextStyle(color=ft.colors.GREEN_500, weight= ft.FontWeight.W_500, font_family="arial"), height=55, border_color=ft.colors.RED_50, max_length=8, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200, input_filter= ft.InputFilter(allow=True, regex_string= r'[.-0-1-2-3-4-5-6-7-8-9]'))
#-----------------------Data base

data_base = ProfileManager()

#-----------------------Functions

def compare_exp_and_current_consumtion():

    id = general_data_table.controls[0].value
    to_general_consumtion = data_base.get_general_consumtion(id)
    exp = data_base.get_consumtion_esp(id)

    if to_general_consumtion > exp:
        data_table.border= ft.border.all(color="red", width=2)
        text_color = ft.colors.RED_400
    elif to_general_consumtion > (exp * 0.9) and to_general_consumtion < exp:
        data_table.border= ft.border.all(color=ft.colors.YELLOW_800, width=2)
        text_color = ft.colors.YELLOW_800
    else:
        data_table.border= ft.border.all(color=ft.colors.GREEN_500, width=2)
        text_color = ft.colors.GREEN_500

    general_data_table.controls[2].controls[0].color = text_color
    general_data_table.controls[2].controls[1].color = text_color

    general_data_table.controls[3].color = text_color

def get_all_rooms_consumtion():
    new_general_consumtion = 0
    id = general_data_table.controls[0].value
    #Esta es la cantidad promedio de días al mes
    average_days_per_month = 30.4167

    for x in data_base.get_rooms_consumtion(id):
        new_general_consumtion += x
            
    new_general_consumtion_month = new_general_consumtion * average_days_per_month
    format_new_general_consumtion = "{:.2f}".format(new_general_consumtion_month)
    int_part, decimal_part  = format_new_general_consumtion.split('.')        
    print(new_general_consumtion_month)

    general_data_table.controls[2].controls[0].value = f'\t\t{int_part}'
    general_data_table.controls[2].controls[1].value = f',{decimal_part}'
    data_base.update_general_consumition(new_general_consumtion_month, id)

def show_rooms(close_form):
    general_rooms_table.controls= []
    #general_rooms_table.controls.clear()

    rooms_id = general_data_table.controls[0].value

    current_consumtion = data_base.get_general_consumtion(rooms_id)
    exp = data_base.get_consumtion_esp(rooms_id)

    print(f"SHOW ROOMS {rooms_id}")

    def get_the_most_bigger():
        num = []
        for x in data_base.get_rooms(rooms_id):
            num.append(x[3])

        the_most = max(num)
        print(f"THE MOST {the_most}")
        return the_most

    for x in data_base.get_rooms(rooms_id):

        def determine_logo():
            logo_show = ft.Image(src="assets/logos/IconGeneric02.png", width=50)
            if x[4] == "Living":
                logo_show = ft.Image(src="assets/logos/rooms/Iconliving01.png", width=50)
            if x[4] == "Cocina":
                logo_show = ft.Image(src="assets/logos/rooms/IconCocina01.png", width=50)
            if x[4] == "Baño":
                logo_show = ft.Image(src="assets/logos/rooms/IconBaño01.png", width=50)
            if x[4] == "Dormitorio":
                logo_show = ft.Image(src="assets/logos/rooms/IconDormi01.png", width=50)
            if x[4] == "Pasillo":
                logo_show = ft.Image(src="assets/logos/rooms/Iconpasillo01.png", width=50)
            if x[4] == "Garaje":
                logo_show = ft.Image(src="assets/logos/rooms/IconGarage01.png", width=50)
            if x[4] == "Otro":
                logo_show = ft.Image(src="assets/logos/rooms/IconGeneric02.png", width=50)

            return logo_show

        if (x[3] == get_the_most_bigger()) and (get_the_most_bigger() > 0) and (current_consumtion > exp):
            general_rooms_table.controls.append(
                                ft.Container(   width=(100),
                                                height=100, 
                                                border_radius= 5,
                                                border=ft.border.all(color = "red", width=1.5),
                                                gradient= ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg2_grey_gradients),
                                                shadow=ft.BoxShadow(
                                                spread_radius=.1,
                                                blur_radius=5,
                                                color=ft.colors.GREY_500,
                                                offset=ft.Offset(0, 0),
                                                blur_style=ft.ShadowBlurStyle.NORMAL,),  
                                                on_click=lambda e: (get_index_2(e),  e.page.go("/rooms"),close_form(e),),
                                                on_long_press=lambda e: (delete_room(e),e.page.update()),
                                                content=ft.Column(spacing=5, alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[ft.Text(x[1],size=0,color=ft.colors.TRANSPARENT),ft.Text(x[2],size=15,font_family="arial",color=ft.colors.GREY_800,weight=ft.FontWeight.W_700), determine_logo(), ft.Text(f'{"{:.3f}".format(x[3])} kWh',size=15,font_family="arial", color="red", weight=ft.FontWeight.W_700)]),
                                                ))
        elif (x[3] == get_the_most_bigger() and get_the_most_bigger() > 0) and (current_consumtion > (exp * 0.9) and (current_consumtion < exp)):
            general_rooms_table.controls.append(
                                ft.Container(   width=(100),
                                                height=100, 
                                                border_radius= 5,
                                                border=ft.border.all(color=ft.colors.YELLOW_800, width=1.5),
                                                gradient= ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg2_grey_gradients),
                                                shadow=ft.BoxShadow(
                                                spread_radius=.1,
                                                blur_radius=5,
                                                color=ft.colors.GREY_500,
                                                offset=ft.Offset(0, 0),
                                                blur_style=ft.ShadowBlurStyle.NORMAL,),  
                                                on_click=lambda e: (get_index_2(e), e.page.go("/rooms"), close_form(e)),
                                                on_long_press=lambda e: (delete_room(e),e.page.update()),
                                                content=ft.Column(spacing=5, alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[ft.Text(x[1],size=0,color=ft.colors.TRANSPARENT),ft.Text(x[2],size=15,font_family="arial",color=ft.colors.GREY_800,weight=ft.FontWeight.W_700), determine_logo(), ft.Text(f'{"{:.3f}".format(x[3])} kWh',size=15,font_family="arial",color=ft.colors.YELLOW_800, weight=ft.FontWeight.W_700)]),
                                                ))
        else:
            general_rooms_table.controls.append(
                                ft.Container(   width=(100),
                                                height=100, 
                                                border_radius= 5,
                                                gradient= ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center,colors=bg2_grey_gradients),
                                                shadow=ft.BoxShadow(
                                                spread_radius=.1,
                                                blur_radius=5,
                                                color=ft.colors.GREY_500,
                                                offset=ft.Offset(0, 0),
                                                blur_style=ft.ShadowBlurStyle.NORMAL,),  
                                                on_click=lambda e: (get_index_2(e), e.page.go("/rooms"), close_form(e),),
                                                on_long_press=lambda e: (delete_room(e),e.page.update()),
                                                content=ft.Column(spacing=5, alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[ft.Text(x[1],size=0,color=ft.colors.TRANSPARENT),ft.Text(x[2],size=15,font_family="arial",color=ft.colors.GREY_800,weight=ft.FontWeight.W_700), determine_logo(), ft.Text(f'{"{:.3f}".format(x[3])} kWh',size=15,font_family="arial",color=ft.colors.GREEN_500,weight=ft.FontWeight.W_700)]),
                                                ))

        
def get_index_2(e):

    room_id = e.control.content.controls[0].value
    room_name = e.control.content.controls[1].value
    room_img = e.control.content.controls[2].src
    room_consumtion = data_base.get_particular_room_consumtion(room_id)

    print(f'ROOM {room_id}')

    #El texto consumo de la habitación cambia dependiendo del estado optimo del consumo mensual del perfil.
    current_color = e.control.content.controls[3].color

    particular_room_data_table.controls.clear()
    particular_room_data_table.controls.append(ft.Text(f'{room_id}', size=0, color=ft.colors.TRANSPARENT))
    particular_room_data_table.controls.append(ft.Text(f'{room_name}', size=15, color=ft.colors.GREY_800, font_family="arial", weight=ft.FontWeight.BOLD))
    particular_room_data_table.controls.append(ft.Image(src=f'{room_img}', width=100))
    particular_room_data_table.controls.append(ft.Row(spacing=2, alignment="center",vertical_alignment=ft.CrossAxisAlignment.END,controls=[ft.Text(f'\t\t\t{"{:.3f}".format(room_consumtion)}', size=20, color= current_color, font_family="arial"), ft.Text(f' kWh', size=20, color= current_color, font_family="arial")]))

    particular_elements_table.controls.clear()

    for x in data_base.get_elements(room_id):
        particular_elements_table.controls.append(
                ft.Container(border_radius=5, on_long_press=lambda e: delete_element(e), on_click=lambda e: (e.page.update()),content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,vertical_alignment=ft.CrossAxisAlignment.CENTER,width=general_width,height=50,controls=[
                                            ft.Container(alignment=ft.alignment.center,width=(general_width-300),bgcolor="black", content=ft.Text(f'x{x[3]}',bgcolor="black",font_family="arial",weight=ft.FontWeight.W_500),),
                                            ft.Container(padding= 5,alignment=ft.alignment.center,width=(general_width-60),bgcolor="white", content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,vertical_alignment=ft.CrossAxisAlignment.CENTER,controls=[ft.Text(f'{x[2]}',color="black",font_family="arial",weight=ft.FontWeight.W_700),ft.Text(f'{x[1]}',color=ft.colors.TRANSPARENT, size=0),ft.Text(f'{"{:.3f}".format(x[4])} kWh',color="black", font_family="arial", weight=ft.FontWeight.W_700)],))]),
                                            ),
            )
        
def show_elements():
        room_id = particular_room_data_table.controls[0].value
        
        particular_elements_table.controls.clear()

        for x in data_base.get_elements(room_id):
            particular_elements_table.controls.append(
                ft.Container(border_radius=5, on_long_press=lambda e: delete_element(e), on_click=lambda e: (e.page.update()),content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_BETWEEN,vertical_alignment=ft.CrossAxisAlignment.CENTER,width=general_width,height=50,controls=[
                                            ft.Container(alignment=ft.alignment.center,width=(general_width-300),bgcolor="black", content=ft.Text(f'x{x[3]}',bgcolor="black",font_family="arial",weight=ft.FontWeight.W_500),),
                                            ft.Container(padding= 5,alignment=ft.alignment.center,width=(general_width-60),bgcolor="white", content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_AROUND,vertical_alignment=ft.CrossAxisAlignment.CENTER,controls=[ft.Text(f'{x[2]}',color="black",font_family="arial",weight=ft.FontWeight.W_700), ft.Text(f'{x[1]}',color=ft.colors.TRANSPARENT, size=0), ft.Text(f'\t\t\t\t{"{:.3f}".format(x[4])} kWh',color="black", font_family="arial", weight=ft.FontWeight.W_700)],))]),
                                            ),
            )


def delete_room(e):

    #e.content.bgcolor = "red"
    #time.sleep(1)
    selected_room_id = e.control.content.controls[0].value
    #room_id = particular_room_data_table.controls[0].value
    data_base.delete_room(selected_room_id)

    #get_all_elements_consumtion()
    #show_elements()
    #get_all_rooms_consumtion()
    show_rooms(lambda e: e.page.update())
    #get_all_elements_consumtion()
    get_all_rooms_consumtion()
    compare_exp_and_current_consumtion()
    #show_rooms(lambda e: e.page.update())

    general_data_table.update()
    general_rooms_table.update()
    data_table.update()

    delete_room_apears()

    
    #compare_exp_and_current_consumtion()

    #particular_room_data_table.controls[3].value = f"\t\t\t{data_base.get_particular_room_consumtion(room_id)}"

    ##particular_elements_table.update()
    #general_data_table.update(
    #particular_room_data_table.update()
    #delete_apears()

    print(f"room {selected_room_id} has been deleted")

delete_room_display = ft.Container(width=general_width,
                                height=80,
                                margin=0,
                                padding=8,
                                visible=False,
                                bgcolor=ft.colors.BLUE_400,
                                shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
                                        color=ft.colors.GREY_900,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                    ),
                                    border_radius=16,
                                    content= ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[ft.Icon(ft.icons.DELETE, size=40, color="white"),ft.Text("Se ha eliminado una habitación.", text_align=ft.TextAlign.CENTER ,size=14, color="white")])
                                )
def delete_room_apears():
    delete_room_display.visible = True
    delete_room_display.update()
    time.sleep(3)
    delete_room_display.visible = False
    delete_room_display.update()


def delete_element(e):

    #e.content.bgcolor = "red"
    #time.sleep(1)
    element_id = e.control.content.controls[1].content.controls[1].value
    room_id = particular_room_data_table.controls[0].value
    data_base.delete_element(element_id)

    get_all_elements_consumtion()
    show_elements()
    get_all_rooms_consumtion()
    show_rooms(lambda e: e.page.update())
    get_all_elements_consumtion()
    get_all_rooms_consumtion()
    compare_exp_and_current_consumtion()
    
    #compare_exp_and_current_consumtion()

    particular_room_data_table.controls[3].value = f"\t\t\t{data_base.get_particular_room_consumtion(room_id)}"

    particular_elements_table.update()
    #data_table.update()
    #general_data_table.update(
    particular_room_data_table.update()
    delete_apears()

    print(f"Element {element_id} has been deleted")

delete_element_display = ft.Container(width=general_width,
                                height=80,
                                margin=0,
                                padding=8,
                                visible=False,
                                bgcolor=ft.colors.BLUE_400,
                                shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
                                        color=ft.colors.GREY_900,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                    ),
                                    border_radius=16,
                                    content= ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[ft.Icon(ft.icons.DELETE, size=40, color="white"),ft.Text("Se ha eliminado un elemento de consumo.", text_align=ft.TextAlign.CENTER ,size=14, color="white")])
                                )
def delete_apears():
    delete_element_display.visible = True
    delete_element_display.update()
    time.sleep(3)
    delete_element_display.visible = False
    delete_element_display.update()

delete_profile_display = ft.Container(width=general_width,
                                height=80,
                                margin=0,
                                padding=8,
                                visible=False,
                                bgcolor=ft.colors.BLUE_400,
                                shadow=ft.BoxShadow(
                                        spread_radius=.1,
                                        blur_radius=5,
                                        color=ft.colors.GREY_900,
                                        offset=ft.Offset(0, 0),
                                        blur_style=ft.ShadowBlurStyle.NORMAL,
                                    ),
                                    border_radius=16,
                                    content= ft.Column(alignment=ft.MainAxisAlignment.CENTER,horizontal_alignment=ft.CrossAxisAlignment.CENTER,controls=[ft.Icon(ft.icons.DELETE, size=40, color="white"),ft.Text("Se ha eliminado el perfil con éxito.", text_align=ft.TextAlign.CENTER ,size=14, color="white")])
                                )

def delete_profile_apears():
    delete_profile_display.visible = True
    delete_profile_display.update()
    time.sleep(3)
    delete_profile_display.visible = False
    delete_profile_display.update()

def get_all_elements_consumtion():
        new_paricular_room_consumtion = 0
        room_id = particular_room_data_table.controls[0].value

        for x in data_base.get_elements(room_id):
            new_paricular_room_consumtion += x[4]
            print(new_paricular_room_consumtion)

        particular_room_data_table.controls[3].controls[0].value = f'{"{:.3f}".format(new_paricular_room_consumtion)}'
        data_base.update_particular_consumition(new_paricular_room_consumtion, room_id)


def generate_new_settings_button():
    id = general_data_table.controls[0].value
    name_to_settings = general_data_table.controls[4].value
    exp_consumition_db_value = data_base.get_consumtion_esp(id)

    def display_settings():
        settings_title_table.content.controls[1].value = name_to_settings
        exp_consumition_field.value = exp_consumition_db_value

    general_data_table.controls[1].controls.pop(0)
    general_data_table.controls[1].controls.insert(0,ft.Container(gradient= ft.LinearGradient(begin=ft.alignment.top_center,end=ft.alignment.bottom_center, colors= bg_e_grey_gradients), border_radius=100, padding=6, height=38, width=38, on_click= lambda e: (display_settings(), e.page.go("/settings"), e.page.update()),content=ft.Image(src="assets/logos/Engranaje_icon.png", height=15,width=15, color=ft.colors.GREY_800)))

def EditARoom(e):
    if edit_form.height != 375:
        edit_form.height = 375
        edit_form.width = general_width
        edit_form.opacity = 1

        dinamic_tips_bar.visible = False
        dinamic_tips_bar.update()

        edit_form.disabled=False
        footer.visible=False
        edit_form.update()

def CancelEditARoom(e):
    if edit_form.height != 0:
        edit_form.height = 0
        edit_form.width = 0
        edit_form.opacity = 1

        dinamic_tips_bar.visible = True
        dinamic_tips_bar.update()

        edit_form.disabled=True
        footer.visible=True
        edit_form.update()

def CloseTheEditForm(e):
    if edit_form.height != 0:
        edit_form.height = 0
        edit_form.width = 0
        edit_form.opacity = 1
        edit_form.disabled=True
        footer.visible=True

edit_name = ft.TextField(label="Nombre", label_style= ft.TextStyle(color=ft.colors.GREY_900, weight= ft.FontWeight.W_500), height=75, border_color=ft.colors.RED_50, max_length=10, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200)
edit_type = ft.Dropdown(label="Tipo", label_style= ft.TextStyle(color=ft.colors.GREY_900, weight= ft.FontWeight.W_500), height=75, color=ft.colors.GREY_900, bgcolor= ft.colors.GREY_200 ,options=[ft.dropdown.Option("Casa"),ft.dropdown.Option("Edificio"),ft.dropdown.Option("Nave"),ft.dropdown.Option("Otro")])

edit_form = ft.Container(
                                width=0,
                                height=0,
                                bgcolor="#3fe39f",
                                border_radius=30,
                                opacity=1,
                                margin=ft.margin.only(top=-10,bottom=-10),
                                animate=ft.animation.Animation(400, "decelerate"),
                                animate_opacity=200,
                                padding= ft.padding.only(top=45, bottom=45, left=25,right=25),
                                content=ft.Column(
                                horizontal_alignment= ft.CrossAxisAlignment.CENTER, 
                                alignment= ft.MainAxisAlignment.CENTER,
                                    controls=
                                    [
                                        ft.Text("Editar perfil", size=20,text_align= ft.TextAlign.CENTER, color=ft.colors.WHITE, weight=ft.FontWeight.W_700),
                                        edit_name,
                                        edit_type,
                                        ft.Container(
                                            content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_EVENLY,vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                                controls=[
                                                    ft.TextButton("Guardar", ft.icons.SAVE, height=40, icon_color="#3fe39f", on_click=(lambda e: (e.page.update())), style= ft.ButtonStyle(bgcolor= ft.colors.WHITE, color="#3fe39f", shape=ft.RoundedRectangleBorder(radius=10))),
                                                    ft.TextButton("Cancelar", ft.icons.CANCEL, height=40, icon_color=ft.colors.WHITE, on_click=lambda e: (CancelEditARoom(e), edit_form.update), style= ft.ButtonStyle(bgcolor=ft.colors.RED_400, color=ft.colors.WHITE, shape=ft.RoundedRectangleBorder(radius=10)))
                                                ]
                                            ),
                                        ),
                                    ]
                                ),
                            )

dinamic_tips_bar = ft.Container(on_click=lambda e: e.page.go("/tips"), width=(general_width-80), bgcolor=ft.colors.GREY_800, border_radius=18, padding=10,content=ft.Row(alignment=ft.MainAxisAlignment.SPACE_EVENLY, vertical_alignment=ft.CrossAxisAlignment.CENTER, controls=[ft.Image(src="assets/logos/LampIcon.png", width=30, color="white"), ft.Text(value=f'{"Consejos para un consumo eficiente."}', font_family="arial", text_align=ft.TextAlign.START, size=12.5, color=ft.colors.WHITE)]))

#-----------------------INDEX VIEW


def delete_profile(e):
    id = general_data_table.controls[0].value 
    data_base.delete_profile(id)
    #profile_table.rows.pop(0)


#-----------------------VIEW TEMPLATE

def view_template(view):
    return ft.Container(    width=1500,
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
                                    content= view
                                )
                            ]),                 
                        )