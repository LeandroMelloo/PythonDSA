minha_lista_string = ["abacaxi", "melancia", "abacate"]
print(minha_lista_string)

minha_lista_numerica = [1, 2, 3, 4, 5]
print(minha_lista_numerica)

minha_lista_mista = ["abacaxi", 3, -1, "Jose", True, 2.7, "Maria"]
print(minha_lista_mista)

# percorrendo a lista com o laço de repetição for
for itens in minha_lista_string:
    print(itens)

# pegando os valores pela posição
print(minha_lista_mista[3]) # Jose

# descartando os itens iniciais do array
print(minha_lista_mista[3:]) # ['Jose', True, 2.7, 'Maria']

# descartando os itens finais do array
print(minha_lista_mista[:4]) # ['abacaxi', 3, -1, 'Jose']

# retornando o tamanho de uma lista
print(len(minha_lista_mista)) # 7

# adicionando valores a minha lista
minha_lista_mista.append('Juca')
print(minha_lista_mista) # ['abacaxi', 3, -1, 'Jose', True, 2.7, 'Maria', 'Juca']

# verificando se um valor está na lista
if 'Leandro' in minha_lista_mista:
    print('Este valor está na minha_lista_mista')
else:
    print('Este valor não está na minha_lista_mista')

# eliminando redundancia da minha lista
del minha_lista_numerica[2:]
print(minha_lista_numerica) # [1, 2, 3, 4, 5] -> [1, 2]

# criando uma lista em branco
minha_lista_em_branco = []
print(minha_lista_em_branco)

# inserindo valores na minha lista em branco
minha_lista_em_branco.append('avião')
print(minha_lista_em_branco) # ['avião']

# ordenando uma lista com o metodo sort, que ordena a lista existente
minha_lista_sort = [230, 89, -2, 56, 7, 90, 76, 333, 7890, -9, 5]
minha_lista_sort.sort()
print(minha_lista_sort) # [-9, -2, 5, 7, 56, 76, 89, 90, 230, 333, 7890]

# ordenando uma lista com o metodo sorted, que ordena uma lista, porém é preciso criar uma variavel
minha_lista_sorted = sorted(minha_lista_sort)
print(minha_lista_sorted) # [-9, -2, 5, 7, 56, 76, 89, 90, 230, 333, 7890]

# ordenando uma lista de maneira decrescente
minha_lista_numerica.sort(reverse=True)
print(minha_lista_numerica) # [2, 1]

# revertendo uma lista
minha_lista_numerica.reverse()
print(minha_lista_numerica)# [1, 2]

# ordenando minha lista string
minha_order_lista_string = ['pessego', 'abacate', 'limão', 'ameixa', 'kiwi']
minha_order_lista_string.sort()
print(minha_order_lista_string)

