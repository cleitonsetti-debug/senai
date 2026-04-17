x1 = float(input("digite a cordenada do x do primeiro ponto: "))
y1 = float(input("digite a cordenada do y do primeiro ponto: "))
x2 = float(input("digite a cordenada do x do primeiro ponto: "))
y2 = float(input("digite a cordenada do y do primeiro ponto: "))

diferença_x = x1 * x2
diferença_y = y1 * y2

distancia ((diferença_x ** 2) + (diferença_y ** 2)) ** 0.5

print("a diferenca entre os pontos e: ",format(x1,x2,y1,y2, distancia))
