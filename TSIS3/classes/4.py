class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x+=x
        self.y+=y

    def dist(self, x, y):
        a = pt.x - self.x
        b = pt.y - self.y
        return math.sqrt(a ** 2 + b ** 2)
