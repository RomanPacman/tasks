class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height= height

    def area(self):
        print(self.width * self.height)

    def perimeter(self):
        print( (self.width + self.height) * 2)

    def is_square(self):
        print(self.width == self.height)

r = Rectangle(10, 5)
r.area()
r.perimeter()
r.is_square()