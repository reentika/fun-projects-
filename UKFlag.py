import turtle
rly = turtle.Turtle()

# Comment: This was hard but really fun to do, it got really frustrating. At the end, I got it to work! With the exception of the lenghts of the red crosses :( But it just won't get right.

# Pensize ;)

rly.pensize(8)

# Blue Background

rly.penup()
rly.goto(0, 0)
rly.pendown()

rly.color("Navy")
rly.begin_fill()
for i in range(2):
    rly.forward(400)
    rly.right(90)
    rly.forward(220)
    rly.right(90)
rly.end_fill()

# White \
rly.penup()
rly.goto(0, 20)
rly.pendown()
rly.right(30)
rly.color("White")
rly.begin_fill()
rly.forward(470)
rly.right(90)
rly.forward(30)
rly.right(90)
rly.forward(470)
rly.right(90)
rly.forward(30)
rly.right(60)
rly.end_fill()

# White /
rly.penup()
rly.goto(406, -10)
rly.pendown()
rly.right(150)
rly.color("White")
rly.begin_fill()
rly.forward(465)
rly.right(90)
rly.forward(30)
rly.right(90)
rly.forward(465)
rly.right(90)
rly.forward(30)
rly.right(300)
rly.end_fill()

# Red \ A
rly.penup()
rly.goto(0, 5)
rly.pendown()
rly.right(30)
rly.color("Crimson")
rly.begin_fill()
rly.forward(220)
rly.right(90)
rly.forward(10)
rly.right(90)
rly.forward(220)
rly.right(90)
rly.forward(10)
rly.right(60)
rly.end_fill()

# Red \ B
rly.penup()
rly.goto(220, -115)
rly.pendown()
rly.right(30)
rly.color("Crimson")
rly.begin_fill()
rly.forward(205)
rly.right(90)
rly.forward(10)
rly.right(90)
rly.forward(205)
rly.right(90)
rly.forward(10)
rly.right(60)
rly.end_fill()

# Red / A
rly.penup()
rly.goto(380, -10)
rly.pendown()
rly.right(150)
rly.color("Crimson")
rly.begin_fill()
rly.forward(220)
rly.right(90)
rly.forward(10)
rly.right(90)
rly.forward(220)
rly.right(90)
rly.forward(10)
rly.right(300)
rly.end_fill()

# Red / B
rly.penup()
rly.goto(220,-110)
rly.pendown()
rly.right(150)
rly.color("Crimson")
rly.begin_fill()
rly.forward(230)

rly.right(90)
rly.forward(10)
rly.right(90)
rly.forward(230)
rly.right(90)
rly.forward(10)
rly.right(300)
rly.end_fill()



# White 1

rly.penup()
rly.goto(170, 1)
rly.pendown()

rly.color("White")
rly.begin_fill()
for i in range(2):
    rly.forward(50)
    rly.right(90)
    rly.forward(220)
    rly.right(90)
rly.end_fill()

# White -

rly.penup()
rly.goto(1, -90)
rly.pendown()

rly.color("White")
rly.begin_fill()
for i in range(2):
    rly.forward(400)
    rly.right(90)
    rly.forward(50)
    rly.right(90)
rly.end_fill()

# Red 1 

rly.penup()
rly.goto(180, 1)
rly.pendown()

rly.color("Crimson")
rly.begin_fill()
for i in range(2):
    rly.forward(30)
    rly.right(90)
    rly.forward(220)
    rly.right(90)
rly.end_fill()

# Red -

rly.penup()
rly.goto(1, -100)
rly.pendown()

rly.color("Crimson")
rly.begin_fill()
for i in range(2):
    rly.forward(400)
    rly.right(90)
    rly.forward(30)
    rly.right(90)
rly.end_fill()

'''
# White /

rly.penup()
rly.goto(400, 10)
rly.pendown()
rly.color("White")
rly.begin_fill()
rly.left(208)
rly.forward(460)
rly.left(90)
rly.forward(50)
rly.left(90)
rly.forward(460)
rly.end_fill()
'''
