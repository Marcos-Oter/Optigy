import flet as ft
from __module__ import bg_grey_gradients,bg_white_gradients,back_button, general_width, bg2_grey_gradients, profiles_containers_height, view_template

class tips(ft.UserControl):
    def __init__(self):
        super().__init__(expand=True)

        self.table =  ft.Container(
                        width=(general_width - 80),
                        border_radius=5,
                        height= (profiles_containers_height),
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
                            disabled=False,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            controls=[
                                    ft.Image(src="assets/images/Tips01.png", width=155),
                            ]
                        )                                        
        )

        self.tips_table =  ft.Container(
                        width=(general_width - 80),
                        border_radius=5,
                        height= (profiles_containers_height + 150),
                        content=ft.Column(
                            expand = True,
                            scroll = ft.ScrollMode.ALWAYS,
                            width=(general_width - 100),
                            height=float("inf"),
                            disabled=False,
                            alignment=ft.MainAxisAlignment.CENTER,
                            horizontal_alignment=ft.CrossAxisAlignment.START,
                            spacing=20,
                            controls=[
                                    ft.Text("Aislamiento térmico", color=ft.colors.GREEN_700,size=17, weight=ft.FontWeight.W_700),
                                    ft.Text("·Asegúrate de que tu casa esté bien aislada. Esto reduce la pérdida de calor en invierno y mantiene el calor afuera en verano, reduciendo la necesidad de calefacción y aire acondicionado.\n\n·Sella grietas y huecos en puertas y ventanas para evitar fugas de aire.", color=ft.colors.GREY_700,size=14, weight=ft.FontWeight.W_700),

                                    ft.Text("Electrodomésticos eficientes", color=ft.colors.GREEN_700,size=17, weight=ft.FontWeight.W_700),
                                    ft.Text("·Elige electrodomésticos con calificación energética alta (A+++, A++, A+) para reducir el consumo de energía.\n\n·Desenchufa los electrodomésticos cuando no estén en uso o utiliza regletas con interruptores para apagar varios dispositivos a la vez.", color=ft.colors.GREY_700,size=14, weight=ft.FontWeight.W_700),

                                    ft.Text("Iluminación eficiente", color=ft.colors.GREEN_700,size=17, weight=ft.FontWeight.W_700),
                                    ft.Text("·Utiliza bombillas LED, que consumen menos energía y duran más que las bombillas incandescentes o fluorescentes.\n\n·Aprovecha al máximo la luz natural durante el día abriendo cortinas y persianas.", color=ft.colors.GREY_700,size=14, weight=ft.FontWeight.W_700),

                                    ft.Text("Termostato inteligente", color=ft.colors.GREEN_700,size=17, weight=ft.FontWeight.W_700),
                                    ft.Text("·Instala un termostato programable o inteligente para controlar la temperatura de tu casa según tu horario y preferencias, reduciendo el uso innecesario de calefacción y aire acondicionado.", color=ft.colors.GREY_700,size=14, weight=ft.FontWeight.W_700),
                                    
                                    ft.Text("Aire acondicionado y calefacción", color=ft.colors.GREEN_700,size=17, weight=ft.FontWeight.W_700),
                                    ft.Text("·Mantén los filtros de aire limpios y revisa regularmente el sistema para asegurarte de que esté funcionando de manera eficiente.\n\n·Ajusta la temperatura del termostato a niveles cómodos pero moderados para evitar un consumo excesivo de energía.", color=ft.colors.GREY_700,size=14, weight=ft.FontWeight.W_700),

                                    ft.Text("Energías renovables", color=ft.colors.GREEN_700,size=17, weight=ft.FontWeight.W_700),
                                    ft.Text("·Considera la instalación de paneles solares para generar tu propia electricidad y reducir la dependencia de la red eléctrica convencional.\n\n·Instala calentadores de agua solares para aprovechar la energía solar para el agua caliente.", color=ft.colors.GREY_700,size=14, weight=ft.FontWeight.W_700),
                                    
                                    ft.Text("Uso responsable de agua caliente", color=ft.colors.GREEN_700,size=17, weight=ft.FontWeight.W_700),
                                    ft.Text("·Reduce la temperatura del calentador de agua a 120°F (49°C) para ahorrar energía.\n\n·Repara los grifos que gotean y considera la instalación de cabezales de ducha y grifos de bajo flujo para reducir el consumo de agua caliente.", color=ft.colors.GREY_700,size=14, weight=ft.FontWeight.W_700),

                                    ft.Text("Aprovechamiento de la ventilación natural", color=ft.colors.GREEN_700,size=17, weight=ft.FontWeight.W_700),
                                    ft.Text("·Abre ventanas y puertas en días frescos para permitir la circulación de aire y reducir la necesidad de utilizar ventiladores o aire acondicionado.", color=ft.colors.GREY_700,size=14, weight=ft.FontWeight.W_700),

                                    ft.Text("Electrodomésticos y hábitos diarios", color=ft.colors.GREEN_700,size=17, weight=ft.FontWeight.W_700),
                                    ft.Text("·Utiliza la lavadora y el lavavajillas con cargas completas para maximizar su eficiencia.\n\n·Seca la ropa al aire libre en lugar de usar la secadora siempre que sea posible.", color=ft.colors.GREY_700,size=14, weight=ft.FontWeight.W_700),

                                    ft.Text("Apagado de dispositivos electrónicos", color=ft.colors.GREEN_700,size=17, weight=ft.FontWeight.W_700),
                                    ft.Text("·Apaga las luces y los dispositivos electrónicos cuando no estén en uso.\n\n·Desenchufa cargadores y otros dispositivos cuando no los estés utilizando, ya que continúan consumiendo energía incluso en modo de espera.", color=ft.colors.GREY_700,size=14, weight=ft.FontWeight.W_700),

                                    ft.Text("Jardinería y paisajismo", color=ft.colors.GREEN_700,size=17, weight=ft.FontWeight.W_700),
                                    ft.Text("·Planta árboles y arbustos alrededor de tu casa para proporcionar sombra y reducir la necesidad de aire acondicionado en verano.\n\n·Utiliza plantas que requieran menos agua en tu jardín para reducir la necesidad de riego.", color=ft.colors.GREY_700,size=14, weight=ft.FontWeight.W_700),
                                    
                                    ft.Text("Concientización y educación", color=ft.colors.GREEN_700,size=17, weight=ft.FontWeight.W_700),
                                    ft.Text("·Educa a todos los miembros de tu hogar sobre la importancia del ahorro energético y la adopción de prácticas sostenibles.\n\n·Realiza auditorías energéticas periódicas para identificar áreas de mejora y seguir optimizando el consumo de energía en tu hogar.", color=ft.colors.GREY_700,size=14, weight=ft.FontWeight.W_700),
                            ]
                        )                                        
        )

        self.footer = ft.Text("Optigy® Todos los derechos reservados", text_align= ft.TextAlign.CENTER, font_family="arial", size=12, weight=ft.FontWeight.W_700, color=ft.colors.GREY_900)

        self.content = ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment= ft.CrossAxisAlignment.CENTER,
            spacing=25,
            scroll="auto",
            controls=[
                back_button("/general",(lambda e: e.page.update())),
                self.table,
                self.tips_table,
                self.footer,
            ]
        )
    
    def build(self):
         return self.content

def _view_():
        return ft.View("/tips", bgcolor=ft.colors.GREY_200,
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
                                    content= tips()
                                )
                            ]),                 
                        )
                    ]       
                )