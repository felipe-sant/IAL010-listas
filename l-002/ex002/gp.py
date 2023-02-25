print("\n-=- Exercício 002 -=-")
print("Determine se um ano é bissexto. Verifique no Google como fazer isso...\n")

#Programa:

from calendar import isleap
ano = int(input("ano: "))
if isleap(ano):
    print("bissexto!")
else:
    print("não é bissexto")


#Fim do Programa.

print("\n--- Fim do Programa ---\n")
