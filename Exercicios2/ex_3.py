seq = input("Digite uma sequência: ")

arquivo = open("seq2_fasta", "w")

arquivo.write(">seq\n")
arquivo.write(seq)

arquivo.close()