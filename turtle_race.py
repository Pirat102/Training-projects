import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "black", "grey"]

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Type a number of racers (2 - 10): ")
        if racers.isdigit():
            if int(racers) in range(2,11):
                return int(racers)
            else:
                print("Wrong number!")
        else:
            print("That's not a number!")

def race(colors):
    turtles = create_turtles(colors)
    winners = []
    completed = set()

    while len(winners) < len(turtles):
        for i, racer in enumerate(turtles):
            distance = random.randrange(1, 20)
            racer.forward(distance)
            x, y = racer.pos()
            if y >= HEIGHT / 2 :
                if racer not in completed:
                    winners.append(colors[i])
                    completed.add(racer)
    return winners

                
        

def create_turtles(colors):
    turtles = []
    space = WIDTH / (len(colors) +1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.shape("turtle")
        racer.color(color)
        racer.left(90)
        racer.penup()
        racer
        x = (-WIDTH / 2) + space * (i +1)
        racer.setpos(x, (-HEIGHT / 2) + 20)
        turtles.append(racer)
    return turtles



racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
winners = race(colors)

print("Finishing order:", winners)



