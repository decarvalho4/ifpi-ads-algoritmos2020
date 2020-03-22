litros = int(input('Digite o número de litros vendidos: '))
tipo_comb = str(input('Digite o tipo de combustível: '))

valor_pago_alcool = 1.90 * litros
valor_pago_gasolina = 2.50 * litros 

if tipo_comb == 'A' and litros <= 20:
    print('O valor a ser pago será de: ',valor_pago_alcool - valor_pago_alcool*0.03,'reais')

if tipo_comb == 'A' and litros > 20:
    print('O valor a ser pago será de: ',valor_pago_alcool - valor_pago_alcool*0.05,'reais')

if tipo_comb == 'G' and litros <= 20:
    print('O valor a ser pago será de: ',valor_pago_gasolina - valor_pago_alcool*0.04,'reais')

if tipo_comb == 'G' and litros > 20:
    print('O valor a ser pago será de: ',valor_pago_gasolina - valor_pago_alcool*0.06,'reais')