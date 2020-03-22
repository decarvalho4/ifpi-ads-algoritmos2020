#Leia a hora do início de um jogo e a hora de fim do jogo (cada hora é composta por 2 variáveis inteiras: hora e minuto).
# Calcule e escreva a duração do jogo (horas e minutos), sabendo-se que o tempo
# máximo de duração do jogo é de 24 horas e que ele pode iniciar-se em um dia e terminar no dia seguinte.

hora_inicio = int(input('Digite a hora de início: '))
minuto_inicio = int(input('Digite o minuto de início: '))

hora_final = int(input('Digite a hora do fim do jogo: '))
minuto_final = int(input('Digite o minuto do fim do jogo: '))

hora_duracao = hora_final - hora_inicio 
minutos_duracao = minuto_final + minuto_inicio 


if hora_inicio > hora_final and 120 > minutos_duracao > 60:
    print('O jogo durou',24 - (-hora_duracao) + 1,'horas e',minutos_duracao % 60, 'minutos' )
    
if hora_inicio < hora_final and 120 > minutos_duracao > 60:
    print('O jogo durou',(hora_duracao),'horas e',minutos_duracao % 60, 'minutos' )

if hora_inicio < hora_final and  minutos_duracao < 60:
    print('O jogo durou',hora_duracao,'e',minutos_duracao,'minutos')




