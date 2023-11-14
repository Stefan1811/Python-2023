import math

class Shape:
    def area(self):
        pass
    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self,radius):
        self.radius=radius
    
    def area(self):
        return math.pi*self.radius*self.radius
    
    def perimeter(self):
        return 2*math.pi*self.radius

class Rectangle(Shape):

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2*(self.length+self.width)

class Triangle(Shape):

    def __init__(self,l1,l2,l3 ):
        self.l1=l1
        self.l2=l2
        self.l3=l3
    
    def area(self):
        semi_perimeter=(self.l1+self.l2+self.l3)/2
        area=math.sqrt(semi_perimeter*(semi_perimeter-self.l1)*(semi_perimeter-self.l2)*(semi_perimeter-self.l3))
        return area

    def perimeter(self):
        return self.l1+self.l2+self.l3

circle=Circle(7)
print(circle.perimeter())
print(circle.area())

rectangle=Rectangle(6,8)
print(rectangle.perimeter())
print(rectangle.area())

triangle=Triangle(6,7,8)
print(triangle.perimeter())
print(triangle.area())
