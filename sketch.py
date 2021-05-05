import pygame
from quadtree import Rectangle, QuadTree, Point
import random

pygame.init()

screen = pygame.display.set_mode((800,800))


boundary = Rectangle(200, 200 ,200 ,200)

qt = QuadTree(boundary, 4)

qt.insert(Point(12, 3))

for i in range(0,5):
     x = random.randrange(0, 800)
     y = random.randrange(0, 800)
     point_width = 2
     pygame.draw.circle(screen, pygame.Color("red"), (x,y), point_width)
    


while True:

    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break
    
    qt.insert()

    #qt.show(screen)
   
    pygame.display.flip()

pygame.quit()
