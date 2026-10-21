# Write a Python program to create a class named Circle constructed by a radius and two methods to compute the area and the perimeter of a circle.

class Circle:
    def __init__(self,radius):
        self.radius=radius

    def parameter(self):
        return 2*3.14*self.radius
    def area(self):
        return 3.14*(self.radius**2)


circle1=Circle(12)
print("Area of Circle",circle1.area())
print("Parameter of Circle",circle1.parameter())
