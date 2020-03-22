#Leia 2 (duas) notas parciais de um aluno, calcule a média e escreva a mensagem:
#o "Aprovado", se a média alcançada for maior ou igual a sete;
#o "Reprovado", se a média for menor do que sete;
#o "Aprovado com Distinção", se a média for igual a dez.

nota_1 = int(input('Digite a primeira nota: '))
nota_2 = int(input('Digite a segunda nota: '))

media = ( nota_1 + nota_2 ) / 2

if media >= 7:
    print('Aprovado')

if media < 7 :
    print('Reprovado')

if media == 10:
    print('Aprovado com distinção')