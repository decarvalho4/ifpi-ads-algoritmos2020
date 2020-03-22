#Leia 3 (três) números, verifique e escreva quantos números iguais existem entre os números.

a = int(input('Qual o primeiro número? '))
b = int(input('Qual o segundo número? '))
c = int(input('Qual o terceiro número? '))

if a == b == c:
    print('Os três números são iguais')
    
if a == b != c:
    print('Dois números são iguais')

if a != b == c:
    print('Dois números são iguais')

if a != b != c:
    print('Nenhum número é igual')

if a == c:
     print('Dois números são iguais')

