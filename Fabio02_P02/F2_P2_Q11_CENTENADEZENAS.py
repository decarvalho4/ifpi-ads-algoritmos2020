#Leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do número. 
#Observando os termos no plural a colocação do "e", da vírgula entre outros. 
#Exemplos: o 326 = 3 centenas, 2 dezenas e 6 unidades
#o 12 = 1 dezena e 2 unidades

numero = int(input('Digite o número inteiro: '))

centena = numero // 100
resto_centena = numero % 100
dezena = resto_centena // 10
unidade = resto_centena % 10

if centena > 1 and dezena > 1 and unidade > 1:
    print(numero, '=',centena,'centenas,',dezena,'dezenas e',unidade,'unidades')

if centena > 1 and dezena == 1 and unidade > 1:
    print(numero, '=',centena,'centenas,',dezena,'dezena e',unidade,'unidades')

if centena > 1 and dezena == 1 and unidade == 1:
    print(numero, '=',centena,'centenas,',dezena,'dezena e',unidade,'unidade')

if centena == 1 and dezena > 1 and unidade > 1:
    print(numero, '=',centena,'centena,',dezena,'dezenas e',unidade,'unidades')

if centena == 1 and dezena == 1 and unidade > 1:
    print(numero, '=',centena,'centena,',dezena,'dezena e',unidade,'unidades')

if centena == 1 and dezena > 1 and unidade == 1:
    print(numero, '=',centena,'centena,',dezena,'dezenas e',unidade,'unidade')