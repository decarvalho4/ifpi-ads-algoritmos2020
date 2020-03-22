#Leia as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 

p_nota = float(input('Digite a primeira nota: '))
s_nota = float(input('Digite a segunda nota: '))

media = ( p_nota + s_nota) / 2

if media >= 9:
    print('Suas notas são',p_nota,'e',s_nota,'sua média ficou',media,'e seu conceito é A,portanto, aprovado.')
   

if 9 > media >= 7.5:
    print('Suas notas são',p_nota,'e',s_nota,'sua média ficou',media,'e seu conceito é B,portanto, aprovado.')

if 7.5 > media >= 6:
    print('Suas notas são',p_nota,'e',s_nota,'sua média ficou',media,'e seu conceito é C,portanto, aprovado.')

if 6 > media >= 4:
    print('Suas notas são',p_nota,'e',s_nota,'sua média ficou',media,'e seu conceito é D,portanto, reprovado.')

if 4 > media >= 0:
    print('Suas notas são',p_nota,'e',s_nota,'sua média ficou',media,'e seu conceito é E,portanto, reprovado.')
