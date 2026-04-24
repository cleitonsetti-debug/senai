quant_sanduiche = int(input("digite a quantidade de sanduiches a fazer: "))
peso_queijo = 50
peso_presunto = 50
peso_carne = 100

total_queijo = (quant_sanduiche *2 *peso_queijo)
total_presunto = (quant_sanduiche *2 *peso_presunto)
total_carne = (quant_sanduiche *2 *peso_carne)

print(f"para produzir{quant_sanduiche} voce precisa de: ")
print(f"- queijo {total_queijo}kg de queijo")
print(f"- presunto {total_presunto}kg de presunto")
print(f"- carne {total_carne}kg de carne")
