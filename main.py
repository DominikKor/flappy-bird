import sys
import pygame
from random import randint
pygame.init()

size = width, height = 360, 640
speed = 1

screen = pygame.display.set_mode(size)

background_1 = pygame.image.load("assets/images/background.png")
background_2 = pygame.image.load("assets/images/background.png")
bird = pygame.image.load("assets/images/birdtest.png")
bird = pygame.transform.scale(bird, (60, 43))
pipe = pygame.image.load("assets/images/pipe.png")
pipe_2 = pygame.image.load("assets/images/pipe.png")

bird_rect = bird.get_rect()
bird_rect.y = height / 2
bird_rect.x = 50

background_1_rect = background_1.get_rect()
background_2_rect = background_2.get_rect()
background_2_rect.x = 360

pipe = pygame.transform.flip(pipe, False, True)
pipe_rect = pipe.get_rect()
pipe_rect.y = -100
pipe_rect.x = (2 / 3) * width
pipe_rect_2 = pipe_2.get_rect()
pipe_rect_2.y = pipe_rect.y + pipe_rect.height + 200
pipe_rect_2.x = pipe_rect.x

is_jump = False
jump_count = 0
before_pressed = pygame.key.get_pressed()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not before_pressed[pygame.K_SPACE]:
                is_jump = True
                jump_count += 11

    if is_jump:
        if jump_count >= 0:
            bird_rect.y -= (jump_count * abs(jump_count)) * 0.2
            jump_count -= 1
        else:
            is_jump = False
            jump_count = 0
    else:
        bird_rect.y += 2

    if bird_rect.y >= height - bird_rect.height or bird_rect.y <= 0:
        bird_rect.y = height / 2

    if background_1_rect.x <= -width:
        background_1_rect.x = 0
        background_2_rect.x = width

    background_1_rect.x -= 1
    background_2_rect.x -= 1

    if pipe_rect.x <= -pipe_rect.width:
        pipe_rect.x = width
        pipe_rect_2.x = width
        pipe_rect.y = randint(-200, 0)
        pipe_rect_2.y = pipe_rect.y + pipe_rect.height + 200

    pipe_rect.x -= 1
    pipe_rect_2.x -= 1
    
    before_pressed = pygame.key.get_pressed()

    screen.blit(background_1, background_1_rect)
    screen.blit(background_2, background_2_rect)
    screen.blit(bird, bird_rect)
    screen.blit(pipe, pipe_rect)
    screen.blit(pipe_2, pipe_rect_2)
    pygame.display.flip()
