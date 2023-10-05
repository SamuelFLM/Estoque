import requests, json


class Produto:
    def __init__(self) -> None:
        self.url = "http://localhost:5208/v1/produto"
        self.headers = {"Content-Type": "application/json"}

    def get(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            print(f"Erro na requisição: {err}")
            return None

    def get_by_id(self, id):
        try:
            response = requests.get(f"{self.url}/{id}")
            response.raise_for_starus()
            return response.json()
        except requests.exceptions.RequestException as err:
            print(f"Erro na requisição: {err}")
            return None

    def get_by_product(self, product):
        try:
            response = requests.get(f"{self.url}/GetByProduct/{product}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            print(f"Erro na requisição: {err}")
            return None

    def post(self, produto):
        try:
            response = requests.post(
                f"{self.url}", data=json.dumps(produto), headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            print(f"Erro na requisição: {err}")
            return None

    def put(self, id, produto):
        try:
            response = requests.put(
                f"{self.url}/{id}", data=json.dumps(produto), headers=self.headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            print(f"Erro na requisição: {err}")
            return None

    def delete(self, id):
        try:
            response = requests.delete(f"{self.url}/{id}")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as err:
            print(f"Erro na requisição: {err}")
            return None


if __name__ == "__main__":
    produto = {
        "nome": "Nome do Produto",
        "marca": "Marca do Produto",
        "preco": 19.99,
        "validadeProduto": "2023-12-31T23:59:59Z",
    }
    api = Produto()
    
    response = list(api.get())
    
    lista = []
    
    for i, valor in enumerate(response):
        print(i, valor)
        lista.append(
            [
                response[i]["id"],
                response[i]["nome"],
                response[i]["marca"],
                response[i]["preco"],
                response[i]["dataCadastro"][:10],
                response[i]["validadeProduto"],
            ]
        )
        
    for i in lista:
        print(i)
