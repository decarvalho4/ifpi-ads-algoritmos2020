p_pergunta = str(input("Telefonou para a vítima ? "))
s_pergunta = str(input("Esteve no local do crime ? "))
t_pergunta = str(input("Mora perto da vítima ? "))
qua_pergunta = str(input("Devia para a vítima ? "))
qui_pergunta = str(input("Já trabalhou com a vítima ? "))

if p_pergunta and s_pergunta and t_pergunta and qua_pergunta and qui_pergunta == 'sim':
    print('Você é o assassino!')

elif p_pergunta and s_pergunta or p_pergunta and t_pergunta or p_pergunta and qua_pergunta or p_pergunta and qui_pergunta == 'sim':
    print('Suspeita')

elif s_pergunta and p_pergunta or s_pergunta and t_pergunta or s_pergunta and qua_pergunta or s_pergunta and qui_pergunta == 'sim':
    print('Suspeita')

elif t_pergunta and s_pergunta or t_pergunta and p_pergunta or t_pergunta and qua_pergunta or t_pergunta and qui_pergunta == 'sim':
    print('Suspeita')

elif qua_pergunta and s_pergunta or qua_pergunta and p_pergunta or qua_pergunta and t_pergunta or qua_pergunta and qui_pergunta == 'sim':
    print('Suspeita')

elif qui_pergunta and s_pergunta or qui_pergunta and p_pergunta or qui_pergunta and qua_pergunta or qui_pergunta and t_pergunta == 'sim':
    print('Suspeita')


    
    

