# aquele link da api = endpoint
# endpoint é o link para os métodos get e post
# ex: https://api.open-meteo.com/v1/forecast

# sempre que eu uso api em python, devo chamar a biblioteca de requisições
# pip install requests
# pip install matplotlib

import requests
import matplotlib.pyplot as plt


# criar uma função chamada de buscar_clima
def buscar_clima(latitude, longitude):
    # deve informar o endpoint (api)
    endpoint = "https://api.open-meteo.com/v1/forecast"

    # informar os parametros para o sistema em formato de dicionario
    # -> o dicionario trabalha com chave:valor
    parametros = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "timezone": "America/Sao_Paulo"
    }

    resposta = requests.get(endpoint, params=parametros)

    # verificar se a requisição deu certo
    if resposta.status_code != 200:
        print("Erro ao acessar a API de clima")
        return None

    # o sistema transforma os dados em json para poder manipular eles
    dados = resposta.json()
    return dados


# pedir os dados para o usuário
latitude = float(input("Informe a latitude: "))
longitude = float(input("Informe a longitude: "))

# vamos começar a exibir informações para os usuários
dados = buscar_clima(latitude, longitude)

# verificar se os dados foram retornados corretamente
if dados is not None:
    horas = dados["hourly"]["time"]
    # chamo a base de dados, informo o parametro e qual a variavel o parametro vai ler
    temperatura = dados["hourly"]["temperature_2m"]
    
    plt.plot(horas, temperatura)

data_inicio = horas[0][:10]
data_fim = horas[-1][:10]

plt.title(f"Temperatura por hora — {data_inicio} a {data_fim}")

plt.xlabel("Hora")
plt.ylabel("Temperatura (°C)")

# deixar o gráfico mais organizado
plt.xticks(horas[::6], rotation=45)
plt.tight_layout()

plt.savefig("grafico_temperatura.png")
plt.show()

print("Gráfico gerado com sucesso!")


