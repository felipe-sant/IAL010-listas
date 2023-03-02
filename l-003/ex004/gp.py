print("\n-=- Exercício 004 -=-\n")

#Programa:

numero=int(input("n: "))
f1=1
f2=1

if numero==1 or numero==2:
    print("1")
else:
    x=3
    while x<=numero:
        f3=f1+f2
        f1,f2 = f2,f3
        x+=1
    print(f3)



#Fim do Programa.

print("\n--- Fim do Programa ---\n")
