import turtle

# Cria uma janela
window = turtle.Screen()

# Cria tartarugas
leonardo = turtle.Turtle()
leonardo.color('blue')

raphael = turtle.Turtle()
raphael.color('red')

donatello = turtle.Turtle()
donatello.color('purple')

michelangelo = turtle.Turtle()
michelangelo.color('orange')


def reg_polygon(cur_turtle, sides, side_len):
    angle = 360 / sides
    for n in range(sides):
        cur_turtle.forward(side_len)
        cur_turtle.left(angle)


def reg_star(cur_turtle, sides, side_len):
    angle = 180 - 180 / sides
    for n in range(sides):
        cur_turtle.forward(side_len)
        cur_turtle.left(angle)


reg_polygon(leonardo, 10, 100)
reg_polygon(raphael, 5, 200)

reg_star(donatello, 15, 75)
reg_star(michelangelo, 5, 500)

# Espera que o user feche a janela
window.mainloop()
