import turtle
# defina caracteristicas do pointer
wn = turtle.Screen()
wn.bgcolor("Silver")
alex = turtle.Turtle()
alex.shape("arrow")
alex.speed(0)
# defina o movimento para o desenho (linha por linha ou num loop)

for _ in range(360):
    alex.forward(200)
    alex.penup()
    alex.back(200)
    alex.pendown()
    alex.right(1)


# sempre finalize com exit on click para manter a tela
wn.exitonclick()

