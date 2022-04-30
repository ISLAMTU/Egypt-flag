from turtle import *

x=Turtle()
x.speed(10)
x.color('black','red')
x.begin_fill()
for i in range(2):
    x.forward(100)
    x.left(90)
    x.fd(200)
    x.left(90)
x.end_fill()

x.color('black','white')
x.goto(100,0)
x.begin_fill()
for i in range(2):
    x.forward(100)
    x.left(90)
    x.fd(200)
    x.left(90)
x.end_fill()

x.color('black','black')
x.goto(200,0)
x.begin_fill()
for i in range(2):
    x.forward(100)
    x.left(90)
    x.fd(200)
    x.left(90)

x.end_fill()    
    


print("Egypt")
done()