from flet import View, Text, ElevatedButton, colors, AppBar

def _view_():
    return View("/general", bgcolor=colors.GREY_400,
                controls=[
                    AppBar(title=Text("Profile"), bgcolor=colors.SURFACE_VARIANT),
                    ElevatedButton("Go Home", on_click=lambda e: e.page.go("/index")),
                ]
            )