import turtle

# Screen() método para obter a tela
wn = turtle.Screen()

# criando objeto tess
tess = turtle.Turtle()


def triangle(x, y):
    # é usado para tirar a caneta
    tess.penup()

    # usado para mover o curso na posição x
    # e y
    tess.goto(x, y)

    # é usado para desenhar com a caneta
    tess.pendown()
    for i in range(3):
        # move o cursor 100 unidades
        # para frente
        tess.forward(100)

        # move o cursor 120 graus para esquerda
        tess.left(120)

        # Novamente, move o cursor 100 digitos
        # para frente
        tess.forward(100)


# função especial embutida para enviar corrente
# posição do cursor para o triângulo
turtle.onscreenclick(triangle, 1)

turtle.listen()

# deixa a tela
turtle.done()