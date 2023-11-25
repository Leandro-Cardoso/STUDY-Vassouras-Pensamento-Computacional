'''
2 - O programa inicia com \( n = 100 \) e aplica as regras do problema de Collatz:

- Se \( n \) é par, divida-o por 2.
- Se \( n \) é ímpar, multiplique por 3 e some 1.

O programa repete essas operações, atualizando o valor de \( n \) a cada passo, até que \( n \) se torne 1. A sequência resultante é:

\[ 100, 50, 25, 76, 38, 19, 58, 29, 88, 44, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1 \]

Esta é a sequência de Collatz começando em 100.
'''

n = 100
print(n)

while n > 1:
    if n % 2 == 0:
        n /= 2
    else:
        n = n * 3 + 1
    print(int(n))
