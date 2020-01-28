import pygame

# Initialize the pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Dropping Hearts")
icon = pygame.image.load('img/Dropping-Hearts.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('img/girl.png')
playerX = 370
playerY = 480


def player():
    screen.blit(playerImg, (playerX, playerY))


# Game Loop makes the game run always and doesn't close down
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((255, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()

