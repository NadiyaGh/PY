import turtle

turtle.bgcolor("black")
colors = ["red","pink","purple","blue","green","yellow","orange"]

p = turtle.Pen()
i = 3

p.shape("turtle")
while i < 100:
    for j in range(len(colors)):
        p.pencolor(colors[j])
        p.width(1.8)
        z = (180 - (((i-2)*180) / i))
        for k in range(i):
            p.forward(70)
            p.left(z)
        i += 1

turtle.done()