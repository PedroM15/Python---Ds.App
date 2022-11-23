# -------------------------------------------------------------------

num1, num2 = input("Digite um numero."),\
             input("Digite outro numero.")

num1, num2 = int(input("Digite um numero.")),\
             int(input("Digite outro numero."))
soma = (num1 + num2)
print(f'A soma é {soma} ')

# -------------------------------------------------------------------

print('Selecione uma opção')
print('1 - mostra pares')
print('2 - mostra impares e sua soma')
print('3 - conta impares e sua soma')
print('4 - Conta os pares')
print('5 - Sair')

op = int(input())

print(op)

# -------------------------------------------------------------------

i, f =int(input('Insira primeiro numero: ')),\
      int(input('Insira segundo numero: '))

i, f =int(input('Insira o primeiro e segundo numero: ')),\
      int(input(' '))

print(i, f)
