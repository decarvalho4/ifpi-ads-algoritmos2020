#Leia 3 (três) números (cada número corresponde a um ângulo interno do triângulo), verifique e escreva
#se os 3 (três) números formam um triângulo (a soma dos ângulos internos é igual a 180o). Se formam,
#verifique se formam um triângulo acutângulo (3 ângulos < 90o), retângulo (1 ângulo = 90o) ou
#obtusângulo (1 ângulo > 90o). Não existe ângulo com tamanho 0o (zero grau).

a = int(input('Qual o primeiro ângulo? '))
b = int(input('Qual o segundo ângulo? '))
c = int(input('Qual o terceiro ângulo? '))

if a + b + c == 180:
    print('É um triângulo')

else:
    print('Não é um triângulo')
    
if a < 90 and  b < 90 and c < 90:
    print('É um triângulo acutângulo')

if a == 90 or b == 90 or c == 90:
    print('É um triângulo retângulo')

if a > 90 or b > 90 or c > 90:
    print('É um triângulo obtusângulo')


