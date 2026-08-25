def calculadora():
    try:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))

        operacao = input("Digite +, -, * ou /: ")

        if operacao == "+":
            resultado = a + b
        elif operacao == "-":
            resultado = a - b
        elif operacao == "*":
            resultado = a * b
        elif operacao == "/":
            resultado = a / b
        else:
            print("Operação inválida!")
            return

        print("Resultado:", resultado)

    except ZeroDivisionError:
        print("Erro: não é possível dividir por zero!")

    except ValueError:
        print("Erro: digite apenas números!")

calculadora()