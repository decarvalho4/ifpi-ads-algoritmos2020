#Leia o turno em que um aluno estuda, sendo M para matutino, V para Vespertino ou N para Noturno 
#escreva a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = str(input('Digite a letra do turno: '))

if turno == 'M':
    print('Bom dia!')

elif turno == 'V':
    print('Boa tarde!')

elif turno == 'N':
    print('Boa noite!')

else:
    print('Valor inválido!')

