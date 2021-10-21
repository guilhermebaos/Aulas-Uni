import turtle

# Cria uma janela
window = turtle.Screen()

# Cria uma tartaruga chamada alex
alex = turtle.Turtle()
alex.speed(1)
alex.forward(50)
alex.left(90)
alex.forward(30)


# Fazer um círculo
steve = turtle.Turtle()
steve.color('red')

sides = 720
walk = 360 / sides
turn = 360 / sides

for i in range(sides):
    steve.forward(walk)
    steve.left(turn)



# Espera que o user feche a janela
window.mainloop()