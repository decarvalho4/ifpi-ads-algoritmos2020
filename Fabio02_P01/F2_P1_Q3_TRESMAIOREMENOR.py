#Leia 3 (três) números, verifique e escreva o maior entre os números lidos.

a = int(input('Qual o primeiro número? '))
b = int(input('Qual o segundo número? '))
c = int(input('Qual o terceiro número? '))

if a == b ==c:
    print('Todos são iguais')

elif a == b > c:
    print(a,'e',b,'são iguais e maior que',c)

elif a < b == c:
    print(a,'é menor que',b,c,'que por ventura,são iguais')

elif a > b > c:
    print(a,'é o maior entre os números')
    
elif a > b == c:
    print(a,'é o maior entre os números')

elif b > a > c:
    print(b,'é o maior entre os números')

elif b > c > a:
    print(b,'é o maior entre os números')

elif b > a == c:
    print(b,'é o maior entre os números')

elif c > a > b:
    print(c,'é o maior entre os números')

elif c > b > a:
    print(c,'é o maior entre os números')

elif c > a == b:
    print(c,'é o maior entre os números')



