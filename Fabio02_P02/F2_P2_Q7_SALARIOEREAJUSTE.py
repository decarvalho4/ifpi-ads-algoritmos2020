salario = float(input('Digite o salário: '))

if salario <= 280:
    print('O salário antes do reajuste é',salario,'seu aumento é de 20%, ou seja',salario*0.20,'reais, seu novo valor é',salario+salario*0.20)

if salario > 280 and salario < 700:
    print('O salário antes do reajuste é',salario,'seu aumento é de 15%, ou seja',salario*0.15,'reais, seu novo valor é',salario+salario*0.15)
    

if salario > 700 and salario < 1500:
    print('O salário antes do reajuste é',salario,'seu aumento é de 10%, ou seja',salario*0.10,'reais, seu novo valor é',salario+salario*0.10)

if salario > 1500:
    print('O salário antes do reajuste é',salario,'seu aumento é de 5%, ou seja',salario*0.05,'reais, seu novo valor é',salario+salario*0.05)