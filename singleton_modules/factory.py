# Reviewing my knowledge on Python Design Patterns

class ShapeInterface:
    def draw(self): 
        pass


class Circle(ShapeInterface):
    def draw(self):
        print("Circle.draw")



class Square(ShapeInterface):
    def draw(self):
        print("Square.draw")


class ShapeFactory:
    def __init__(self, name):
        self.name = name

    # a static method to check if the shape is Circle or Square or something else
    @staticmethod
    def getShape(type):
        if type == 'Circle':
            return Circle()
        if type == 'Square':
            return Square()
        else:
            assert 0, 'Could not find shape ' + type

    # a class method to create a shape object by name.
    @classmethod
    def createShape(cls, name):
        return cls(name)
