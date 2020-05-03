import random

def gerarListaInt(tam):
    lista = []
    for itens in range(tam):
        lista.append(random.randint(0, tam))

    return lista