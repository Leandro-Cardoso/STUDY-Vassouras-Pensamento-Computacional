'''
Questão 3 -
Crie um o qual o usuário irá digitar uma senha. Caso a senha seja digitada de forma incorreta, o programa deverá continuar em loop pedindo para que a senha seja fornecida novamente.

Exemplo de resposta esperada:
Insira a senha correta: najsdnjlsakd

Senha errada!
Inira a senha correta: jklansdlkasjd

Senha errada!
Inira a senha correta: 123456

Senha correta. Pode continuar
'''

import random
senha_certa = '123456'

# Seu código abaixo

senha = ''

while senha != senha_certa:
    senha = input('Digite a senha: ')
    if senha != senha_certa:
        print('Senha incorreta...')

print('Senha correta!!!')
