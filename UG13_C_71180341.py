import turtle

s = turtle.Screen()
t = turtle.Turtle()
s.bgcolor("black")

#i-nggrid
t.pensize(20)
t.color("pink")
t.forward(100)
t.backward(200)
t.forward(100)
t.right(90)
t.forward(150)
t.left(90)
t.forward(100)
t.backward(200)

#L-anggida
t.pensize(20)
t.color("pink")

t.right(90)
t.forward(100)

t.left(90)
t.forward(100)

#for 1
t = turtle.Turtle()
t.pensize(10)
t.color("pink")
t.penup()
t.goto(0,-130)
t.pendown()
t.right(90)
t.forward(80)
t.right(90)
t.forward(25)
t.right(180)
t.forward(50)
t.penup()
t.goto(0,-130)
t.pendown()
t.left(220)
t.forward(30)
