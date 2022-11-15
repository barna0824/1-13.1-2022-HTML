import turtle

ablak=turtle.Screen()
Eszti=turtle.Turtle()
ablak.bgcolor('green')
Eszti.shape('turtle')
Eszti.color('blue')

for i in range(1,13):
    Eszti.penup()
    Eszti.forward(100)
    Eszti.pendown()
    Eszti.forward(10)
    Eszti.penup()
    Eszti.forward(15)
    Eszti.pendown()
    Eszti.stamp()
    Eszti.penup()
    Eszti.backward(125)
    Eszti.right(30)



ablak.mainloop()
