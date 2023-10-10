import PySimpleGUI as sg
from Models.tela_estoque import TelaEstoque
from utils import *
from Models.tela_adicionar_produto import *
from Models.tela_editar_produto import *

API = Produto()


def edit_produto(item):
    TelaEditarProduto(API, item)
    main()

def add_produto():
    TelaAdicionarProduto(API)
    main()

def main():
    produtos, window = TelaEstoque().front()
    
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        
        novos_produtos = atualizarProdutos()
        window["table"].update(values=novos_produtos)    
        
        if event == "btn_pesquisar":
            if (values["pesquisar"] != ""):
                novo_produto = Produto().get_by_product()
                window["table"].update(values=novo_produto)
            else:
                novos_produtos = atualizarProdutos()
                window["table"].update(values=novos_produtos)
            
        if event == "btn_carregar":
            novos_produtos = atualizarProdutos()
            window["table"].update(values=novos_produtos)

        if event == "btn_adicionar":
            window.close()
            add_produto()
            break
     

        if event == "btn_deletar":
            try:
                item = produtos[values["table"][0]]
            except: continue
            Produto().delete(item[0])

        if event == "btn_editar":
            try:
                item = produtos[values["table"][0]]
            except: continue
            window.close()
            edit_produto(item)
            break
main()