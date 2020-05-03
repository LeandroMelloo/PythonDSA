import random

# random.randint() - gera numeros aleatorios
numero = random.randint(0, 10)
print(numero)

# random.seed(1) - força trazer o numero determinado, no caso 2
random.seed(1)
numero2 = random.randint(0, 10)
print(numero2)

# random.choice() - seleciona um numero de uma lista
lista = [-3, 55, 77, 4, 5, 9, 0]
numero3 = random.choice(lista)
print(numero3)