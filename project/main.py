# https://awari.com.br/funcao-recursiva-em-python-aprenda-a-criar-algoritmos-poderosos/#:~:text=Fibonacci%3A-,O%20que%20%C3%A9%20uma%20fun%C3%A7%C3%A3o%20recursiva%20em%20Python%3F,e%20id%C3%AAnticos%20ao%20problema%20original.

'''
Uma função recursiva é uma função que se chama a si mesma durante a sua própria execução. Isso pode ser usado para resolver problemas que podem ser divididos em problemas menores e idênticos ao problema original.

Aqui está um exemplo de uma função recursiva em Python que calcula o fatorial de um número:

Neste exemplo, a função fatorial chama a si mesma para calcular o fatorial de n-1 até que chegue a 0 ou 1, onde retorna 1. O resultado final é o produto de todos os números de n a 1.
'''

# def fatorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fatorial(n-1)


import time


def contagem_regressiva(n):
    if n == 0:
        print(n)
        time.sleep(2)
        print("Decolar!")
    else:
        print(n)
        time.sleep(2)
        contagem_regressiva(n-1)
        # colocar delay de 20 segundos


contagem_regressiva(10)