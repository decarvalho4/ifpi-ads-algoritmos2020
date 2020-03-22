#Leia 1 (um) número entre 0 e 100, verifique e escreva se o número é ou não primo.

numero = int(input('Qual o número ?'))

if numero % 2 > 0:
    print('É primo')
else:
    print('Não é primo')

