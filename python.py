tup1 = ("*")
print(tup1*10)
for i in range (10):
    print("    ",tup1,)
print(tup1*10)
print("     ")
for i in range(10):
    print("*",)
print(tup1*10)
print("   ")
import turtle
wn = turtle.Screen()
wn.setup(width=400, height=400)
red = turtle.Turtle()

def curve():
    for i in range(200):
        red.right(1)
        red.forward(1)

def heart():
    red.fillcolor('red')
    red.begin_fill()
    red.left(140)
    red.forward(113)
    curve()
    red.left(120)
    curve()
    red.forward(112)
    red.end_fill()

heart()
red.ht()
turtle.done()
for i in range (10):
    print(tup1,"      ",tup1)
print(tup1*10)