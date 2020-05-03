# Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.
n1 = int(input("Digite o primeiro número: "))
sinal = input("Digite o sinal: ")
n2 = int(input("Digite o segundo número: "))

# soma
if sinal == "+":
    op = n1 + n2

# subtracao
elif sinal == "-":
    op = n1 - n2

# divisao
elif sinal == "/":
    op = n1 + n2

# multiplicacao
elif sinal == "*":
    op = n1 * n2

# modulo
elif sinal == "%":
    op = n1 % n2

# exponenciacao
elif sinal == "**":
    op = n1 ** n2
 
else:
    print("Sinal inválido.")
 
print('Resultado: ', op)