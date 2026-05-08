quanti_blusas = int(input("digite a quantidade de blusas necessarias: "))
metros_totais = quanti_blusas * 120
novelos = metros_totais // 125

if metros_totais % 125 > 0:
        novelos += 1

print(f"total de novelos necessarios: {novelos} ")