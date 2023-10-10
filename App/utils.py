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

    