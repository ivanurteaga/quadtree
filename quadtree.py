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

class QuadTree():
    def __init__(self, boundary, n):
        self.boundary = boundary
        self.capacity = n
        self.points = []
        self.divided = False

    def subdivide():
        nw = Rectangle(x + w/2, y - h/2, w/2, h/2)
        self.nw = QuadTree(nw)
        ne = Rectangle(x - w/2, y - h/2, w/2, h/2)
        self.ne = QuadTree(nw)
        sw = Rectangle(x - w/2, y + h/2, w/2, h/2)
        self.sw = QuadTree(sw)
        se = Rectangle(x + w/2, y + h/2, w/2, h/2)
        self.se = QuadTree(se)
        
        self.divided = True

    def insert(point):
        if len(self.points) < self.capacity:
            self.points.append(point)
        elif self.divided is not False:
            self.subdivide()
            