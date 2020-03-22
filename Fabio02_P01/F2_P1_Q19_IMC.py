#Leia a altura (em metros) e peso (em Kg) de uma pessoa, em seguida calcule o índice de massa corpórea
#(IMC = peso / altura2). Ao final, escreva se a pessoa está com peso normal (IMC abaixo de 25), obeso
#(IMC entre 25 e 30) ou obesidade mórbida (IMC acima de 30).

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = peso / (altura*2)

if imc < 25:
    print('Normal')

if 30 > imc > 25:
    print('Obeso')

if imc > 30:
    print('Obeso mórbido') 