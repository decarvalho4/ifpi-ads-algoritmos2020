valor_hora = int(input('Digite o valor da hora: '))
qntd_hora = int(input('Digite a quantidade de horas trabalhadas: '))

salario = valor_hora * qntd_hora

if salario <= 900:
    print('Isento de impostos')

if salario > 900 and salario <= 1500:
    print('O salário bruto é ',salario,' e o desconto é de ',salario*0.05,'reais, seu salário líquido é ',salario-salario*0.05)

if salario > 1500 and salario <= 2500:
    print('O salário bruto é ',salario,' e o desconto é de ',salario*0.10,'reais, seu salário líquido é ',salario-salario*0.10)

if salario > 2500:
    print('O salário bruto é ',salario,' e o desconto é de ',salario*0.20,'reais, seu salário líquido é ',salario-salario*0.20)
