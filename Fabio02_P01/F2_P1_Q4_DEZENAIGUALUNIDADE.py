#Leia 1 (um) número de 2 (dois) dígitos, verifique e escreva se o algarismo da dezena é igual 
# ou diferente do algarismo da unidade.

numero = int(input('Qual o número de dois digitos? '))

dezena = numero // 10
unidade = numero % 10

if dezena == unidade:
    print('São iguais')
else:
    print('Não são iguais')
