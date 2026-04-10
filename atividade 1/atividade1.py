contador = 1
soma = 0
while contador <= 5:
    # Solicita o salário ao usuário e converte para número decimal (float)
    salario = float(input(f"digite o salario do { contador } funcionario: "))
    # Incrementa o contador para evitar um loop infinito e passar para o próximo funcionário
    contador += 1

    soma += salario
    # Após o fim do loop, calcula a média aritmética
media = soma / 5
print("a media dos salariois dos 5 funcionarios é:", media)
