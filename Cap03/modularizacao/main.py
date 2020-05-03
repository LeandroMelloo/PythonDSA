''' main - arquivo responsavel por chamar os outros arquivo
    gerando um apelido com a palavra reservada 'as'
'''
import aleatorio as a
import media as m

lista = a.gerarListaInt(5)
media = m.media(lista)
mediana = m.mediana(lista)
moda = m.moda(lista)

print(lista)
print("A média da minha lista é:", media)
print("A mediana da minha lista é:", mediana)
print("A moda da minha lista é:", moda)