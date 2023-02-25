print("\n-=- Exercício 007 -=-\n")

#Programa:

#estou levando em conta que eu terei que comprar um balde de tinta inteiro caso falte.
metros=int(input("metros quadrados a serem pintados: ")) 
if metros > 0:
    tinta=1
    if metros > 54:
        while metros > 54:
            metros -= 54
            tinta += 1
    print(f"Você vai precisar de {tinta} baldes")
    print(f"Tendo que pagar R$ {tinta*80}")
else:
    print("Seus metros quadrados são igual ou menor que zero!")

#Fim do Programa.

print("\n--- Fim do Programa ---\n")
