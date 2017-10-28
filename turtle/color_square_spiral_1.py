import turtle
t = turtle.Pen()
colors = ["turquoise", "red", "pink", "black"]
for x in range(200):
    t.pencolor(colors[x % 4])
    t.forward(x)
    t.left(91)
