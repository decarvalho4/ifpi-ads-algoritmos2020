#Leia 3 (três) números (cada número corresponde a um lado do triângulo), 
#verifique e escreva se os 3 (três) números formam um triângulo 
#(a soma de dois lados não pode ser menor que o terceiro lado). 
#Se formam, verifique se formam um triângulo equilátero (3 lados iguais), isósceles (2 lados iguais) ou
#escaleno (3 lados diferentes). Não existe lado com tamanho 0 (zero).

a = int(input('Qual o primeiro lado? '))
b = int(input('Qual o segundo lado? '))
c = int(input('Qual o terceiro lado? '))

if a + b < c or a + c < b or b + c < a:
    print('Não é um triângulo')

if a == b == c:
    print('É um triângulo equilátero')

elif a == b and a == c or b == c and b == a or c == a and c == b:
    print('É um triângulo isósceles')

elif a != b and b != c:
    print('É um triângulo escaleno')