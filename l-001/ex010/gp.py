print("\n-=- Exercício 010 -=-")
print("Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias.\n")

#Programa:

cigarros_por_dia=int(input("cigarros pro dia:"))
anos=int(input("anos:"))
qnt_cigarros=(anos*365)*cigarros_por_dia
dias_perdidos=(qnt_cigarros*10)/1440
print(dias_perdidos,"dias")

#Fim do Programa.

print("\n--- Fim do Programa ---\n")
