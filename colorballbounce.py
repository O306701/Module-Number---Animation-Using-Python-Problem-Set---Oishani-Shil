# Draw a ball that bounces off all edges and changes color when it hits.

WIDTH = 600
HEIGHT = 400

ball_x = 300
ball_y = 200

ball_radius = 25

speed_x = 4
speed_y = 3

colors = ["red", "blue", "green", "purple"]
color_index = 0


def draw():
    screen.fill("white")
    screen.draw.filled_circle(
        (ball_x, ball_y),
        ball_radius,
        colors[color_index]
    )


def update():
    global ball_x, ball_y, speed_x, speed_y, color_index

    ball_x += speed_x
    ball_y += speed_y

    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        speed_x = -speed_x
        color_index = (color_index + 1) % len(colors)

    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        speed_y = -speed_y
        color_index = (color_index + 1) % len(colors)