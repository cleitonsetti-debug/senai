nome = input("digite o seu nome: ")
idade = int(input("digite a sua idade: "))

if idade > 120:
    print("idade invalida : por favor, ")
else:

dias_de_vida = idade * 365
print("voce ja viveu: " , dias_de_vida , "de sua vida")