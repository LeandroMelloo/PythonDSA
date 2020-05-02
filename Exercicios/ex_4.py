# Escreva um programa que ordene uma lista numérica com três elementos.
lista = [3,2,1]
print(sorted(lista)) # função sorted - ordena uma lista

# Ordenando com o select sorted
lista1 = [-9, 80, 6, 2, 45, 2, -1, 22, 123, 456, 1000, 4, 6]

for i in range(len(lista1)):
    menor = i

    for j in range(i+1, len(lista1)):
        if lista1[j] < lista1[menor]:
            menor = j

    if lista1[i] != lista1[menor]:
        aux = lista1[i]
        lista1[i] = lista1[menor]
        lista1[menor] = aux

print(lista1) # [-9, -1, 2, 2, 4, 6, 6, 22, 45, 80, 123, 456, 1000]
