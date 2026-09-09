import pygame

pygame.init()

screen = pygame.display.set_mode((2560, 1664)) #2560 x 1664 px 

pygame.display.set_caption("My First Game")

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()