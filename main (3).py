

#Imports

import turtle
import random

#Screen Setup + Defining Turtles
s = turtle.Screen()
s.setup(315, 315)
s.screensize(300, 300)
s.bgcolor("silver")
s.tracer(0)
s.bgpic("sky.gif")

w, h = s.screensize()

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()
t5 = turtle.Turtle()
t6 = turtle.Turtle()
t7 = turtle.Turtle()
t8 = turtle.Turtle()
t8.hideturtle()

turtles = ["t1", "t2", "t5"]

# Position Variabels
x = -150
y = 0
x1 = 0
y1 = -150
y5 = 100
x5 = 20

#Dictionaries

game_objects = [{
    "t": t1,
    "x": x,
    "y": y,
    "radius": 10,
    "image": "crow1.gif",
    "type": "enemy",
    "speed": 0.3
}, {
    "t": t5,
    "x": x,
    "y": y,
    "radius": 10,
    "image": "crow2.gif",
    "type": "enemy",
    "speed": 0.5
}, {
    "t": t3,
    "x": x,
    "y": y,
    "radius": 10,
    "image": "crow3.gif",
    "type": "enemy",
    "speed": 0.9
},{
    "t": t4,
    "x": random.randint(-150,150),
    "y": random.randint(-150,150),
    "radius": 15,
    "image": "coin.gif",
    "type": "points"
}]
characters = {
    "t": t2,
    "x": x1,
    "y": y1,
    "radius": 15,
    "image": "charcter1.gif",
    "type": "character",
    "speed": 5
}
s.addshape(characters["image"])
t2.shape(characters["image"])
t2.penup()
t2.goto(x1, y1)
t2.pendown()

# Global variable

game_values = {
    'score': 0,
    'lives_remaining': 3,
    'current_level': 1,
}

#Defining Function To Write Starting Screen


def show_instructions():
    ''' To show the start screen '''
    t6.hideturtle()
    t6.penup()
    t6.color("navy")
    t6.goto(0, 120)
    t6.pendown()
    t6.write("Sky Pig", align="center", font=('Arial', 20, 'bold'))
    t6.penup()
    t6.sety(t6.ycor() - 60)
    t6.pendown()
    t6.write("Try to make it to the other side",
             align="center",
             font=('Arial', 12, 'bold'))
    t6.penup()
    t6.sety(t6.ycor() - 20)
    t6.pendown()
    t6.write("without hitting a bird",
             align="center",
             font=('Arial', 12, 'bold'))
    t6.penup()
    t6.sety(t6.ycor() - 50)
    t6.pendown()
    t6.write("Press Space to start the game",
             align="center",
             font=('verdana', 12, 'bold'))


#Defining A Function To Write Game Data: (Score,Lives,Level)

def game_data():

    t7.hideturtle()
    t7.penup()
    t7.color("navy")
    t7.goto(-145, 120)
    t7.pendown()
    t7.write('Score:' + str(game_values['score']),
             font=('Arial', 12, 'bold'))
    t7.penup()
    t7.goto(-35, 120)
    t7.pendown()
    t7.write('Lives:' + str(game_values['lives_remaining']),
             font=('Arial', 12, 'bold'))

    t7.penup()
    t7.goto(75, 120)
    t7.pendown()
    t7.write('Level:' + str(game_values['current_level']),
             font=('Arial', 12, 'bold'))

#Defining Main Function That Controls All Moving Objects And Game Logic

