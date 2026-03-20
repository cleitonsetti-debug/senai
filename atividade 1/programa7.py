quant_broas = int(input("digite a quantidade de broas vendidas: "))
quant_pao = int(input("digite a quantidade de pao vendidas: "))

arrecadado = (quant_pao * 0.12) + (quant_broas * 1.50)
poupança = ( arrecadado * 0.10)

print("total de vendas de pao e broas foi: " ,arrecadado)
print("quantidade de dinhiro que ira para a poupança " ,poupança)
