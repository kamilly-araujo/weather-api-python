# aquele link da api = endpoint
# endpoint é o link para os métodos get e post
# ex: https://api.open-meteo.com/v1/forecast 

# sempre que eu uso api em python, devo chamar a biblioteca de requisições
# pip install requests / -m pip install matplotlib / py -m pip install requests - esse foi

import requests
import matplotlib.pyplot as plt

# criar uma função chamada de buscar_clima

def buscar_clima(latitude, longitude):
    # deve informar o endpoint (api)
    endpoint = 'https://api.open-meteo.com/v1/forecast'
    # informar os parametros para o sistema em formato de dicionario
    # -> o dicionario trabalha com chave:valor
    parametros = {
        # "chave" : valor,
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "temperature_2m",
        "timezone": "America/Sao_Paulo"
    }
    resposta = requests.get(endpoint, params=parametros)
    # sempre que queremos obter a resposta usamos o comando
    # requests.get para pegar os valores e colocamos os atributos
    # requests.get(variavel_do_endpoint, parms=dicionário_com_parametros)
    
    # para o sistema usar o método post -> para mostrar as informações
    dados = resposta.json()
    # o sistema transofrma os dados em json para poder manipular eles
    return dados

latitude = float(input("informe a latitude "))
longitude = float(input("informe a longitude "))

# vamos começar a exibir informações para os usuários
dados = buscar_clima(latitude, longitude)

horas = dados['hourly']['time']
# chamo a base de dados, informo o parametro e qual a variavel o parametro vai ler
temperatura = dados['hourly']['temperature_2m']

plt.plot(horas, temperatura)
# plt.plot cria um gráfico, onde informo como parametro primeiro o eixo x e depois o eixo y
#plt.plot(eixo_x, eixo_y)
plt.title('TEMPERATURA POR HORA')

# para ver o gráfico
plt.show()