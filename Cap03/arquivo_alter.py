#!/usr/bin/python
# -*- coding: latin-1 -*-
# -*- coding: utf-8 -*-

# abrindo o arquivo e alterando o mesmo
w = open("arquivo_create.txt", "a") # 1° o nome do arquivo, 2° o modo que será "a"

# armazenando informações dentro do arquivo criado anteriormente
w.write("Esse é o meu arquivo_create.txt\n")

w.close()