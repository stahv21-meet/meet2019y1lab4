import turtle

turtle.shape("turtle")
finn=turtle.clone()
finn.shape("square")

finn.goto(100,0)
finn.goto(100,100)
finn.goto(0,100)
finn.goto(0,0)

turtle.shape("turtle")
trin=turtle.clone()
trin.shape("triangle")

trin.goto(-100,0)
trin.goto(-50,100)
trin.goto(0,0)

finn.goto(0,200)
id1 = finn.stamp()
finn.goto(200,200)
finn.clearstamp(id1)
turtle.maneloop()
