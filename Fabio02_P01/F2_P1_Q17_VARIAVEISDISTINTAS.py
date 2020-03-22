#Leia valores inteiros em duas variáveis distintas e se o resto da divisão da primeira pela segunda for 1
#escreva a soma dessas variáveis mais o resto da divisão; se for 2 escreva se o primeiro e o segundo valor
#são pares ou ímpares; se for igual a 3 multiplique a soma dos valores lidos pelo primeiro; se for igual a 4
#divida a soma dos números lidos pelo segundo, se este for diferente de zero. Em qualquer outra situação
#escreva o quadrado dos números lidos.

x = int(input('Digite o primeiro valor: '))
y = int(input('Digite o segundo valor: '))

resto = x % y
soma = ( x + y) / x % y
multiplique = ( x + y ) * x
divida = ( x + y) / y
quadrado = ( x + y) ** 2

if resto == 1: 
    print(soma)

if resto == 3:
    print(multiplique)

if resto == 4:
    print(divida)

if resto != 0 and resto > 1 and resto > 2 and resto > 3 and resto > 4:
    print(quadrado)