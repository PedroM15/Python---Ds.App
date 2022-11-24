# -------------------------------------------------------------------

print('Insira os valores abaixo: ')
l, c, h = int(input('largura: ')), \
          int(input('comprimento: ')),\
          int(input('altura: '))

print('O volume do produto dos tres valores é: ', l * c * h)

# -------------------------------------------------------------------

vb, vn, vv = int(input('Quantidades de votos brancos: ')),\
            int(input('Quantidades de votos nulos: ')),\
            int(input('Quantidades de votos validos: '))
print('Quantidade de votos totais: ', vb + vn + vv)

print('A soma dos brancos é: ',
            vb * 100 // (vb + vn + vv), '%')
print('A soma dos nulos é: ',
            vn * 100 // (vb + vn + vv), '%')
print('A soma dos validos é: ',
            vv * 100 // (vb + vn + vv), '%')

n1 = int(input('Insira o 1°  numero: '))
n2 = int(input('Insira o 2°  numero: '))
n3 = int(input('Insira o 3°  numero: '))
media = (n1*2 + n2*3 + n3*5)/10
print('A media obtida foi: ', media)
