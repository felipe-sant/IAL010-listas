print("\n-=- Exercício 001 -=-")
print("Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor, sem usar as funções max e min.\n")

#Programa:

import random
lista = random.sample(range(1,100), 10)
x = 0
num_maior = 0
num_menor = 101
while x < len(lista):
    if lista[x] > num_maior:
        num_maior = lista[x]
    if lista[x] < num_menor:
        num_menor = lista[x]
    x += 1
print(f"A lista de números são: \n{lista}")
print(f"O número maior é {num_maior}")
print(f"O número menor é {num_menor}")

#Fim do Programa.

print("\n--- Fim do Programa ---\n")
