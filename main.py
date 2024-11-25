import pygame
from pygame.examples.testsprite import screen_dims

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

player_pos_x = screen.get_width() / 2
player_pos_y  = screen.get_height() / 2


#font
font  = pygame.font.Font('/Users/harshmishra/PycharmProjects/PACMAN/font/Pixeltype.ttf', 32)
dt = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("black")
    pygame.draw.circle(screen,"red",(player_pos_x,player_pos_y),40)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_pos_y -= 300 * dt
    if keys[pygame.K_a]:
        player_pos_x -=300*dt
    if keys[pygame.K_s]:
        player_pos_y += 300 * dt
    if keys[pygame.K_d]:
        player_pos_x += 300*dt

    coordinates = (player_pos_x , player_pos_y)

    text = font.render(f"{coordinates}",True,"blue")
    textRect = text.get_rect(center=(400, 250))
    screen.blit(text, textRect)
    if player_pos_y > 790:
        player_pos_y = 0
    elif player_pos_y < -10:
        player_pos_y = 780
    if player_pos_x > 1290:
        player_pos_x = 0
    elif player_pos_x < -10:
        player_pos_x = 1290

    pygame.display.flip()
    dt = clock.tick(60) / 1000
