#!/usr/bin/python
# -*- coding: latin-1 -*-
# -*- coding: utf-8 -*-

arquivo = open("arquivo.txt")
arquivo_texto_completo = open("arquivo_texto_completo.txt")
arquivo_texto_readline = open("arquivo_texto_readline.txt")

# função readlines() - le todo arquivo e armazena em uma lista
linhas = arquivo.readlines()
print(linhas) # ['Meu arquivo\n', 'Ola mundo']

# função read() - lê o arquivo completo
texto_completo = arquivo_texto_completo.read()
print(texto_completo) # Texto completo - Imprimindo o texto completo

# função realine() - lê uma linha
linhas_readline = arquivo_texto_readline.readline()
print(linhas_readline) # Arquivo readline

# imprimindo linha por linha com o laço de repetição for
for linha in linhas:
    print(linha) # Meu arquivo Ola mundo

# criando um arquivo
w = open("arquivo_create.txt", "w") # 1° o nome do arquivo, 2° o modo que será "w"

# armazenando informações dentro do arquivo criado anteriormente
w.write("Esse é o meu arquivo_create.txt")

