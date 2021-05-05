import pygame
import random

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
    
    def contains(self, point):
        return (point.x > self.x - self.w,
            point.x < self.x + self.w,
            point.y > self.y - self.h,
            point.y < self.y + self.h)

class QuadTree():
    def __init__(self, boundary, n):
        self.boundary = boundary
        self.capacity = n
        self.points = []
        self.divided = False

    def subdivide(self):
        nw = Rectangle(x + w/2, y - h/2, w/2, h/2)
        self.nw = QuadTree(nw, self.capacity)
        ne = Rectangle(x - w/2, y - h/2, w/2, h/2)
        self.ne = QuadTree(ne, self.capacity)
        sw = Rectangle(x - w/2, y + h/2, w/2, h/2)
        self.sw = QuadTree(sw, self.capacity)
        se = Rectangle(x + w/2, y + h/2, w/2, h/2)
        self.se = QuadTree(se, self.capacity)
        
        self.divided = True

    def insert(self, point):
        
        if self.boundary.contains(point) is not False:
            return

        if len(self.points) < self.capacity:
            self.points.append(point)
        elif self.divided is not False:
            self.subdivide()
        
        self.ne.insert(point)
        self.nw.insert(point)
        self.se.insert(point)
        self.sw.insert(point)


    def show(self, screen):
        pygame.draw.rect(screen, pygame.Color(255, 150, 75, 4) ,pygame.Rect( self.boundary.x, self.boundary.y, self.boundary.w * 2, self.boundary.h * 2))
        if self.divided is True:
            self.ne.show()
            self.nw.show()
            self.se.show()
            self.sw.show()
