import PySimpleGUI as sg
from Models.produto import Produto


class TelaEstoque:
    def __init__(self) -> None:
        self.bg_color = "#FFFFFF"
        self.text_color = "#414141"
        sg.theme_background_color(self.bg_color)
        # self.produtos = [["1", "Doritos", "Elma Chips", 15.00, "07-10-2023", "07-10-2023"]]
        self.response = list(Produto().get())
        self.produtos = []
        for i, valor in enumerate(self.response):
            self.produtos.append(
                [
                    self.response[i]["id"],
                    self.response[i]["nome"],
                    self.response[i]["marca"],
                    self.response[i]["preco"],
                    self.response[i]["dataCadastro"][:10],
                    self.response[i]["validadeProduto"][:10],
                ]
            )

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
                    sg.Text("", background_color=self.bg_color, pad=(155, (0, 0))),
                    sg.Input(
                        "",
                        size=(30, 30),
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
                    values=self.produtos,
                    headings=[
                        "Id",
                        "Produto",
                        "Marca",
                        "Preço",
                        "Validade",
                        "Data Cadastro",
                    ],
                    bind_return_key=True,
                    auto_size_columns=True,
                    background_color="white",
                    expand_x=True,
                    border_width=0,
                    justification="c",
                    font="Jaldi 11 bold",
                    text_color="#6D6D6D",
                    header_border_width=0,
                    header_background_color="white",
                    k="table",
                    display_row_numbers=True,
                    sbar_background_color="white",
                    sbar_width=0,
                    sbar_arrow_width=0,
                    size=(10,15),
                    pad=(20, (10, 30)),
                )
            ],
            [sg.HSep(pad=(20, (0, 40)))],
        ]

        rodape = [
            sg.Text("", background_color=self.bg_color, pad=(80, (0, 0))),
            sg.Image(
                filename="Image//adicionaron.png",
                background_color=self.bg_color,
                pad=(20, (0, 0)),
                enable_events=True,
                key="btn_adicionar",
            ),
            sg.Image(
                filename="Image//lixeiraon.png",
                background_color=self.bg_color,
                pad=(70, (0, 0)),
                enable_events=True,
                key="btn_deletar",
            ),
            sg.Image(
                filename="Image//carregar.png",
                background_color=self.bg_color,
                pad=(70, (0, 0)),
                enable_events=True,
                key="btn_carregar",
            ),
            sg.Image(
                filename="Image//editaron.png",
                background_color=self.bg_color,
                pad=(60, (0, 0)),
                enable_events=True,
                key="btn_editar",
            ),
            sg.Image(
                filename="Image//downloadon.png",
                background_color=self.bg_color,
                pad=(40, (0, 0)),
                enable_events=True,
                key="btn_download",
            ),
        ]

        layout = [cabecalho, buscar_produto, produtos, rodape]

        window = sg.Window(
            "Produtos", layout=layout, size=(979, 724), margins=(0, 0), finalize=True
        )

        return self.produtos, window
