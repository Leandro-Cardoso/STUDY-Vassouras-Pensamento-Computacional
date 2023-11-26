'''
Questão 4: Escreva um programa que peça ao usuário para criar um nome de usuário. Se o nome de usuário inserido não seguir os critérios especificados (por exemplo, deve ter entre 5 e 10 caracteres, contendo apenas letras e números), o programa deverá solicitar que o usuário o insira novamente até que um nome de usuário válido seja fornecido.
'''

min_char = 5
max_char = 10

while True:
    usuario = input('Digite o nome de usuário: ')
    usuario.replace(' ', '')
    if min_char <= len(usuario) <= max_char:
        chars_validados = 0
        for char in usuario:
            if char.isnumeric() or char.isalpha():
                chars_validados += 1
        if chars_validados == len(usuario):
            break
        else:
            print('O nome de usuário deve conter apenas numeros e letras.')
    else:
        print('O nome de usuário deve ter entre 5 até 10 caracteres.')

print(f'Usuário {usuario} cadastrado com sucesso!')
