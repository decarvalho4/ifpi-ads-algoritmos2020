#Eistem números de 4 dígitos (entre 1000 e 9999) que obedecem à seguinte característica: se dividirmos
#o número em dois números de dois dígitos, um composto pela dezena e pela unidade, e outro pelo
#milhar e pela centena, se somarmos estes dois novos números gerando um terceiro, o quadrado deste
#terceiro número é exatamente o número original de quatro dígitos. Por exemplo:
#2025 -> dividindo: 20 e 25 -> somando temos 45 -> 452 = 2025

numero = int(input('Digite o número de 4 dígitos: '))

raiz_quadrada = numero ** 1/2
milhar = numero // 1000
resto_milhar = numero % 1000  
centena = resto_milhar // 100
resto_centena = resto_milhar % 100
dezena = resto_centena // 10
unidade = resto_centena % 10

primeiros_digitos = milhar*10 + centena
ultimos_digitos = dezena*10 + unidade
soma = primeiros_digitos + ultimos_digitos

if soma ** 2 == numero:
    print('Funcionou com esse número.')

else:
    print('Não funcionou.')