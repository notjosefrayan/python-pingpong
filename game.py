import pygame
import random
pygame.init()

screen= pygame.display.set_mode((1280, 720))
pygame.display.set_caption("0-0")

player1goals= 0
player2goals=0

ball_pos_x= 1280/2
ball_pos_y=720/2

player1_pos_x= 40
player1_pos_y=720/2
player2_pos_x=1240
player2_pos_y=720/2
length = 120

a = random.choice([-1,1])
b = random.choice([-1,1])

bewegung_x = 6 * b
bewegung_y = 6  * a

game=True
while game:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
            print("game finished")

    ball_pos_x+= bewegung_x
    ball_pos_y += bewegung_y

    if ball_pos_y-20 <= 0:
        bewegung_y *= -1
    if ball_pos_y+20 >= 720:
        bewegung_y *= -1

    keys=pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_pos_y -=6
    if keys[pygame.K_s]:
        player1_pos_y +=6
    if keys[pygame.K_UP]:
        player2_pos_y -=6
    if keys[pygame.K_DOWN]:
        player2_pos_y +=6

    screen.fill((0, 102, 255))
        
    ball=pygame.draw.circle(screen,"orange",[ball_pos_x,ball_pos_y],20)
    goal1=pygame.draw.line(screen,"red",[0,0],[0,720],20)
    goal2=pygame.draw.line(screen,"red",[1280,0],[1280,720],20)
    player1=pygame.draw.line(screen,(0, 204, 0),[player1_pos_x,player1_pos_y -length/2],[player1_pos_x,player1_pos_y +length/2], 10)
    player2=pygame.draw.line(screen,(0, 204, 0),[player2_pos_x,player2_pos_y -length/2],[player2_pos_x,player2_pos_y +length/2],10)

    if ball.colliderect(goal1):
        ball_pos_x = 1280/2
        ball_pos_y = 720/2
        player2goals += 1
    if ball.colliderect(goal2):
        ball_pos_x = 1280/2
        ball_pos_y = 720/2
        player1goals += 1
    if ball.colliderect(player1):
        bewegung_x *= -1
    if ball.colliderect(player2):
        bewegung_x *= -1
    pygame.display.set_caption(str(player1goals) + " : " + str(player2goals))

    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()