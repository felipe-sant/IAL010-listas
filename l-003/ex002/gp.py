print("\n-=- Exercício 002 -=-")
print("Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.\n")

#Programa:

nome=str(input("Nome de Úsuario: "))
senha=str(input("Senha: "))
while senha != nome:
    senha=str(input("Senha: "))

#Fim do Programa.

print("\n--- Fim do Programa ---\n")
