# função reduce
from functools import reduce

def soma(x, y):
    return x + y

lista = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 33, 44]

soma = reduce(soma, lista)
print(soma) # 130