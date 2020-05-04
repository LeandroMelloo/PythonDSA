# zip - vai compactar estas duas listas, concatenando elas
lista1 = [1, 2, 3, 4, 5]
lista2 = ["abacate", "bola", "cachorro", "dinheiro", "elefante"]
lista3 = ["verde", "azul", "feliz", "limpo", "grande"]

valores = zip(lista1, lista2, lista3)

for numero, nome, valor in valores:
    print(numero, nome, valor)