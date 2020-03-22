#Leia duas notas de um aluno e escreva na tela a palavra “Aprovado” se a média das duas notas for maior
#ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcule a média final
#Se esta média for maior ou igual a 5,0, o programa deve escreva “Aprovado”, caso contrário deve escreva “Reprovado”.
#Escreva um algoritmo para ler um número e verificar se ele obedece a esta característica.

matematica = int(input('Digite a nota em matemática: '))
portugues = int(input('Digite a nota em português: '))

media = (matematica + portugues) / 2

if media >= 7:
    print('Aprovado')

else:
    print(matematica)
    print(portugues)

