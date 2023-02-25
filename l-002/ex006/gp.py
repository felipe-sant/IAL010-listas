print("\n-=- Exercício 001 -=-\n")

#Programa:

dinheiro_p_hora=float(input("Quanto você ganha por hora: "))
horas_trabalhadas=int(input("Horas trabalhadas no mês: "))
salario_bruto=dinheiro_p_hora*horas_trabalhadas
imposto_de_renda=salario_bruto*0.11
inss=salario_bruto*0.08
sindicato=salario_bruto*0.05
salario_liquido=salario_bruto-imposto_de_renda-inss-sindicato
print(f"Seu salário bruto foi de R$ {salario_bruto};")
print(f"por conta no imposto de renda de 11%, foi descontado R$ {imposto_de_renda}")
print(f"por conta do inss de 8%, foi descontado R$ {inss}")
print(f"por conta do sindicato de 5%, foi descontado R$ {sindicato}")
print(f"Seu salário final ficou de R$ {salario_liquido}")


#Fim do Programa.

print("\n--- Fim do Programa ---\n")
