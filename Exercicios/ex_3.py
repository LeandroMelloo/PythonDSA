# Escreva um programa que resolva uma equação de segundo grau.

a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
 
delta = b**2 - 4*a*c
print(delta)
raiz_delta = delta
 
if raiz_delta < 0:
    print("Delta negativo")
else:
    x1 = (-b + raiz_delta)/2*a
    print(x1)
    x2 = (-b + raiz_delta)/2*a
    print(x2)
 
    print("As raízes são", x1, "e", x2)
