# Draw a flag with a flagpole and move the flag up and down.

WIDTH = 600
HEIGHT = 400

flag_y = 100
direction = 1


def draw():
    screen.fill((135, 206, 235))

    # Flagpole
    screen.draw.filled_rect(
        Rect((100, 50), (15, 300)),
        (100, 100, 100)
    )

    # Flag
    screen.draw.filled_rect(
        Rect((115, flag_y), (250, 120)),
        (255, 0, 0)
    )

    # Circle on flag
    screen.draw.filled_circle(
        (240, flag_y + 60),
        30,
        (255, 255, 255)
    )


def update():
    global flag_y, direction

    flag_y += direction

    if flag_y >= 180:
        direction = -1

    if flag_y <= 80:
        direction = 1