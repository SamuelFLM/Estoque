import PySimpleGUI as sg

bg_color = "#FFFFFF"
text_color = "#414141"
sg.theme_background_color(bg_color)

cabecalho = [
    sg.Image(
        filename="Image//cabecalho.png",
        pad=(0, (0, 0)),
        background_color=bg_color,
        expand_x=True,
    )
]

buscar_produto = [
    [
        sg.Text(
            "Buscar Produto",
            font="Inter 20",
            text_color=text_color,
            background_color=bg_color,
            expand_x=True,
            justification="center",
            pad=(0, (50, 20)),
        )
    ],
    [
        sg.Text("", background_color=bg_color, pad=(120, (0, 0))),
        sg.Input(
            "a", size=(50, 50), pad=(0, (0, 0)), justification="center", font="Inter 13"
        ),
        sg.Image(
            filename="Image//procurar.png", pad=(0, (0, 0)), background_color=bg_color
        ),
    ],
    [
        sg.Text("", background_color=bg_color, pad=(120, (0, 0))),
        sg.HSep(pad=(0, (0, 0))),
        sg.Text("", background_color=bg_color, pad=(120, (0, 0))),
    ],
]

produtos = []

rodape = []

layout = [cabecalho, buscar_produto, produtos, rodape]

window = sg.Window("Mercadorias", layout=layout, size=(979, 724), margins=(0, 0))

while True:
    event, values = window.read(timeout=1)

    if event == sg.WIN_CLOSED:
        break
