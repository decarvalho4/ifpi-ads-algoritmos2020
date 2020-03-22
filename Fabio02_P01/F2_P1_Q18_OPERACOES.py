#Leia dois valores e uma das seguintes operações a serem executadas (codificadas da seguinte forma: 1 –
#Adição, 2 – Subtração, 3 – Multiplicação e 4 – Divisão). Calcule e escreva o resultado dessa operação sobre os dois valores lidos.

x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))
operacao = int(input('Digite a operação: '))

if operacao == 1:
    print(x+y)

if operacao == 2:
    print(x-y)

if operacao == 3:
    print(x*y)

if operacao == 4:
    print(x/y)