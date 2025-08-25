from teja import Shape
class Circle(Shape):   # Subclass
    def __init__(self, radius):
        self.radius = radius
        return self.radius

    def area(self):   # Implementing abstract method
        return 3.14 * self.radius * self.radius

    # def perimeter(self):
    #     return 2 * 3.14 * self.radius

# s = Shape()  ❌ Error (cannot create object of abstract class)

