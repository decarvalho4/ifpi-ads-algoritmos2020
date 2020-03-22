#Leia a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um.
#Escreva na tela qual dos professores tem salário total maior.

horas_prof1 = int(input('Quantas horas o primeiro professor deu de aula? '))
horas_prof2 = int(input('Quantas horas o segundo professor deu de aula? '))
valor_prof1 = int(input('Qual o valor da hora do primeiro professor? '))
valor_prof2 = int(input('Qual o valor da hora do segundo professor? '))

salario_1 = horas_prof1 * valor_prof1
salario_2 = horas_prof2 * valor_prof2

if salario_1 > salario_2:
    print('O maior salário é o do primeiro professor')

else:
    print('O maior salário é o do segundo professor')


