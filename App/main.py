import PySimpleGUI as sg
from Models.tela_estoque import TelaEstoque
from utils import *
from Models.tela_adicionar_produto import *

API = Produto()
produtos, window = TelaEstoque().front()


while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
   
    if event == "btn_carregar":
        novos_produtos =  atualizarProdutos()
        window["table"].update(values=novos_produtos)

    if event == "btn_adicionar":
        TelaAdicionarProduto(API)
        novos_produtos =  atualizarProdutos()
        window["table"].update(values=novos_produtos)
    
window.Close()



