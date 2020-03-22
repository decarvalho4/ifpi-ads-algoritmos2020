#Leia o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é sempre pelo mais barato.

x = float(input('Digite o preço do primeiro produto: '))
y = float(input('Digite o preço do segundo produto: '))
z = float(input('Digite o preço do terceiro produto: '))

if x > y > z or y > x > z:
    print('O mais barato é o produto de preço',z)

if x > z > y or z > x > y:
    print('O mais barato é o produto de preço',y)

if z > y > x or y > z > x:
    print('O mais barato é o produto de preço',x)
