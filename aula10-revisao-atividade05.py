'''
Questão 5: Validação de Formato de Email: Implemente um programa que peça ao usuário seu endereço de email. O programa deve verificar se o email segue um formato válido (contendo um @ e um .). Se o formato estiver incorreto, o programa deve continuar solicitando um email válido até que um seja fornecido.
'''

while True:
    email = input('Digite seu email: ')
    email = email.replace(' ', '')
    if '@' in email and '.' in email:
        break
    else:
        print('O endereço de email não é válido.')

print(f'O email {email} é válido!')
