import PySimpleGUI as sg


class TelaEstoque:
    
    def __init__(self) -> None:
        self.bg_color = "#FFFFFF"
        self.text_color = "#414141"
        sg.theme_background_color(self.bg_color)
        self.lista = [["1", "Doritos", "Elma Chips", 15.00, "07-10-2023", "07-10-2023"]]
    
    def front(self):

        cabecalho = [
            sg.Image(
                filename="Image//cabecalho.png",
                pad=(0, (0, 0)),
                background_color=self.bg_color,
                expand_x=True,
            )
        ]

        buscar_produto = [
            [
                sg.Text(
                    "Buscar Produto",
                    font="Inter 20",
                    text_color=self.text_color,
                    background_color=self.bg_color,
                    expand_x=True,
                    justification="center",
                    pad=(0, (50, 20)),
                )
            ],
            [
                [
                    sg.Text("", background_color=self.bg_color, pad=(100, (0, 0))),
                    sg.Input(
                        "",
                        size=(50, 50),
                        pad=(0, (0, 0)),
                        justification="center",
                        font="Inter 14",
                        border_width=0.5,
                        background_color=self.bg_color,
                        key="pesquisar",
                        focus=True,
                    ),
                    sg.Image(
                        filename="Image//procurar.png",
                        pad=(20, (0, 0)),
                        background_color=self.bg_color,
                        enable_events=True,
                        key="btn_pesquisar",
                    ),
                ],
            ],
        ]

        produtos = [
            [sg.HSep(pad=(20, (30, 0)))],
            [
                sg.Table(
                    values=self.lista,
                    headings=["Id", "Produto", "Marca", "Preço", "Validade", "Data Cadastro"],
                    key="table",
                    bind_return_key=True,
                    auto_size_columns=True,
                    background_color="white",
                    expand_x=True,
                    border_width=0,
                    justification="c",
                    font="Jaldi 10 bold",
                    text_color="#6D6D6D",
                    header_border_width=0,
                    max_col_width=15,
                    header_background_color="white",
                    k="table",
                    display_row_numbers=True,
                    sbar_background_color="white",
                    sbar_width=0,
                    sbar_arrow_width=0,
                    pad=(20, (10, 50)),
                )
            ],
            [sg.HSep(pad=(20, (0, 40)))],
        ]

        rodape = [
            sg.Image(
                filename="Image//Deletar.png",
                background_color=self.bg_color,
                pad=(60, (0, 0)),
                enable_events=True,
                key="btn_deletar",
            ),
            sg.Image(
                filename="Image//adicionar.png",
                background_color=self.bg_color,
                pad=(20, (0, 0)),
                enable_events=True,
                key="btn_adicionar",
            ),
            sg.Image(
                filename="Image//Alterar.png",
                background_color=self.bg_color,
                pad=(40, (0, 0)),
                enable_events=True,
                key="btn_alterar",
            ),
        ]

        layout = [cabecalho, buscar_produto, produtos, rodape]

        window = sg.Window(
            "Mercadorias", layout=layout, size=(979, 724), margins=(0, 0), finalize=True
        )
        
        return window



    