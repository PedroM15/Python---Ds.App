# Remeber) -----------------------------------------------------------

a = int(input('escreva o valor de A: '))
b = int(input('escreva o valor de B: '))
c = int(input('escreva o valor de C: '))
if (a + b) < c:
    print('o valor da soma de a+b é menor que c')

# 1) -----------------------------------------------------------

a = int(input('Insira o valor de A: '))
b = int(input('Insira o valor de B: '))
if a == b:
    print('A soma de A+B é: ', a+b)
else:
    print("A multiplicação de AxB é: ", a * b)

# 2) -----------------------------------------------------------

n1 = int(input('Insira um numero: '))
if n1 < 0 :
    print('O numero é negativo; ', n1*3)
else:
    print('O numero é positivo: ', n1*2)

# 3) -----------------------------------------------------------

n = int(input('Insira um numero: '))
if n % 2 == 1:
    print('O numero é impar: ', n+8)
else:
    print('O numero é par: ', n+5)

# 4) -----------------------------------------------------------

a = int(input('Digite o 1º número: '))
b = int(input('Digite o 2º número: '))
c = int(input('Digite o 3º número: '))

if (a < b) and (b < c) and (a < c):
    print(c, b, a,)

if (a < b) and (b > c) and (a < c):
    print(b, c, a,)

if (a > b) and (b < c) and (a < c):
    print(c, a, b,)

if (a < b) and (a > c) and (b > c):
    print(b, a, c,)

if (a > b) and (a > c) and (b < c):
    print(a, c, b,)

if (a > b) and (b > c) and (b > c):
    print(a, b, c,)

# 5) -----------------------------------------------------------

peso = float(input('Insira o seu peso: '))
alt = float(input('Insira a sua altura: '))

imc = peso / alt ** 2
if imc <= 18.5:
    print('Voce esta abaixo do peso: ', imc)

if (imc >= 18.5) and (imc == 25):
    print('Voce esta com o peso normal: ', imc)

if (imc >= 25) and (imc == 30):
    print('Voce esta acima do peso: ', imc)

if imc > 30:
    print('Voce esta obeso do peso: ', imc)'

# 6) -----------------------------------------------------------

n1 = int(input('Insira a primeira nota: '))
n2 = int(input('Insira a segunda nota: '))

med = (n1 + n2) / 2

if (med >= 7) and (med < 10):
    print('Aprovado')

if (med < 7):
    print('Reprovado')

if (med == 10) and (med > 9):
    print('Aprovado com distinção')

# 7) -----------------------------------------------------------

n1 = int(input('Insira o 1º numero: '))
n2 = int(input('Insira o 2º numero: '))
n3 = int(input('Insira o 3º numero: '))

if (n1 > n2) and (n1 > n3):
    print('O maior numero digitado foi: ', n1)
else
    if (n2 > n1) and (n2 > n3):
        print('O maior numero digitado foi: ', n2)
    else
        print('O maior numero digitado foi: ', n3)

# 8) -----------------------------------------------------------

p1 = int(input('Insira o valor do 1º produto: '))
p2 = int(input('Insira valor do 2º produto: '))
p3 = int(input('Insira valor do 3º produto: '))

if (p1 > p2) and (p1 > p3):
    print('O produto mais barato é: ', p1)
else
    if (p2 > p1) and (p2 > p3):
        print('O produto mais barato é: ', p2)
    else
        print('O produto mais barato é: ', p3)

# 9) -----------------------------------------------------------

n1 = int(input('Insira o 1º numero: '))
n2 = int(input('Insira o 2º numero: '))
n3 = int(input('Insira o 3º numero: '))

if (n1 > n2) and (n1 > n3):
    print('O maior numero digitado foi: ', n1)
else
    if (n2 > n1) and (n2 > n3):
        print('O maior numero digitado foi: ', n2)
    else
        print('O maior numero digitado foi: ', n3)
