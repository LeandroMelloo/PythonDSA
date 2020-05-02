# String
a = 'Leandro'
b = 'Luciana'

# '\n' => quebra de linha
concatenar = a + ' ' + 'e' + ' ' + b + '\n'
print(concatenar)

# vendo o tamanho da variavel concatenar com a função 'len', que recebe o valor de uma 'string'
tamanho = len(concatenar)
print(tamanho)

# retornando o valor da posição[]
print(concatenar[0]) # L
print(concatenar[1]) # e
print(concatenar[2]) # a
print(concatenar[3]) # n
print(concatenar[4]) # d
print(concatenar[5]) # r
print(concatenar[6]) # o

# retornando um pedaço da minha String
print(concatenar[0:7]) # Leandro

# ignorando a primeira letra
print(concatenar[1:]) # eandro e Luciana

# lower => imprime tudo minusculo
print(concatenar.lower()) # leandro e luciana

# upper => imprime tudo maiusculo
print(concatenar.upper()) # LEANDRO E LUCIANA

# função strip() => remove caracteres especiais
print(concatenar.strip()) # quebra de linhas

# função split() => converte a minha sequencia em uma lista
print(concatenar.split()) # ['Leandro', 'e', 'Luciana']

# função find() => busca a palavra dentro de uma sequencia
buscar = concatenar.find('Leandro')
print(buscar) # 0

print(concatenar[buscar:]) # Leandro e Luciana

# função replace() => substitui uma palavra da string
print(concatenar.replace('Luciana', 'Mello'))