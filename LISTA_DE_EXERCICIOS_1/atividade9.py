preco_pequeno = 10
preco_media = 12
preco_grande = 15

quant_pequena = int(input("digite a quantidade de camisas pequenas: "))
quant_media = int(input("digite a quantidade de camisas media: "))
quant_grande = int(input("digite a quantidade de camisas grande: "))

valor_arecadado = quant_pequena *preco_pequeno + quant_media* preco_media + quant_grande* preco_grande 
print("o valor total todo foi",valor_arecadado)