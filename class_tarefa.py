import flet as ft


class Campo_tarefa(ft.Row):
    def __init__(self,texto_tarefa):
        super().__init__()
        self.caixa_texto = ft.TextField(value=texto_tarefa,
                                        label="Tarefas",
                                        filled=True,
                                        bgcolor="#cc9966",
                                        border_color="#604020",
                                        border_radius=15,
                                        width=500
                                        )
        self.texto=ft.Text(value="Concluido ✔📝")
        self.coluna2=ft.Column(controls=[self.texto,self.caixa_texto])

        self.caixa_selecao= ft.Checkbox(on_change=self.alterar_cor)

        self.botao1= ft.FloatingActionButton(icon=ft.Icons.DELETE_FOREVER,bgcolor="#6D5542"
                                             )
        self.botao2= ft.FloatingActionButton(icon=ft.Icons.CREATE_OUTLINED,bgcolor="#6D5542")

        coluna_botoes=ft.Column(controls=[self.botao1,self.botao2])
        linha = ft.Row(controls=[self.caixa_selecao,self.coluna2,coluna_botoes])

        self.container_botao= ft.Container(content= linha, bgcolor="#cc9966",border=ft.Border.all(width=1,
                                                                                                   color="#00000000"),
        border_radius= 10,padding=5,animate=True)
  
        
        self.controls=[self.container_botao]
     



    def alterar_cor(self):
        if self.caixa_selecao.value == True:
            self.container_botao.bgcolor ="#9b754f"
        else:
            self.container_botao.bgcolor="#cc9966"

        


