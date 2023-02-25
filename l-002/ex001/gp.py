print("\n-=- Exercício 001 -=-")
print("Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.\n")

#Programa:

n1=int(input("Lado 1: "))
n2=int(input("Lado 2: "))
n3=int(input("Lado 3: "))
if n1==n2 and n2==n3:
    print("\nEquilatero")
elif n1==n2 or n2==n3 or n1==n3:
    print("\nIsóseles")
else:
    print("\nEscaleno")

#Fim do Programa.

print("\n--- Fim do Programa ---\n")
