arquivo = open("seq3_fasta") # abrindo um arquivo

linhas = arquivo.readlines() # lendo um arquivo

multifasta = {} # dicionario

for linha in linhas:

    if linha[0] == ">":
        seq_atual = linha[1:].strip()
        multifasta[seq_atual] = ""
    else:
        multifasta[seq_atual] = multifasta[seq_atual] + linha.strip()

print(multifasta["seq3"])