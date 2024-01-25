import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
w = 1
h = 1
speed_x = 400 * [-1, 1][random.randint(0, 1)]
speed_y = 300 * [-1, 1][random.randint(0, 1)]
speed_vec = pygame.Vector2(speed_x, speed_y)

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
player_pos_1 = pygame.Vector2(60, screen.get_height() / 2)
player_pos_2 = pygame.Vector2(screen.get_width() - 60, screen.get_height() / 2)

first_time = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    player_pos_1_start = [*player_pos_1.copy()]
    player_pos_1_end = [*player_pos_1.copy()]
    player_pos_2_start = [*player_pos_2.copy()]
    player_pos_2_end = [*player_pos_2.copy()]
    player_pos_1_start[1] += 60
    player_pos_2_start[1] += 60
    player_pos_1_end[1] -= 60
    player_pos_2_end[1] -= 60
    player_pos_1_start, player_pos_1_end, player_pos_2_start, player_pos_2_end = tuple(player_pos_1_start), tuple(player_pos_1_end), tuple(player_pos_2_start), tuple(player_pos_2_end)
    
    screen.fill("#3c78d8")

    pygame.draw.line(screen, "#93c47d", player_pos_1_start, player_pos_1_end, 10)
    pygame.draw.line(screen, "#93c47d", player_pos_2_start, player_pos_2_end, 10)

    pygame.draw.line(screen, "red", pygame.Vector2(0, 0), pygame.Vector2(0, screen.get_height()), 20)
    pygame.draw.line(screen, "red", pygame.Vector2(screen.get_width(), 0), pygame.Vector2(screen.get_width(), screen.get_height()), 20)

    if player_pos.y < 35:
        h *= -1
    if player_pos.y > screen.get_height() - 35:
        h *= -1
    speed_vec = pygame.Vector2(speed_x * w * dt, speed_y * h * dt)
    player_pos += speed_vec
    pygame.draw.circle(screen, "orange", player_pos, 35)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        if player_pos_1.y > 60:
            player_pos_1.y -= 350 * dt
    if keys[pygame.K_s]:
        if player_pos_1.y < 660:
            player_pos_1.y += 350 * dt
    if keys[pygame.K_UP]:
        if player_pos_2.y > 60:
            player_pos_2.y -= 350 * dt
    if keys[pygame.K_DOWN]:
        if player_pos_2.y < 660:
            player_pos_2.y += 350 * dt

    pygame.display.flip()

    dt = clock.tick(60) / 1000

    first_time = 0

