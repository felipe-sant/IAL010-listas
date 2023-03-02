print("\n-=- Exercício 001 -=-")
print("Faça um programa que peça dois números inteiros e imprima a soma desses dois números.\n")

#Programa:

n1 = int(input("Digite um valor: "))
n2 = int(input("Digite outro valor: "))
if n1 < n2:
    n1,n2 =  n2,n1
resto = n1 % n2
while resto != 0:
    n1,n2 = n2,resto
    resto = n1 % n2
print(n2)

#Fim do Programa.

print("\n--- Fim do Programa ---\n")
