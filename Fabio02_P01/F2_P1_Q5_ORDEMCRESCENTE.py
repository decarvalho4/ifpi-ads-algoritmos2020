#Leia 3 (três) números e escreva-os em ordem crescente.

a = int(input('Qual o primeiro número? '))
b = int(input('Qual o segundo número? '))
c = int(input('Qual o terceiro número? '))

if a > b > c:
    print(a,b,c)

if a < b < c:
    print(c,b,a)

if b > a > c:
    print(b,a,c)

if b > c > a:
    print(b,c,a)

if c > a > b:
    print(c,a,b)

elif c > b > a:
    print(c,b,a)