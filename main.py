import flet as ft 

result = ft.Text(value="0", color = ft.Colors.WHITE, size=20)

def main(page : ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.vertical_alignment = ft.CrossAxisAlignment.CENTER
    
    ## Функции калькулятора
    def cl_button(e):
        data = e.control.data 
        print(f"{data} is clicked")
        

    page.add(
        ft.Container(
            width = 350,
            height = 300,
            border_radius = ft.BorderRadius.all(20),     
            bgcolor = ft.Colors.BLACK,
            padding = 20,
            content = ft.Column(
                controls = [
                    ft.Row(controls = [result]),
                    ft.Row(
                        controls = [
                            ft.Button(content="A/C", bgcolor = ft.Colors.WHITE_54, data="AC", on_click=cl_button),
                            ft.Button(content="+/-", bgcolor = ft.Colors.WHITE_54),
                            ft.Button(content="%", bgcolor = ft.Colors.WHITE_54),
                            ft.Button(content="/", bgcolor = ft.Colors.ORANGE_600),
                        ]
                    ),

                    ft.Row(
                        controls = [
                            ft.Button(content="7", bgcolor = ft.Colors.WHITE_24),
                            ft.Button(content="8", bgcolor = ft.Colors.WHITE_24),
                            ft.Button(content="9", bgcolor = ft.Colors.WHITE_24),
                            ft.Button(content="*", bgcolor = ft.Colors.ORANGE_600)
                    
                        ]
                    ),

                    ft.Row(
                        controls = [
                            ft.Button(content="4", bgcolor = ft.Colors.WHITE_24),
                            ft.Button(content="5", bgcolor = ft.Colors.WHITE_24),
                            ft.Button(content="6", bgcolor = ft.Colors.WHITE_24),
                            ft.Button(content="-", bgcolor = ft.Colors.ORANGE_600)
                    
                        ]
                    ),

                    ft.Row(
                        controls = [
                            ft.Button(content="1", bgcolor = ft.Colors.WHITE_24),
                            ft.Button(content="2", bgcolor = ft.Colors.WHITE_24),
                            ft.Button(content="3", bgcolor = ft.Colors.WHITE_24),
                            ft.Button(content="+", bgcolor = ft.Colors.ORANGE_600)
                    
                        ]
                    ),

                    ft.Row(
                        controls = [
                            ft.Button(content="0", expand=2, bgcolor = ft.Colors.WHITE_24),
                            ft.Button(content=".", bgcolor = ft.Colors.WHITE_24),
                            ft.Button(content="=", bgcolor = ft.Colors.ORANGE_600)
                    
                        ]
                    ),

                ]
            )            
        )
    )

ft.run(main)