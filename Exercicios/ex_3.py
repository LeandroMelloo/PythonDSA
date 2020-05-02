# Escreva um programa que resolva uma equação de segundo grau.

from math import sqrt

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))
 
delta = b**2 - 4*a*c
raiz_delta = sqrt(delta)
 
if raiz_delta < 0:
    print("Delta negativo")
else:
    x1 = (-b + raiz_delta)/2*a
    x2 = (-b - raiz_delta)/2*a
 
    print("As raízes são", x1, "e", x2)
