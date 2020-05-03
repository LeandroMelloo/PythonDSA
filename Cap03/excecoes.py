# tratando excessoes
a = 2
b = 0

try:
    calculo = a / b
    print(calculo)
except:
    print('Não é permitido divisão por 0')

# continua o programa
print(a/a) # 1.0