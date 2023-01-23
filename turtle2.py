import turtle
import random_rgb
import random
# .goto(x,y) - ajusta a posicao do pointer
''' criar desenho com mudanca de cor aleatoria no stamp'''

display = turtle.Screen()
display.bgcolor("Black")

catarina = turtle.Turtle()
catarina.shape("turtle")
catarina.color("#FFFFFF")
#funcao para gerar numero aleatorio e guardar na tuple rgb_hex = [0,0,0]
#esse rgb sera a cor nova do pointer para cada linha

def change_color():
    colore = ["#" + ''.join([random.choice('0123456789ABCDEF') for i in range(6)])]
    return colore
'''#muita chance de estar errdo

catarina.color(random_rgb()) 
print(catarina.color(random_rgb()))
'''
# funcao para desenhar

def desenhe(dist,angle,vezes):
    catarina.speed(0)
    for _ in range(vezes):
        catarina.forward(dist)
        catarina.penup()
        catarina.backward(dist)
        catarina.color(change_color())
        catarina.pendown()
        catarina.right(angle)




desenhe(360,0.5,720)

display.exitonclick()