'''
LOOP WHILE:
break, continue
'''

'''i = 0
while i < 5:
    i += 1
    print(i)'''

# VERIFICAR SENHA:
senha_correta = 'Leandro'
senha = ''

while senha != senha_correta:
    senha = input('Senha: ')
    if senha != senha_correta:
        print('Senha incorreta!!!')
print('Acertou a senha, pode entrar!')
