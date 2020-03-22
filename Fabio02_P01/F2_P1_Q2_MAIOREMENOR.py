#Leia 2 (dois) números, verifique e escreva o menor e o maior entre os números lidos.

a = int(input('Qual o primeiro número? '))
b = int(input('Qual o segundo número? '))

if a > b:
    print(a,'é o maior')
elif a < b:
    print(b,'é o maior')
else:
    print('Os dois são iguais')

