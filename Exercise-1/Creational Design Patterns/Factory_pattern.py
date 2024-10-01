class Shape:
    def draw(self):
        pass


class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"


class Square(Shape):
    def draw(self):
        return "Drawing a Square"


class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str) -> Shape:
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError("Unknown shape type")
shape_factory = ShapeFactory()
shape1 = shape_factory.create_shape("circle")
print(shape1.draw())  

shape2 = shape_factory.create_shape("square")
print(shape2.draw())  
