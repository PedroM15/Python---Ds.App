def exerc4():
    soma = 0
    prod = 1

    num = int(input("DIGITE UM NÚMERO POSITIVO E 'ZERO' PARA TERMINAR: "))

    if num == 0:
        prod = 0
    else:
        while num != 0:
            if num % 2 == 0:
                soma = soma + num
            else:
                prod = prod * num

            num = int(input("DIGITE UM NÚMERO POSITIVO OU 'ZERO' PARA TERMINAR: "))

    print("A SOMA DOS NUMEROS PARES É: ", soma)
    print("O PRODUTO DOS NUMEROS IMPARES É: ", prod)

exerc4()
