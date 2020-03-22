carne = str(input('Digite o tipo de carne: '))
quantidade = int(input('Digite a quantidade de carne em kg: '))

if carne == 'Filé' and quantidade <= 5:
    print('Filé de',quantidade,'kilos com preço total de',4.90*quantidade,'reais com',4.90*quantidade*0.05,'reais de desconto, ficando por',4.90*quantidade - 4.90*quantidade*0.05,'no valor final')

if carne == 'Filé' and quantidade > 5:
    print('Filé de',quantidade,'kilos com preço total de',5.80*quantidade,'reais com',5.80*quantidade*0.05,'reais de desconto, ficando por',5.80*quantidade - 5.80*quantidade*0.05,'no valor final')

if carne == 'Alcatra' and quantidade <= 5:
    print('Filé de',quantidade,'kilos com preço total de',5.90*quantidade,'reais com',5.90*quantidade*0.05,'reais de desconto, ficando por',5.90*quantidade - 5.90*quantidade*0.05,'no valor final')

if carne == 'Alcatra' and quantidade > 5:
    print('Filé de',quantidade,'kilos com preço total de',6.80*quantidade,'reais com',6.80*quantidade*0.05,'reais de desconto, ficando por',6.80*quantidade - 6.80*quantidade*0.05,'no valor final')

if carne == 'Picanha' and quantidade <= 5:
    print('Filé de',quantidade,'kilos com preço total de',6.90*quantidade,'reais com',6.90*quantidade*0.05,'reais de desconto, ficando por',6.90*quantidade - 6.90*quantidade*0.05,'no valor final')

if carne == 'Picanha' and quantidade > 5:
    print('Filé de',quantidade,'kilos com preço total de',7.80*quantidade,'reais com',7.80*quantidade*0.05,'reais de desconto, ficando por',7.80*quantidade - 7.80*quantidade*0.05,'no valor final')