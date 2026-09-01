import flet as ft
from class_tarefa import Campo_tarefa

def main(pg:ft.Page):
    pg.title= " Godo Tarefas"
    pg.horizontal_alignment="CENTER"
    pg.bgcolor = "#cc9966"
    pg.window.width= 1000
    pg.window.height = 800


    lista_campos_tarefas = []

    def adicionar_campo_tarefa():
        novo_campo= Campo_tarefa(texto_tarefa=lista_campos_tarefas.value)
        lista_campos_tarefas.append(Campo_tarefa())






   

    texto_hello = ft.Text(value= "Godo Tarefas 🐹",
                       color="#604020",
                       size=35,
                       italic=True)




    botao_adiconar= ft.FloatingActionButton(icon=ft.Icons.ADD_CIRCLE_OUTLINE,
                                                   bgcolor="#6D5542",on_click=adicionar_campo_tarefa)

    
    campo_tarefa= ft.TextField(label="Digite aqui a sua tarefa",
                               color="#4A2E1B",
                               text_align="Center",
                               bgcolor="#CC9966",
                               border_radius=20,
                               border_color= "#4A2E1B"
                               
                               )
    linha_botoes= ft.Row(controls=[campo_tarefa,botao_adiconar],alignment="Center")
    


    coluna=ft.Column(controls=lista_campos_tarefas)


    container_resultado = ft.Container(content=coluna,
                                       bgcolor="#CC9966",
                                       padding=30,
                                       border_radius=20,
                                       width=800,
                                       border=ft.Border.all(2, color="#5C4434"),on_click=adicionar_campo_tarefa)
   
    
    
   
   
















    pg.add(texto_hello)
    pg.add(linha_botoes)
    pg.add(container_resultado)
    
    
ft.run(main)
