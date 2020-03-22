#Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos.

a = int(input('Digite o tamanho do primeiro lado: '))
b = int(input('Digite o tamanho do segundo lado: '))
c = int(input('Digite o tamanho do terceiro lado: '))

if a > b > c or a > c > b:
    print(a,'é a hipotenusa e',b,'e',c,'os catetos')

if b > a > c or b > c > a:
    print(b,'é a hipotenusa',a,'e',c,'são os catetos')

if c > a > b or c > b > a:
    print(c,'é a hipotenusa',a,'e',b,'são os catetos')