import PySimpleGUI as sg
from Models.tela_estoque import TelaEstoque
from Models.produto import Produto

def atualizarProdutos():
    response = list(Produto().get())
    lista = []
    for i, valor in enumerate(response):
        lista.append(
            [
                response[i]["id"],
                response[i]["nome"],
                response[i]["marca"],
                response[i]["preco"],
                response[i]["dataCadastro"][:10],
                response[i]["validadeProduto"][:10],
            ]
        )
    return lista


API = Produto()
produtos, window = TelaEstoque().front()


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event == "btn_carregar":
        novos_produtos = atualizarProdutos()
        window["table"].update(values=novos_produtos)

window.Close()



