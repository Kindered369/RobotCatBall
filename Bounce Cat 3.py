import turtle

wn = turtle.Screen()
wn.title("Cat Ball Clicker by CoolCompany")
wn.bgcolor("white")

wn.register_shape("./assests/img/greenfloor.gif")
greenfloor = turtle.Turtle()
greenfloor.shape("./assests/img/greenfloor.gif")
greenfloor.speed(0)

wn.register_shape("./assests/img/catball-000.gif")

catball = turtle.Turtle()
catball.shape("./assests/img/catball-000.gif")
catball.speed(0)

clicks = 0

pen = turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.penup()
pen.goto(0, 200)
pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))

def clicked(x, y):
    global clicks
    clicks += 1 
    pen.clear()
    pen.write(f"Clicks: {clicks}", align="center", font=("Courier New", 32, "normal"))
    catball.penup()
    catball.goto(0,20)
    catball.goto(0,0)
catball.onclick(clicked)
    

wn.mainloop()

#waz gud