def calcular_media():
    print("=== SISTEMA DE NOTAS ===")
    
    # Solicita o nome do aluno
    nome = input("Digite o nome do aluno: ").strip()
    
    # Loop para garantir entrada correta das 3 notas
    notas = []
    for i in range(1, 4):
        while True:
            try:
                nota = float(input(f"Digite a {i}ª nota (0 a 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Por favor, digite uma nota entre 0 e 10.")
            except ValueError:
                print("Entrada inválida! Digite apenas números.")

    # Cálculo da média
    media = sum(notas) / len(notas)
    
    # Exibição do resultado
    print("\n---------------------------")
    print(f"Aluno: {nome}")
    print(f"Média final: {media:.1f}")
    
    if media >= 6.0:
        print("Status: APROVADO! 🎉")
    else:
        print("Status: REPROVADO. ❌")
    print("---------------------------")

if __name__ == "__main__":
    calcular_media()