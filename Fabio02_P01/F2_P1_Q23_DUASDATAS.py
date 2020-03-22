#Leia 2 datas (cada data é composta por 3 variáveis inteiras: dia, mês e ano) e escreva qual delas é a mais recente.

dia_data_1 = int(input('Digite o dia da primeira data: '))
mes_data_1 = int(input('Digite o mês da primeira data: '))
ano_data_1 = int(input('Digite o ano da primeira data: '))

dia_data_2 = int(input('Digite o dia da segunda data: '))
mes_data_2 = int(input('Digite o mês da segunda data: '))
ano_data_2 = int(input('Digite o ano da segunda data: '))

if dia_data_1 > dia_data_2 and mes_data_1 >= mes_data_2 and ano_data_1 >= ano_data_2:
    print('A primeira data é a mais recente')

elif dia_data_1 <= dia_data_2 and mes_data_1 >= mes_data_2 and ano_data_1 >= ano_data_2:
    print('A primeira data é a mais recente')

elif dia_data_2 >= dia_data_1 and mes_data_2 >= mes_data_1 and ano_data_2 >= ano_data_1:
    print('A segunda data é a mais recente') 

elif dia_data_2 <= dia_data_1 and mes_data_2 >= mes_data_1 and ano_data_2 >= ano_data_1:
    print('A segunda data é a mais recente')