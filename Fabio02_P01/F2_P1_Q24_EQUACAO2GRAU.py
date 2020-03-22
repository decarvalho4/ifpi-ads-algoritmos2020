#Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes.
#coeficiente A deve ser diferente de 0 (zero).

a = int(input('Digite o coeficiente A  '))
b = int(input('Digite o coeficiente B  '))
c = int(input('Digite o coeficiente C  '))

delta = (b**2) - 4 * a * c

raiz_1 = (-b + delta**1/2) / 2*a

raiz_2 = (-b - delta**1/2) / 2*a

print(raiz_1 + raiz_2)