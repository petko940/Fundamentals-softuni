class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        pi = Circle.__pi
        r = self.radius
        return pi * (r ** 2)

    def calculate_area_of_sector(self, angle):
        pi = Circle.__pi
        r = self.radius
        return angle / 360 * pi * (r ** 2)


circle = Circle(5)
angle = 90

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")
