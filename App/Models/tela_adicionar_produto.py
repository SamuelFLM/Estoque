import PySimpleGUI as sg
import pyautogui as bot
import webbrowser
import re
from datetime import datetime


def validar_preco(preco):
    # A expressão regular abaixo corresponde a números inteiros e de ponto flutuante
    regex = r"^-?\d+(\.\d+)?$"
    if re.match(regex, preco):
        return True
    else:
        return False


def validar_validade_produto(data):
    # A expressão regular abaixo corresponde ao formato de data 'yyyy-MM-dd'
    regex = r"^\d{4}-\d{2}-\d{2}$"
    if re.match(regex, data):
        return True
    else:
        return False


data = datetime.now()

def TelaAdicionarProduto(api):
    bg_color = "#FFFFFF"
    text_color = "#414141"

    sg.theme_background_color(bg_color)
    cabecalho = [
        sg.Image(
            filename="Image//logo_2.png",
            background_color=bg_color,
            pad=(0, (0, 30)),
            enable_events=True,
            k="ajudar",
        )
    ]

    ajudar = [
        sg.Text("", background_color=bg_color, pad=(130, (0, 0))),
        sg.Image(
            filename="Image//ajudar.png",
            background_color=bg_color,
            pad=(0, (0, 0)),
            enable_events=True,
            k="btn_ajudar",
        ),
    ]

    titulo = [
        sg.Text("", background_color=bg_color, pad=(32, (0, 0))),
        sg.Text(
            "Adicionar Produto",
            expand_x=True,
            background_color=bg_color,
            text_color=text_color,
            font="Inter 18",
            pad=(0, (30, 20)),
        ),
    ]

    produto = [
        [
            sg.Text(
                "Produto",
                background_color=bg_color,
                pad=(15, (30, 10)),
                font="Inter 12 bold",
                text_color=text_color,
                key="title_produto",
            )
        ],
        [
            sg.Input(
                "",
                size=(40, 10),
                pad=(20, (0, 0)),
                justification="center",
                font="Inter 12",
                border_width=0,
                background_color=bg_color,
                key="ipt_produto",
            ),
        ],
        [sg.HSep(pad=(20, (0, 0)))],
    ]

    marca = [
        [
            sg.Text(
                "Marca",
                background_color=bg_color,
                pad=(15, (30, 10)),
                font="Inter 12 bold",
                text_color=text_color,
                key="title_marca",
            )
        ],
        [
            sg.Input(
                "",
                size=(40, 10),
                pad=(20, (0, 0)),
                justification="center",
                font="Inter 12",
                border_width=0,
                background_color=bg_color,
                key="ipt_marca",
            ),
        ],
        [sg.HSep(pad=(20, (0, 0)))],
    ]

    preco = [
        [
            sg.Text(
                text="Preço",
                background_color=bg_color,
                pad=(15, (30, 10)),
                font="Inter 12 bold",
                text_color=text_color,
                key="title_preco",
            )
        ],
        [
            sg.Input(
                "",
                size=(40, 10),
                pad=(20, (0, 0)),
                justification="center",
                font="Inter 12",
                border_width=0,
                background_color=bg_color,
                key="ipt_preco",
            ),
        ],
        [sg.HSep(pad=(20, (0, 0)))],
    ]

    validade = [
        [
            sg.Text(
                "Validade",
                background_color=bg_color,
                pad=(15, (30, 10)),
                font="Inter 12 bold",
                text_color=text_color,
                key="title_validade",
            )
        ],
        [
            sg.Input(
                str(data.strftime("%Y-%m-%d")).strip(),
                size=(40, 10),
                pad=(20, (0, 0)),
                justification="center",
                font="Inter 12",
                border_width=0,
                background_color=bg_color,
                key="ipt_validade",
            ),
        ],
        [sg.HSep(pad=(20, (0, 0)))],
    ]

    rodape = [
        sg.Image(
            filename="Image//btn_adicionar_2telaoff.png",
            background_color=bg_color,
            pad=(55, (40, 0)),
            enable_events=True,
            key="btn_adicionar",
        )
    ]

    layout = [cabecalho, ajudar, titulo, produto, marca, preco, validade, rodape]

    window = sg.Window(
        "Produtos", layout=layout, size=(322, 723), margins=(0, 0), finalize=True
    )

    while True:
        event, values = window.read(timeout=1)

        if event == sg.WIN_CLOSED:
            break

        produto = str(values["ipt_produto"]).strip()
        marca = str(values["ipt_marca"]).strip()
        preco = str(values["ipt_preco"]).strip()
        validade = str(values["ipt_validade"]).strip()

        if event == "btn_ajudar":
            webbrowser.open_new_tab("https://github.com/SamuelFLM/Estoque")
            
        if bool(produto) and bool(marca) and bool(preco) and bool(validade):
            if len(produto) <= 30 and len(marca) <= 20:
                validar = validar_preco(preco)
                if validar:
                    window["title_preco"].update("Preço")
                    validar_data = validar_validade_produto(validade)
                    if validar_data:
                        if (int(validade[5:7]) > 00 and int(validade[8:10]) > 00):
                            window["btn_adicionar"].update(
                                filename="Image//btn_adicionar_2tela.png"
                            )
                            if event == "btn_adicionar":
                                produto = {
                                    "nome": produto,
                                    "marca": marca,
                                    "preco": preco,
                                    "validadeProduto": validade,
                                }
                                api.post(produto)
                                bot.confirm(
                                    title="SUCESSO",
                                    text="PRODUTO CADASTRADO COM SUCESSO!",
                                    buttons=["OK"],
                                )
                                window.close()
        else:
            window["btn_adicionar"].update(filename="Image//btn_adicionar_2telaoff.png")

    window.Close()
