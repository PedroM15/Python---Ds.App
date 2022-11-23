# 1) ------------------------------------------------

i = int(input('Insira um numero: '))
f = int(input('Insira um numero: '))
for x in range(i, f+1):
    print(x)

# 2) ------------------------------------------------

for x in range (1, 11):
    print(f'5 x {x} a {5 * x}')

# 3) ------------------------------------------------

tabu = int(input('Informe a tabuada que deseja: '))
for x in range (1, 10+1):
    print(f'{tabu} x {x} = {tabu * x}')

# 4) ------------------------------------------------

ini = int(input('Informe o primeiro valor: '))
fim = int(input('Informe o segundo valor: '))

for x in range(ini, fim+1):
    if x % 3 == 0:
        print(x)

# 5) ------------------------------------------------

ini = int(input('Informe o primeiro valor: '))
final = int(input('Informe o ultimo valor: '))
di = int(input('Informe o numero divisor: '))

for x in range(ini, final+1):
    if x % di == 0:
        print(x)

# 6) ------------------------------------------------

ini = int(input('Informe o primeiro valor: '))
fim = int(input('Informe o ultimo valor: '))

x: int
for x in range (ini, fim):
    adc = x
    if adc % 2 == 1:
        print(x)

# 7) ------------------------------------------------

lc = int(input('Insira o tamanho da reta numerica: '))
n1 = int(input('Insira o primeiro numero da reta numerica: '))

menor: int
maior: int

menor = n1
maior = n1

for x in range (2, lc):
    n1= int(input(f'Insira o {x} º numero: '))
    if n1 < menor:
        menor = n1

    if n1 > maior:
        maior = n1

print(f'O menor nummero digitado é: {menor}')
print(f'O maior nummero digitado é: {maior}')

# 8) ------------------------------------------------

for x in range(0, 29):
    print(30 - x)

# 9) ------------------------------------------------

ant: int
ant = 1

antes: int
antes = 0

atu: int

for x in range(1, 10):
    atu = ant + antes
    antes = ant
    ant = atu
    print(atu)

# 10) ------------------------------------------------

soma: int
soma = 0
for x in range(1, 5):
    n = int(input(f'Insira o {x} º numero: '))
    if n > 40:
        soma = soma + n
print(soma)

# 11) ------------------------------------------------

soma: int
soma = 0

prod = int(input('Informe a quantidade de produtos: '))
for x in range(1, prod):
    n = int(input(f'Digite o valor do {x} º produto'))
    soma = soma + n
print(f'O valor total em estoque é: {soma}')
print(f'A media de produtos é: {soma / prod}')

# 12) ------------------------------------------------

somasalario: int
somasalario = 0

somafilhos: int
somafilhos = 0

maiorsalario: int
maiorsalario = 0

contador: int
contador = 0

for x in range(1, 2):
     salario = int(input("Informe o salário!"))
     filhos = int(input("Informe a quantidade de filhos!"))
     somasalario = somasalario + salario
     somafilhos = somafilhos + filhos
     if salario > maiorsalario:
        maiorsalario = salario

     if salario < 150:
        contador = contador +1


print("A Média de salário da população é: ", somasalario/2)
print("A Média do número de filhos é: ", somafilhos/2)
print("O Maior salário informado foi: ", maiorsalario)
print("O Percentual de pessoas com salário menor que R$ 150,00 é: ", (contador/2) * 100, "%")
