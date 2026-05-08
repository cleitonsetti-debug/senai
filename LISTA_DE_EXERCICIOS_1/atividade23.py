altura_pessoa = float(input("digite sua altura: "))
sombra_pessoa = float(input("digite o comprimento da sua sombra: "))
sombra_predio = float(input("digiteo comprimento da sombra do predio: "))
altura_predio = (altura_pessoa * sombra_predio) / sombra_pessoa
print(f"a altura do predio é: {altura_predio} em metros") 