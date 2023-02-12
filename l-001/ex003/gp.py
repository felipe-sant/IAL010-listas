print("\n-=- Exercício 003 -=-")
print("Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.\n")

#Programa:

dias=int(input("dias:"))
horas=int(input("horas:"))
minutos=int(input("minutos:"))
segundos=int(input("segundos:"))

horas+=dias*24
minutos+=horas*60
segundos+=minutos*60

print(segundos)

#Fim do Programa.

print("\n--- Fim do Programa ---\n")
