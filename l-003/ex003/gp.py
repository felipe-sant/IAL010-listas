print("\n-=- Exercício 003 -=-\n")

#Programa:

a=int(80000)
b=int(200000)
ano=0
while a<b:
    a=a+(a*0.03)
    b=b+(b*0.015)
    ano+=1
print(f"O número de anos necessarios para a Cidade A ultrapassar a Cidade B é de {ano}")

#Fim do Programa.

print("\n--- Fim do Programa ---\n")
