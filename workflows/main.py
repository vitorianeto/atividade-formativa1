from calculadora import somar, subtrair, multiplicar, dividir

print("♡ Bem-vindo(a) à Atividade Formativa 1: Calculadora ♡")
while True:
    print("\nOperações disponíveis:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    operacao = input("\nEscolha uma operação (1/2/3/4/5): ")

    if operacao == "5":
        print("Saindo da calculadora... Até logo!")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == "1":
        print(f"O resultado da soma é: {somar(num1, num2)}")
    elif operacao == "2":
        print(f"O resultado da subtração é: {subtrair(num1, num2)}")
    elif operacao == "3":
        print(f"O resultado da multiplicação é: {multiplicar(num1, num2)}")
    elif operacao == "4":
        print(f"O resultado da divisão é: {dividir(num1, num2)}")
    else:
        print("Operação inválida! Tente novamente.")
