# Crie um programa o qual o usuário insere a sua idade e é informado quantos anos faltam para ele chegar a idade mínima de se aposentar (65 anos)

idade = int(input('Qual a sua idade? '))
idade_aposentadoria = 65

anos_restantes = 65 - idade

print(f'Faltam {anos_restantes} anos para você se aposentar...')
