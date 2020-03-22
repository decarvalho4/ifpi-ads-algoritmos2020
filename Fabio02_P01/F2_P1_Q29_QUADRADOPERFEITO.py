#Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas
#formadas pelos seus dois primeiros e dois últimos dígitos.
#Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
#Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado perfeito.

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

if raiz_quadrada == (primeiros_digitos+ultimos_digitos):
    print('O número é um quadrado perfeito.')

else:
    print('O número não é um quadrado perfeito.')


