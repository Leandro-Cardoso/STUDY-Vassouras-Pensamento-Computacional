'''
4) Crie um programa que gere uma senha de forma aleatória de 6 caracteres. Deve conter numero, letra e símbolo.
'''

from random import choice, shuffle

def create_ascii_list(start_dec:int, stop_dec:int) -> list:
    '''Return a list of chars based on ASCII dec code.'''
    chars = []
    for i in range(start_dec, stop_dec + 1):
        chars.append(chr(i))
    return chars

letters = create_ascii_list(97, 122)
letters.extend(create_ascii_list(65, 90))
numbers = create_ascii_list(48, 57)
simbols = ['#', '*', '+', '-', '<', '>', '@', '_', '~']

n_letter = 3
n_number = 2
n_simbol = 1
n_password = n_letter + n_number + n_simbol

password = []

for i in range(n_password):
    if i + 1 <= n_letter:
        password.append(choice(letters))
    elif i + 1 <= n_letter + n_number:
        password.append(choice(numbers))
    elif i + 1 <= n_password:
        password.append(choice(simbols))

shuffle(password)
password = ''.join(password)

print('Senha:', password)
