import math

x1 = float(input("Entre o valor x do ponto 1: "))
y1 = float(input("Entre o valor y do ponto 1: "))
x2 = float(input("Entre o valor x do ponto 2: "))
y2 = float(input("Entre o valor y do ponto 2: "))
xsub = x2 - x1
ysub = y2 - y1
distancia = math.sqrt(math.pow(xsub,2) + math.pow(ysub,2))
if distancia >= 10:
        print("longe")
else:
        print("perto")