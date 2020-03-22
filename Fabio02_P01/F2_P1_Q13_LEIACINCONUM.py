#Leia 5 (cinco) números inteiros e escreva o maior e o menor deles. Considere que todos os valores são diferentes.

a = int(input('Qual o primeiro número?  '))
b = int(input('Qual o segundo número?  '))
c = int(input('Qual o terceiro número?  '))
d = int(input('Qual o quarto número?  '))
e = int(input('Qual o quinto número?  '))

if a > b and a > c and a > d and a > e:
    print('O maior é o', a)

if b > a and b > c and b > d and b > e:
    print('O maior é o', b)

if c > a and c > b and c > d and c > e:
    print('O maior é o', c)

if d > a and d > b and d > c and d > e:
    print('O maior é o', d)

if e > a and e > b and e > c and e > d:
    print('O maior é o', e)

if a < b and a < c and a < d and a < e:
    print('O menor é o', a )

if b < a and b < c and b < d and b < e:
    print('O menor é o', b )

if c < a and c < b and c < d and c < e:
    print('O menor é o', c )

if d < a and d < d and d < c and d < e:
    print('O menor é o', d )

if e < a and e < b and e < c and e < d:
    print('O menor é o', e )







