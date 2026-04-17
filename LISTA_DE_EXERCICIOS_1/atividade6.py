peso = float(input("insira o peso :"))
preco_por_kg = 12
total = peso * preco_por_kg

while True:
    if peso <= 0 or peso >= 10:
        print("peso invalido: por favor digite um valor valido que esteja entre 0 e 10")
        peso = float(input("insira o peso :"))
    else: 
        break
total = peso * preco_por_kg

print(f"o total a pagar e : ",total )
