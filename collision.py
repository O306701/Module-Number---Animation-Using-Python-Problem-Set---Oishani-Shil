# Make two circles move around the screen and bounce off the edges.
# If they collide, the blue circle moves to a random location.

import random

WIDTH = 600
HEIGHT = 400

red_x = 150
red_y = 200

blue_x = 450
blue_y = 200

radius = 25

red_speed_x = 3
red_speed_y = 2

blue_speed_x = -2
blue_speed_y = 3


def draw():
    screen.fill("white")

    screen.draw.filled_circle(
        (red_x, red_y),
        radius,
        "red"
    )

    screen.draw.filled_circle(
        (blue_x, blue_y),
        radius,
        "blue"
    )


def update():
    global red_x, red_y
    global blue_x, blue_y
    global red_speed_x, red_speed_y
    global blue_speed_x, blue_speed_y

    red_x += red_speed_x
    red_y += red_speed_y

    blue_x += blue_speed_x
    blue_y += blue_speed_y

    # Red ball bounces off the edges
    if red_x - radius <= 0 or red_x + radius >= WIDTH:
        red_speed_x = -red_speed_x

    if red_y - radius <= 0 or red_y + radius >= HEIGHT:
        red_speed_y = -red_speed_y

    # Blue ball bounces off the edges
    if blue_x - radius <= 0 or blue_x + radius >= WIDTH:
        blue_speed_x = -blue_speed_x

    if blue_y - radius <= 0 or blue_y + radius >= HEIGHT:
        blue_speed_y = -blue_speed_y

    # Check if the balls are touching
    distance_x = red_x - blue_x
    distance_y = red_y - blue_y

    distance_squared = distance_x ** 2 + distance_y ** 2

    if distance_squared <= (radius * 2) ** 2:
        blue_x = random.randint(radius, WIDTH - radius)
        blue_y = random.randint(radius, HEIGHT - radius)