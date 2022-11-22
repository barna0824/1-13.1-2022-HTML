import turtle

screen=turtle.Screen()
teknos=turtle.Turtle()
turtle.speed(100)


class Forma:
    def hatszog():
       for i in range(1,6):
         turtle.forward(100)
         turtle.right(144)
    def elore():
        turtle.penup()
        turtle.forward(650)
        turtle.right(144)
        turtle.pendown()


for i in range(0,6):
       Forma.hatszog()
       Forma.elore()




screen.mainloop()