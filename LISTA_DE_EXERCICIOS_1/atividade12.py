salario = float(input("digite seu salrio atual: "))
x = salario * 0.15
aumento = salario + x
imposto = aumento * 0.08
salario_final = aumento - imposto

print("salario sem aumento erra", salario)
print(f"salario com aumento erra", aumento)
print(f"salario salario final e de:", salario_final)