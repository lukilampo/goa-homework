from turtle import *


#we want to paint a house

#step 1:  draw a square
speed(5)
width(5)
color("gold")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)


forward(200)
left(90)

forward(70)
color("brown")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup()
goto(200,200)
pendown()


color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

color("gold")
left(30)
forward(70)
left(90)
forward(60)
left(90)
forward(70)
left(90)
forward(30)
left(90)
forward(70)
left(90)
forward(30)
left(90)
forward(35)
left(90)
forward(60)
right(90)
forward(35)
right(90)
forward(200)

right(90)
forward(70)
right(90)
forward(60)
right(90)
forward(70)
right(90)
forward(30)
right(90)
forward(70)
right(90)
forward(30)
right(90)
forward(35)
right(90)
forward(60)




exitonclick()