class Circle:
    def __init__(self, radius):
        self.radius = radius


    def area_circle(self):
        PI = 3.14
        area = PI * (self.radius ** 2)
        return area

Area_circle = Circle(2)
area_01 = Area_circle.area_circle()
print(area_01)
