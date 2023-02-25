print("\n-=- Exercício 005 -=-")
print("Faça um Programa que leia três números e mostre o maior e o menor deles\n")

#Programa:

n1=int(input("n1: "))
n2=int(input("n2: "))
n3=int(input("n3: "))
if n2<n1>n3:
    print(f"O número maior é o n1: {n1}")
    if n2>n3:
        print(f"O número menor é o n3: {n3}")
    elif n2<n3:
        print(f"O número menor é o n2: {n2}")
    else:
        print(f"O n2 e n3 são iguais e os menores números: {n2}")
elif n1<n2>n3:
    print(f"O número maior é o n2: {n2}")
    if n1>n3:
        print(f"O número menor é o n3: {n3}")
    elif n1<n3:
        print(f"O número menor é o n1: {n1}")
    else:
        print(f"O n1 e n3 são iguais e os menores números: {n1}")
elif n1<n3>n2:
    print(f"O número maior é o n3: {n3}")
    if n1>n2:
        print(f"O número menor é o n2: {n2}")
    elif n1<n2:
        print(f"O número menor é o n1: {n1}")
    else:
        print(f"O n1 e n2 são iguais e os menores números: {n1}")
else:
    print("Os números são iguais!")

#Fim do Programa.

print("\n--- Fim do Programa ---\n")
