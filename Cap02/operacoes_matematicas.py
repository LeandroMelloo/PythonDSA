########### operações matematicas ##########

# soma
print(4 + 4)

# subtração
print(4 - 4)

# divisão
print(4 / 4)

# multiplicação
print(4 * 4)

# potencia
print(4 ** 3)

# modulo - resto
print(5 % 2)

########### função type ##########
print(type(5)) # int
print(type(4.0)) # float
print(type('ola')) #str

########## operações com números float ##########
print(3.3 + 3.4) # 6.999999999
print(type(3 + 3.4)) # float

print(4 + 4.0) # 8.0
print(type(3 + 3.4)) # float

print(4 + 4) # 8
print(type(4 + 4)) # int

print(4 / 2) # 2.0
print(type(4 / 4)) # float

print(4 // 2) # 2
print(type(4 // 4)) # int

print(4 / 2.0) # 2.0
print(type(4 / 4)) # float

print(4 // 2.0) # 2.0
print(type(4 // 4)) # int


########### conversão ##########
print(float(9)) # 9.0

'''
    => print(int(9.2)) # saída 9
    => print(int(9.6)) # saída 9

    no caso de conversão de 9.2 ou 9.6, o valor vai ser sempre 9,
    pois ele está retornado o valor inteiro, ou seja isso
    não é conversão, precisa ficar atento pois não existe arredondamento
    nem pra mais nem pra menos
'''
print(int(9.2)) # 9
print(int(9.6)) # 9

########## Hexadecimal e Binário ###########
print(hex(10)) # 0xa
print(bin(1)) # 0b1

########## funções abs, round e pow ##########
print(abs(-8)) # retorna o valor absoluto, saída = 8
print(round(8.334567890)) # retorna o valor aredondado, saída = 8
print(round(8.734567890)) # retorna o valor aredondado, saída = 9
print(round(8.334567890, 2)) # retorna o valor aredondado com duas casas decimais, saída = 8.33
print(round(8.736567890, 2)) # retorna o valor aredondado com duas casas decimais, saída = 8.74
print(pow(5, 3)) # potencia, saída = 125
