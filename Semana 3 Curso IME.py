x = 10
y = 20
z = 30
print(not y > 10 or not z > 10)

print("resposta 10")
a = 1
b = 2

print(a != 2 or b == 1)

####### Exucucao condicional (IF) #####
### boolean condition ###

#condicao = int(input("temperature "))
#if condicao > 100:
#    then_comando = True
#    danger = "high danger"
#    print(then_comando, danger)
#else:
#    then_comando = False
#    danger = "low danger"
#    print(then_comando,danger)

is_ready = True
if (is_ready):
    print("Certo")
### quadratic equasion conditional ###
import math

a = float(input("Entre o valor de 'a': "))
b = float(input("Entre o valor de 'b': "))
c = float(input("Entre o valor de 'c': "))


delta = b ** 2 - 4 * a * c
if delta == 0:
    x = (-b + math.sqrt(delta)) / (2 * a)
    print("a raiz desta equação é ", x)
else:
    if delta < 0:
        print("Esta equacao nao possue raizes reais")
    else:
        x = (-b + math.sqrt(delta)) / (2 * a)
        y = (-b - math.sqrt(delta)) / (2 * a)
        if x < y:
        print("as raízes da equação são ", x, "e",y)
        else:
        print("as raízes da equação são ", y, "e", x)



