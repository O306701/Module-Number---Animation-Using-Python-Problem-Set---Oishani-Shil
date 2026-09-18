# This program animates a traffic light and a car that moves when the light is green.

WIDTH = 600
HEIGHT = 400

car_x = 50
car_y = 300

car_speed = 3

light = "red"

timer = 0


def draw():
    screen.fill("skyblue")

    # Road
    screen.draw.filled_rect(
        Rect((0, 280), (600, 120)),
        "gray"
    )

    # Road lines
    screen.draw.filled_rect(
        Rect((0, 335), (600, 5)),
        "white"
    )

    # Traffic light
    screen.draw.filled_rect(
        Rect((450, 50), (100, 210)),
        "black"
    )

    # Lights
    if light == "red":
        screen.draw.filled_circle((500, 90), 30, "red")
    else:
        screen.draw.filled_circle((500, 90), 30, "darkgray")

    if light == "yellow":
        screen.draw.filled_circle((500, 155), 30, "yellow")
    else:
        screen.draw.filled_circle((500, 155), 30, "darkgray")

    if light == "green":
        screen.draw.filled_circle((500, 220), 30, "green")
    else:
        screen.draw.filled_circle((500, 220), 30, "darkgray")

    # Car
    screen.draw.filled_rect(
        Rect((car_x, car_y), (90, 35)),
        "blue"
    )

    # Car roof
    screen.draw.filled_rect(
        Rect((car_x + 20, car_y - 20), (50, 20)),
        "blue"
    )

    # Car wheels
    screen.draw.filled_circle(
        (car_x + 20, car_y + 35),
        12,
        "black"
    )

    screen.draw.filled_circle(
        (car_x + 70, car_y + 35),
        12,
        "black"
    )


def update():
    global car_x, light, timer

    timer += 1

    # Change the traffic light every few seconds
    if timer >= 180:
        timer = 0

        if light == "red":
            light = "green"

        elif light == "green":
            light = "yellow"

        elif light == "yellow":
            light = "red"

    # Move the car when the light is green
    if light == "green":
        car_x += car_speed

    # Stop the car when the light is red or yellow
    else:
        car_x += 0

    # Put the car back at the beginning when it leaves the screen
    if car_x > WIDTH:
        car_x = -90