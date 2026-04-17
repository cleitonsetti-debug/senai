nome = input("digite o seu nome: ")
idade = int(input("digite a sua idade: "))

if idade > 120 or idade < 0:
    print("idade invalida : por favor, digite um valor menor ou igual a 120 ")
else:

    dias_de_vida = idade * 365
    print(f"ola {nome} , voce ja viveu cerca de: {dias_de_vida}") 