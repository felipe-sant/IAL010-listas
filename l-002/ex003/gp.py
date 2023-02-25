print("\n-=- Exercício 003 -=-\n")

#Programa:

peso=float(input("peso do peixe: "))
if peso > 50:
    valor=(peso-50)*4
    print("\nO peso excedeu o limite estabelecido, logo você recebera uma multa!")
else:
    valor=0
    print("\nO peso esta dentro dos conformes estabelecido pelo regulamento de normas de São Paulo.")
print(f"valor da multa: R$ {valor}")

#Fim do Programa.

print("\n--- Fim do Programa ---\n")
