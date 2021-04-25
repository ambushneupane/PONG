import pygame
import random

# setup
pygame.init()
clock = pygame.time.Clock()

# Main Screen
WIDTH, HEIGHT = 1000, 680
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG GAME")

# colors
RED = (255, 0, 0)
LIME = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
Navy = (0, 0, 128)
LIGHT_GREY = (200, 200, 200)

# Game Rectangles
ball_widht, ball_height = 30, 30
ball = pygame.Rect(int(WIDTH / 2 - ball_widht / 2), int(HEIGHT / 2 - ball_height / 2), 30,
                   30)  # (Left,Top, Width ,Height)

player_widht, player_height = 10, 140
player = pygame.Rect(int(WIDTH - player_widht * 2), int(HEIGHT / 2 - player_height / 2), player_widht, player_height)

opponent_widht, opponent_height = 10, 140
opponent = pygame.Rect(10, int(HEIGHT / 2 - 70), opponent_widht, opponent_height)

# Background features
BACKGROUND_COLOR = pygame.Color('grey12')

# Movements
ball_speed_X = 7 * random.choice((1, -1))
ball_speed_Y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7


def ball_restart():
    global ball_speed_X, ball_speed_Y
    ball.center = (WIDTH / 2, HEIGHT / 2)
    ball_speed_Y *= random.choice((1, -1))
    ball_speed_X *= random.choice((1, -1))


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= HEIGHT:
        player.bottom = HEIGHT


def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= HEIGHT:
        opponent.bottom = HEIGHT


def ball_animation():
    global ball_speed_X, ball_speed_Y
    ball.x += ball_speed_X
    ball.y += ball_speed_Y

    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_Y *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_X *= -1


# Game LOOP
running = True
while running:
    clock.tick(60)
    # Handling the event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()

    # Visulas
    SCREEN.fill(BACKGROUND_COLOR)
    pygame.draw.rect(SCREEN, LIGHT_GREY, player)
    pygame.draw.rect(SCREEN, LIGHT_GREY, opponent)
    pygame.draw.ellipse(SCREEN, LIGHT_GREY, ball)
    pygame.draw.aaline(SCREEN, LIGHT_GREY, (WIDTH / 2, 0), (
    WIDTH / 2, HEIGHT))  # IN First tuple (width/2) means at middle and 0 means starting heigt(from top)
    # Second tuple means where to end the line so Widht/2,height will be straight with frist tuple.

    # Updating the Screen
    pygame.display.flip()

pygame.quit()
