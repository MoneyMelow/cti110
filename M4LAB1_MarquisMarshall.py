import turtle
win = turtle.Screen()
t = turtle.Turtle()

t.pensize(3)
t.pencolor('blue')
t.shape('turtle')



for i in range(4):
    t.forward(100)
    t.left(90)


t.right(60)
t.forward(100)
t.left(120)
t.forward(100)



win.mainloop()
 
