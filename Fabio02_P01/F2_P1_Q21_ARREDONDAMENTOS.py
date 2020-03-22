#Realize arredondamentos de números utilizando a regra usual da matemática: se a parte fracionaria for
#maior do que ou igual a 0,5, o numero é arredondado para o inteiro imediatamente superior, caso
#contrario, é arredondado para o inteiro imediatamente inferior.

numero = float(input('Digite o número: '))

parte_fracionaria = ( numero * 10 ) % 10 / 10

if parte_fracionaria >= 0.5:
    print(numero + 1 - parte_fracionaria)

if parte_fracionaria < 0.5:
    print(numero - parte_fracionaria)





