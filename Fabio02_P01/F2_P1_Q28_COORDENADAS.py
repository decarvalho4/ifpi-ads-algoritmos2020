#Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de um retângulo. 
#calcule e escreva a área deste retângulo. Lembre-se de que o valor da área não pode ser negativo.

x_primeiro_ponto = int(input('Digite o x do primeiro ponto: '))
y_primeiro_ponto = int(input('Digite o y do primeiro ponto: '))

area = x_primeiro_ponto * y_primeiro_ponto

if area < 0:
    print('Não existe')

else:
    print('A área deste retângulo é',area,'metros.')