def animations():

    game_data()
    #Function To Move Character Right
    def move_right():
        t2.penup()
        t2.forward(characters["speed"])
        t2.pendown()
    
    #Function To Move Character Left
    def move_left():
        t2.penup()
        t2.backward(characters["speed"])
        t2.pendown()

    #Function To Move Character Up
    def move_up():
        t2.up()
        t2.right(90)
        t2.forward(characters["speed"])
        t2.left(90)
        t2.pendown()
        
    #Function To Move Character Down
    def move_down():
        t2.up()
        t2.left(90)
        t2.forward(characters["speed"])
        t2.right(90)
        t2.pendown()

    #Command to run functions according to keys pressed
    s.onkeypress(move_down, "Up")
    s.onkeypress(move_up, "Down")
    s.onkeypress(move_left, "Left")
    s.onkeypress(move_right, "Right")
    s.listen()

    #Defining Location Variables
    x = -150
    y = -10
    y5 = 100
    x5 = 20
    x3 = -150
    y3 = -100

    #Defining function that determines random location for coin
    def coin_location():
      s.addshape(game_objects[3]["image"])
      t4.shape(game_objects[3]["image"])
      t4.goto(random.randint(-150,150),random.randint(-150,150))
    
    coin_location()
    
    #Adding images from dictionary to screen
    for obj in game_objects:
        if (obj["type"] == "enemy"):
        
          img = obj["image"]
          t = obj["t"]

          s.addshape(img)
          t.shape(img)

    game_state = "play"
    
    #Moving Enemies Across The Screen
    while (game_state != "over"):

        for obj in game_objects:

            img = obj["image"]
            t = obj["t"]

            s.addshape(img)
            obj["t"].clear()

            if (obj["type"] == "enemy"):
                x5 = x5 - game_objects[0]["speed"]
                x = x + game_objects[1]["speed"]
                x3 = x3 + game_objects[2]["speed"]

            if t1.xcor() > 150:
                x = -150
                t1.penup()

                t1.goto(x, y)
                t1.pendown()

            elif t5.xcor() < -150:
                x5 = 150
                t5.penup()

                t5.goto(x5, y5)
                t5.pendown()
            elif t3.xcor() > 150:
              x3 = -150
              t3.penup()
              t3.goto(x3,y3)
              t3.pendown
            
            else:
                t1.goto(x, y)
                t5.goto(x5, y5)
                t3.goto(x3,y3)


        #Code To Detect Collisions Between Objects

        #Enemy 1 & Character
        distance1 = t1.distance(t2)
        #Enemy 2 & Character
        distance2 = t5.distance(t2)
        #Enemy 2 & Character
        distance3 = t3.distance(t2)
        #Coin & Character
        distance_coin = t4.distance(t2)
        
        #Conditional Statments To Reduce Amount of Lives if Collision Occurs
        if (distance1 <= game_objects[0]["radius"] + characters["radius"]):
            game_values["lives_remaining"] -= 1
            t2.penup()
            t2.goto(x1, y1)
            t2.pendown()
        elif (distance2 <= game_objects[1]["radius"] + characters["radius"]):
            game_values["lives_remaining"] -= 1
            t2.penup()
            t2.goto(x1, y1)
            t2.pendown()
        elif (distance3 <= game_objects[2]["radius"] + characters["radius"]):
          game_values["lives_remaining"] -= 1
          t2.penup()
          t2.goto(x1,y1)
          t2.pendown()
       
        #Conditional Statment to Determine Amount of Points Earned

        elif (distance_coin <= game_objects[3]["radius"] + characters["radius"]):

          game_values["score"] += 50
          t7.clear()
          game_data()
          t4.goto(1000,1000)

        s.update()
        t6.clear()
       
        #Conditional Statment to Change Enemy Speed as Level Increases

        if (t2.ycor() > 150):
            game_values["current_level"] = game_values["current_level"] + 1
            t7.clear()
            game_data()
            game_objects[0] ["speed"] = game_objects[0] ["speed"] + 0.2
            game_objects[1] ["speed"] = game_objects[1] ["speed"] + 0.2
            game_objects[2] ["speed"] = game_objects[2] ["speed"] + 0.2
            coin_location()
            
            t2.penup()
            t2.goto(0, -150)
            t2.penup
        
        #Defining Function to Display End Screen

        def end_screen():
          
          s.bgcolor("black")

          t7.hideturtle()
          t7.penup()
          t7.color("Red")
          t7.goto(0, 120)
          t7.pendown()
          t7.write("GAME OVER", align="center", font=('Arial', 20, 'bold'))
          t7.penup()
          t7.goto(0, 60)
          t7.pendown()
          t7.write('Level:' + str(game_values['current_level']),
                  font=('Arial', 12, 'bold'))
          t7.penup()

          t7.goto(-100, 60)
          t7.pendown()
          t7.write('Score:' + str(game_values['score']),
                  font=('Arial', 12, 'bold'))

        #Controls Amount of Lives & End Screen
        if game_values["lives_remaining"] == 2:
            t7.clear()
            game_data()
        elif game_values["lives_remaining"] == 1:
            t7.clear()
            game_data()
        elif game_values["lives_remaining"] == 0:
            game_state = "over"
            s.clear()
            end_screen()
            

def main():
  show_instructions()

  
  s.onkeypress(animations, "space")

  s.listen()

main()
