# função reduce
from functools import reduce

lista = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 33, 44]

soma = reduce(lambda x, y: x + y, lista)
print(soma) # 130