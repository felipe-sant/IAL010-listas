print("\n-=- Exercício 009 -=-")
print("Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.\n")

#Programa:

km=int(input("km:"))
dias=int(input("dias:"))
preco=(km*0.15)+(dias*60.0)
print("R$",preco)

#Fim do Programa.

print("\n--- Fim do Programa ---\n")
