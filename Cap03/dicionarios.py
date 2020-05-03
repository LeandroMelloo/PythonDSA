# dicionario
meu_dicionario = {'a': 'ameixa', 'b': 'bola', 'c': 'cachorro'}
print(meu_dicionario) # {'a': 'ameixa', 'b': 'bola', 'c': 'cachorro'} - imprime tudo
print(meu_dicionario['a']) # ameixa

# navegar pelo meu dicionario com o comando for
for chave in meu_dicionario:
    print(chave + ":" + meu_dicionario[chave]) # a:ameixa b:bola c:cachorro

# retornando todos os itens do meu dicionario, e convertendo em uma tupla
for i in meu_dicionario.items():
    print(i) # ('a', 'ameixa') ('b', 'bola') ('c', 'cachorro')

# retornando valores
for i in meu_dicionario.values():
    print(i) # ameixa bola cachorro

# retornando chaves
for i in meu_dicionario.keys():
    print(i) # a b c