# Draw a square that bounces off all edges of the window.

WIDTH = 600
HEIGHT = 400

square_x = 100
square_y = 100

square_size = 50

speed_x = 4
speed_y = 3


def draw():
    screen.fill("white")
    screen.draw.filled_rect(
        Rect((square_x, square_y), (square_size, square_size)),
        "blue"
    )


def update():
    global square_x, square_y, speed_x, speed_y

    square_x += speed_x
    square_y += speed_y

    if square_x <= 0 or square_x + square_size >= WIDTH:
        speed_x = -speed_x

    if square_y <= 0 or square_y + square_size >= HEIGHT:
        speed_y = -speed_y