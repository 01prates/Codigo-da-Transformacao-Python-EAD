import json

clientes = {
    "1": {
        "nome": "Carlos",
        "idade": 16
    },
    "2": {
        "nome": "João",
        "idade": 17
    }
}

with open("clientes.json", "w") as arquivo:
    json.dump(clientes, arquivo, indent=4)

with open("clientes.json", "r") as arquivo:
    dados = json.load(arquivo)

print(dados)