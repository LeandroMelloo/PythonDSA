############ variaveis ###########
b = 10
print(b) # 10 int

############ operadores aritmeticos ###########
"""
soma = +
subtração = -
divisão = /
multiplicação = *
potencia = **
modulo = %
int() = converte para inteiro
float() = converte para float
"""

########### operadores relacionais #############
"""
igualdade => ==
desigualdade => !=
maior => >
menor => <
maior ou igual => >=
menor ou igual => <=
"""

########### operadores de atribuição ###########

# atribuição
z = 10
print(z) # 10 int

# soma
z += 10
print(z) # equivale a z = z + 10 (10 + 10 = 20) int

# subtração
z -= 10
print(z) # equivale a z = z - 10 (20 - 10 = 10) int

# multiplicação
z *= 10
print(z) # equivale a z = z * 10 (10 * 10 = 100) int

# divisão
z /= 10
print(z) # equivale a z = z / 10 (100 / 10 = 10) float

# modulo
z %= 10
print(z) # equivale a z = z % 10 (100 % 10 = 0.0) float

# potencia
z = 2
z **= 2
print(z) # equivale a z = z ** 2 (2 ** 2 = 4) int

# divisão inteira
z //= 2
print(z) # equivale a z = z // 2 (4 // 2 = 2) int

########### operadores logicos ###########
"""
AND(E), se ambos operadores forem True, (x and y) é True
OR(OU), se alguns dos operadores forem True, (x or y) é True
NOT(NÃO), utilizado para reverter o estado da lógica, NOT (x and y) é False
"""

########### declaração multipla ###############
pessoa1, pessoa2, pessoa3 = "José", "João", "Maria"
print(pessoa1, pessoa2, pessoa3) # José João Maria

fruta1 = fruta2 = fruta3 = "laranja"
print(fruta1, fruta2, fruta3) # laranja, laranja, laranja

############# sintaxe error #####################
"""
1x = 10 (não pode)
x 1 = 10 (não pode)
x = 10 (pode)
x_1 = 10 (pode)
"""

############# Variaveis atribuidas a outras variáveis e ordem dos operadores #############
largura = 2
altura = 4

area = largura * altura
print(area) # area = 8

perimetro = 2 * largura + 2 * altura
print(perimetro) # perimetro = 12

############## operacoes com variaveis ###########
idade1 = 25
idade2 = 25
idade3 = 2
idade4 = 2

print(idade1 + idade2) # soma => 50
print(idade1 - idade2) # subtração => 0
print(idade1 * idade2) # multiplicação => 625
print(idade1 / idade2) # divisão => 1.0
print(idade1 // idade2) # divisão inteiro => 1
print(idade1 % idade2) # modulo (resto da divisão) => 0
print(idade3 ** idade4) # potencia => 4

############ concatenação de variaveis ###########
esposa = "Luciana"
marido = "Leandro"

casal = "Casal" + " " + esposa + " " + "e" + " " + marido + " " + "firme e forte."
print(casal) # Casal Luciana e Leandro firme e forte.

nome = "Luciana"
sobrenome = "Moreira"

nome_completo = nome + " " + sobrenome
print(nome_completo)