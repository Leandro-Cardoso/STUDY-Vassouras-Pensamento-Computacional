'''
6 - Crie um programa que crie uma arvore de natal como no desenho abaixo utilizando apenas linha e asteriscos.

Digite a altura da árvore de Natal: 10
         *
        ***
       *****
      *******
     *********
    ***********
   *************
  ***************
 *****************
*******************
         |
         |
         |
        |||
'''

linhas = int(input('Digite o número de linhas da pirâmide: '))
estrelas = 1
espacos = linhas - 1

for i in range(1, linhas + 1):
    linha = ' ' * espacos + '*' * (estrelas)
    espacos -= 1
    estrelas += 2
    print(linha)

espacos = linhas - 2
for i in range(3):
    linha = ' ' * espacos + ' |'
    print(linha)

linha = ' ' * espacos + '|' * 3
print(linha)
