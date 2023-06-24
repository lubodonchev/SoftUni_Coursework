class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        circumference = self.diameter * Circle.__pi
        return circumference

    def calculate_area(self):
        area = (self.diameter / 2) ** 2 * Circle.__pi
        return area

    def calculate_area_of_sector(self, angle):
        area_of_sector = (self.diameter / 2) ** 2 * angle * Circle.__pi/360
        return area_of_sector


circle = Circle(10)
c_angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(c_angle):.2f}")
