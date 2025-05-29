class Triangle():
    def __init__(self, *args):
        if len(args) != 3:
            raise ValueError("Нужно передать ровно 3 стороны")
        else:
            self.sides = args
            self.side_a, self.side_b, self.side_c = args
            self.half_sum = sum(args)/2

    @staticmethod
    def is_valid(*args):
        if len(args) != 3:
            raise ValueError("Нужно передать ровно 3 стороны")
        else:
            perimeter = sum(args)
        for side in args:
            if side > perimeter-side:
                return False
        return True

    def area(self):
        if self.is_valid(*self.sides):
            from math import sqrt
            return sqrt(self.half_sum * (self.half_sum - self.side_a) * (self.half_sum - self.side_b) * (self.half_sum - self.side_c) )

    def description(self):
        return f"Triangle with sides: {', '.join(str(s) for s in self.sides)}"


# t = Triangle(3, 4, 5)
# print(t.is_valid(3, 4, 5))
# print(t.area())
# print(t.description())

class Person():
    counter = 0

    def __init__(self, name):
        self.name = name
        self.__class__.counter += 1
    @classmethod
    def how_many(cls):
        return cls.counter

    @classmethod
    def reset_counter(cls):
        cls.counter = 0

p1 = Person("Alice")
p2 = Person("Bob")
print(Person.how_many())
Person.reset_counter()
print(Person.how_many())