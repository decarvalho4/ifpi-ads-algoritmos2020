#Leia um número e escreva se o número é inteiro ou decimal.

numero = float(input('Digite um número: '))

if numero % 1 == 0:
    print('É inteiro')

else:
    print('É decimal')