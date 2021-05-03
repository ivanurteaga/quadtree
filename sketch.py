import pygame

# boundary = Rectangle(200, 200 ,200 ,200)

# qt = QuadTree(boundary)

pygame.init()

screen = pygame.display.set_mode((1000,800))


while True:

    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

pygame.quit()
