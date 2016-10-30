#space Inavaders - Part 1
#Set up the screen
#Python 2.7
import turtle
import os

#set up the screen
wn = turtle.Screen()
wn.bgcolor("grey")
wn.title("Space Invaders")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

#create the player turtleplayer = turtle.Turtle()
player = turtle.Turtle()
player.color("red")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.lt(90) #setheading(90) #alternative

playerspeed = 15

#create the enemy
enemy = turtle.Turtle()
enemy.color("red")
enemy.shape("circle")
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemyspeed = 2

#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

#Define bullet's state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"


#Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def fire_bullet():
    #Declare bulletstate as a global if it needs changed
    global bulletstate
    if bulletstate == "ready":
        bulletstate = "fire"
        #Move the bullet to the just above te player
        x = player.xcor()
        y = player.ycor() +10
        bullet.setposition(x,y)
        bullet.showturtle()


#Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right , "Right")
turtle.onkey(fire_bullet,"space")

#Main game loop
while True:

    #Move the enemy
    x = enemy.xcor()
    x += enemyspeed
    enemy.setx(x)

    #Move the enemy back and down
    if enemy.xcor() > 280:
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
        enemyspeed *= -1

    if enemy.xcor() < -280:
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)
        enemyspeed *= -1

    #Move the bullet
    if bulletstate == "fire":
        y = bullet.ycor()
        y += bulletspeed
        bullet.sety(y)

    #check bullet borders
    if bullet.ycor() >275:
        bullet.hideturtle()
        bulletstate = "ready"

delay = raw_input("Press enter to finish")
