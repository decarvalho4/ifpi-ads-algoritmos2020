#Leia quatro números (opção, num 1, num2, num3) e que escreva o valor de num1 se opção igual a 1; 
#valor de num2 se opção for igual a 2; e o valor de num3 se opção for igual a 3. Os únicos valores
#possíveis para a variável opção são 1, 2 e 3.

opcao = int(input('Qual o primeiro número? '))
num1 = int(input('Qual o segundo número? '))
num2 = int(input('Qual o terceiro número? '))
num3 = int(input('Qual o quarto número? '))

if opcao == 1:
    print(num1)

if opcao == 2:
    print(num2)

if opcao == 3:
    print(num3)
