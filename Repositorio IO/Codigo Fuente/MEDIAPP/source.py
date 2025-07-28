import flet as ft

conteiner = ft.Container(
    ft.Column([
        ft.Container(
    content=ft.Image(
        src="logo.jpg",
        width=100,
        height=100,
        fit=ft.ImageFit.CONTAIN
    ),
    width=100,
    height=100,
    border_radius=10,  
    clip_behavior=ft.ClipBehavior.HARD_EDGE,
    alignment=ft.alignment.center,
    padding=ft.padding.only(top=20)
),


        ft.Container(
            ft.Text(
                "MEDIAPP",
                width=320,
                size=30,
                text_align="center",
                weight="w900"
            ),
            padding= ft.padding.only(20,20)
        ),
        ft.Container(
            ft.TextField(
                width=280,
                height=40,
                hint_text="Usuario",
                border="underline",
                color="black",
                prefix_icon= ft.Icons.LOGIN
            ),
            padding= ft.padding.only(20,20)
        ),
        ft.Container(
            ft.TextField(
                width=280,
                height=40,
                hint_text="Contraseña",
                border="underline",
                color="black",
                prefix_icon= ft.Icons.LOCK,
                password= True
            ),
            padding= ft.padding.only(20,20)
        ),

        ft.Container(
            ft.Checkbox(
                label= "Olvidaste tu contraseña",
                check_color="black",
            ),
            padding= ft.padding.only(80)
        ),
        ft.Container(
            ft.ElevatedButton(
                text= "Iniciar Sesión",
                width= 280,
                bgcolor= "black"
            ),
            padding= ft.padding.only(20,20)
        ),
        ft.Text("Iniciar sesión con",
                text_align= "center",
                width=320),

        ft.Container(
            ft.Row([
                ft.IconButton(
                    icon= ft.Icons.EMAIL,
                    tooltip="Gmail",
                    icon_size=35
                ),
                ft.IconButton(
                    icon= ft.Icons.APPLE,
                    tooltip="Apple ID",
                    icon_size=35
                ),
                ft.IconButton(
                    icon= ft.Icons.FACEBOOK,
                    tooltip="Facebook",
                    icon_size=35
                ),
            ],
            alignment= ft.MainAxisAlignment.CENTER
            ),
            padding= ft.padding.only(20,20)
        ),
        
        ft.Container(
            ft.Row([
                ft.Text("¿No esta registrado?"),
                ft.TextButton("Registrarse")
            ],
            alignment= ft.MainAxisAlignment.CENTER
            )
        )

    ],
    alignment= ft.MainAxisAlignment.SPACE_EVENLY
    ),
    border_radius= 20,
    width= 320,
    height= 650,
    gradient= ft.LinearGradient([
        ft.Colors.BLUE_500,
        ft.Colors.BLUE_700,
        ft.Colors.BLUE_400
    ]
    
    )

    )

    

def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLACK
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.add(conteiner)


ft.app(target=main)
