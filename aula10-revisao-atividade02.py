'''
Questão 2: Análise de Temperatura Semanal
Uma estação meteorológica coleta dados de temperatura (em graus Celsius) ao longo da semana. Os registros são os seguintes:

dias_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
temperaturas = [22, 19, 21, 24, 24, 18, 17]

O meteorologista quer saber qual foi a maior temperatura registrada na semana e em que dia ocorreu. Escreva um código que identifica os dias com temperatura acima de 22 graus.
'''

dias_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
temperaturas = [22, 19, 21, 24, 24, 18, 17]

for dia in dias_da_semana:
    if temperaturas[dias_da_semana.index(dia)] == max(temperaturas):
        print(f'{dia} = {temperaturas[dias_da_semana.index(dia)]}°')
