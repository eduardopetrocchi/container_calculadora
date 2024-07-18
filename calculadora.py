def calculadora():
    continuar = []
    while continuar != "sair":

        n1 = int(input("Digite o valor: "))
        operacao = input("Digite a operação: ")
        n2 = int(input("Digite o valor: "))

        if operacao == "+":
            print(n1 + n2)
        elif operacao == "-":
            print(n1 - n2)
        elif operacao == "*":
            print(n1 * n2)

        if operacao == "/":
            if n2 != 0:
                print(n1 / n2)
            else:
                print("Não é possivel dividir por 0")
        continuar = input("Digite 'sair' ou 'continuar': ")

calculadora()
