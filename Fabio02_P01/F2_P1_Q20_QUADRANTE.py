#Leia a medida de um ângulo (entre 0 e 360°) e escreva o quadrante (primeiro, segundo, terceiro ou quarto) em que o ângulo se localiza.

angulo = int(input('Digite o ângulo: '))

if 0 <= angulo <= 90:
    print('Primeiro quadrante')

if 90 < angulo <= 180:
    print('Segundo quadrante')

if 180 < angulo <= 270:
    print('Terceiro quadrante')

if 270 < angulo <= 360:
    print('Quarto quadrante')