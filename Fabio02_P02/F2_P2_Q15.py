morango = float(input('Digite a quantidade em Kg de morangos: '))
maca = float(input('Digite a quantidade em Kg de maçãs: '))

if morango <= 5 and maca <= 5:
    print('Será gasto',morango * 2.50,' reais em morango e',maca * 1.80,'reais em maças')

if 8 > morango > 5 and 8 > maca > 5:
    print('Será gasto',morango * 2.20,' reais em morango e',maca * 1.50,'reais em maças')

if morango >= 8 and maca >= 8:
    print('Será gasto',morango * 2.50 - morango * 2.50 * 0.10,' reais em morango e',maca * 1.80 - maca * 2.50 * 0.10,'reais em maças')