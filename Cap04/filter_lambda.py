# filter

lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = filter(lambda i: i % 2 == 0, lista)

resultado = list(lista_pares)

print(resultado)