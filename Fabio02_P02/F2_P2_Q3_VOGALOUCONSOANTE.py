#Leia uma letra e verifique se a letra digitada é vogal ou consoante.

letra = str(input('Digite a letra: '))

if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print('Vogal')

if letra != 'a' or letra != 'e' or letra != 'i' or letra != 'o' or letra != 'u':
    print('Consoante')