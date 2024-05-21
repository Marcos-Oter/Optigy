from flet import View, Text, ElevatedButton, colors, AppBar
def _view_():
    return View("/tips", bgcolor=colors.GREY_400,
                controls=[
                    AppBar(title=Text("Tips"), bgcolor=colors.SURFACE_VARIANT),
                    ElevatedButton("Go Home", on_click=lambda e: e.page.go("/index")),
                ]
            )