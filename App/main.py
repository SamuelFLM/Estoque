import PySimpleGUI as sg
from Models.tela_estoque import TelaEstoque

window = TelaEstoque().front()


while True:
    event, values = window.read(timeout=1)

    if event == sg.WIN_CLOSED:
        break