contador = 1
soma = 0
while contador <= 5:
    salario = float(input(f"digite o salario do { contador } funcionario: "))
    contador += 1
    soma += salario
media = soma / 5
print("a media dos salariois dos 5 funcionarios e", media)
