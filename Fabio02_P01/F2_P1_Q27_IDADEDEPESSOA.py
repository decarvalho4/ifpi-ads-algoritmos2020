#Determine a idade de uma pessoa em anos, meses e dias, dadas a data (dia, mês e ano) do seu nascimento e a data (dia, mês e ano) atual.

dia_atual = int(input('Qual o dia atual ? '))
mes_atual = int(input('Qual o mês atual ? '))
ano_atual = int(input('Qual o ano atual ? '))

dia_nascimento = int(input('Qual o dia você nasceu ? '))
mes_nascimento = int(input('Qual o mês de nascimento ? '))
ano_nascimento = int(input('Qual o ano de nascimento ? '))

idade_atual = ano_atual - ano_nascimento

if mes_atual == mes_nascimento and dia_atual == dia_nascimento:
    print(idade_atual)

elif mes_atual < mes_nascimento:
    print(idade_atual - 1)

elif mes_atual <= mes_nascimento and dia_atual < dia_nascimento:
    print(idade_atual - 1)

elif mes_atual >= mes_nascimento and dia_atual >= dia_nascimento or dia_atual <= dia_nascimento :
    print(idade_atual)
    


