# Verifique a validade de uma senha fornecida pelo usuário. 
# A senha é 1234. O algoritmo deve escrever uma mensagem de permissão de acesso ou não.

senha = int(input('Digite a senha: '))

if senha != 1234:
    print('Acesso negado')

else:
    print('Acesso permitido')