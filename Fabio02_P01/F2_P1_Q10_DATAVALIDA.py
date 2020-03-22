#Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.


dia = int(input('Qual o dia? '))
mes = str(input('Qual o mes? '))
ano = int(input('Qual o ano? '))

janeiro = mes
fevereiro = mes
março = mes
abril = mes
maio = mes
junho = mes
julho = mes
agosto = mes
setembro = mes
outubro = mes
novembro = mes
dezembro = mes

if mes == janeiro and dia > 31:
    print('Inválido')

elif mes == fevereiro and dia > 29:
    print('Inválido')

elif mes == março and dia > 31:
    print('Inválido')

elif mes == abril and dia > 30:
    print('Inválido')

elif mes == maio and dia > 31:
    print('Inválido')

elif mes == junho and dia > 30:
    print('Inválido')

elif mes == julho and dia > 31:
    print('Inválido')

elif mes == agosto and dia > 31:
    print('Inválido')

elif mes == setembro and dia > 30:
    print('Inválido')

elif mes == outubro and dia > 31:
    print('Inválido')

elif mes == novembro and dia > 30:
    print('Inválido')

elif mes == dezembro and dia > 31:
    print('Inválido')




