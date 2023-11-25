'''
5 - Crie um programa que crie uma uma piramide como a do desenho abaixo. O usuário deverá digitar o número de linhas e o programa irá criar como no exemplo abaixo.

Digite o número de linhas da pirâmide: 10
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
'''

linhas = int(input('Digite o número de linhas da pirâmide: '))
estrelas = 1
espacos = linhas - 1

for i in range(1, linhas + 1):
    linha = ' ' * espacos + '*' * (estrelas)
    espacos -= 1
    estrelas += 2
    print(linha)
