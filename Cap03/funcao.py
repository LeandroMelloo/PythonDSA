# funcao_local
def soma(x, y):
    soma = x + y
    print(soma) # 3

soma(1, 2)

# funcao_global
itens = [1, 2, 3, 4, 5, 6]

def lista(lista):
    return lista

res = lista(itens)
print(res)

# utilizando duas operações com escopo global
def soma(x, y):
    return x + y

def multiplicacao(x, y):
    return x * y

s = soma(2, 2) # 4
m = multiplicacao(4, 2) # 8

operacao = soma(s, m)
print(operacao) # 12
