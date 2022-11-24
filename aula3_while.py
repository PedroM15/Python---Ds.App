# 1) -------------------------------------------

n = 1
soma = 0

while n <= 2:
    nota = int(input(f'Insira a {n} º nota'))
    soma = soma + nota
    n = n + 1

print(f'Resultado: {soma/2}')

# 2) -------------------------------------------

resp = 'S'
md: float

while resp != "N":
    nt1 = int(input(f'Digite a primeira nota: '))
    nt2 = int(input(f'Digite a segunda nota: '))

    md = (nt1 + nt2) / 2

    print(f'A media é: {md}')
    resp = input(f'Digite S para continuar e N para fechar ')

# 3) ------------------------------------------------------

n1 = 0
n2 = 0

while resp != 5:

print("  ---------------------------------------  ")
print(" | Calculadora:                          | ")

print(" |                                       | ")
print(" | Opções                                | ")
print(" |                                       | ")

print(" | 1 - Soma                              | ")
print(" | 2 - Subtração                         | ")
print(" | 3 - Multiplicação                     | ")
print(" | 4 - Divisão                           | ")
print(" | 5 - Sair                              | ")

print(" |                                       | ")
print("  ---------------------------------------  ")

escreval(" | Escreva o numero da opção que deseja: | ")
leia(resp)

print(" ")

if resp = 1:
n1 = 0
n2 = 0
print("Opção soma")
n1 = int(input('Insira o primeiro numero: '))
escreval("  Insira o segundo numero: ")
leia(n2)
print("  A soma resultou em: ", n1 + n2)
fimse

se
resp = 2
entao
n1 < - 0
n2 < - 0
print("Opção subtração")
n1 = int(input('Insira o primeiro numero: '))
escreval("  Insira o segundo numero: ")
leia(n2)
print("  A subtração resultou em: ", n1 - n2)
fimse

se
resp = 3
entao
n1 < - 0
n2 < - 0
print("Opção multiplicação")
escreval("  Insira o primeiro numero: ")
leia(n1)
escreval("  Insira o segundo numero: ")
leia(n2)
print("  A multiplicação resultou em: ", n1 * n2)
fimse

se
resp = 4
entao
n1 < - 0
n2 < - 0
print("Opção divisão")
escreval("  Insira o primeiro numero: ")
leia(n1)
escreval("  Insira o segundo numero: ")
leia(n2)
print("  A divisão resultou em: ", n1 / n2)

print(" ")


