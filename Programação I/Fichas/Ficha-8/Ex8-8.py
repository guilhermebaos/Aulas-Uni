import turtle

# Cria uma janela
window = turtle.Screen()

# Cria uma tartaruga chamada alex
alex = turtle.Turtle()
alex.speed(1000)

beggining = 200
alex.penup()
alex.left(180)
alex.forward(beggining)
alex.left(90)
alex.forward(beggining)
alex.left(90)
alex.pendown()


def triangle(lado):
    for _ in range(3):
        alex.forward(lado)
        alex.left(120)


def sierpinski(n, lado):
    if n == 0:
        triangle(lado)
        return
    lado /= 2
    sierpinski(n - 1, lado)
    alex.forward(lado)
    sierpinski(n - 1, lado)
    alex.forward(lado)
    alex.left(120)
    alex.forward(lado)
    sierpinski(n - 1, lado)
    alex.forward(lado)
    alex.left(120)
    alex.forward(lado * 2)
    alex.left(120)
    return


sierpinski(4, 500)
input()
