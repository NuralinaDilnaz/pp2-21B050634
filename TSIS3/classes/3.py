class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width  = width

    def rectangle_area(self):
        return self.length*self.width
a = int(input())
b = int(input())
s = Rectangle(a, b)
print(s.rectangle_area())
 