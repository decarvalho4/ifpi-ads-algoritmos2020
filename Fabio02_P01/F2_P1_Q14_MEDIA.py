#Leia 5 (cinco) números inteiros, calcule a sua média e escreva os que são maiores que a média.

a = int(input('Qual o primeiro número?  '))
b = int(input('Qual o segundo número?  '))
c = int(input('Qual o terceiro número?  '))
d = int(input('Qual o quarto número?  '))
e = int(input('Qual o quinto número?  '))

media = ( a + b + c + d +e ) / 5


if a > media:
    print('O valor',a,'é maior que a media')
else:
    print(print('O valor',a,'é menor que a media'))

if b > media:
    print('O valor',b,'é maior que a media')
else:
    print('O valor',b,'é menor que a media')

if c > media:
    print('O valor',c,'é maior que a media')
else:
    print('O valor',c,'é menor que a media')

if d > media:
    print('O valor',d,'é maior que a media')
else:
    print('O valor',d,'é menor que a media')

if e > media:
    print('O valor',e,'é maior que a media')
else:
    print('O valor',e,'é menor que a media')