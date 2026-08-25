from datetime import datetime

nome = input("Qual é o seu nome? ")

agora = datetime.now()

hora_atual = agora.strftime("%H:%M:%S")

print(f"Oi, {nome}! Tudo bem? Agora são {hora_atual}.")