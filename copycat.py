import turtle



# the yellow line
line1 = turtle.Turtle()
line1.pensize(5)
line1.color("yellow")
line1.shape("blank")
line1.goto(0,150)
line1.goto(-75,150)
turtle.bgcolor("purple")

# the white line
line2 = line1.clone()
line2.color("white")
line2.shape("circle")
line2.goto(-75,0)

#the greenline
line3=turtle.Turtle()
line3.color("green")
line3.pensize(10)
line3.shape("blank")
line3.goto(0,-150)
line3.goto(75,-150)

#the blue line
line4 = line3.clone()
line4.color("blue")
line4.shape("arrow")
line4.left(90)
line4.goto(75,0)

turtle.mainloop()
