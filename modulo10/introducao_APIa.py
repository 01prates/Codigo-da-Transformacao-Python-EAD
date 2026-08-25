import requests

API_KEY = "SUA_CHAVE_AQUI"

cidade = input("Digite o nome da cidade: ")

url = "https://api.openweathermap.org/data/2.5/weather"

parametros = {
    "q": cidade,
    "appid": API_KEY,
    "units": "metric",
    "lang": "pt_br"
}

try:
    resposta = requests.get(url, params=parametros)

    if resposta.status_code == 200:
        dados = resposta.json()
        print("Dados recebidos com sucesso!")

    else:
        print("Erro ao consultar a API.")

except requests.exceptions.RequestException:
    print("Erro de conexão com a API.")