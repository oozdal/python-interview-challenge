from factory import ShapeFactory

circle = ShapeFactory.createShape('Circle')
square = ShapeFactory.createShape('Square')

print(circle) # -> returns <factory.ShapeFactory object at 0x7feab146af40>
print(square) # -> returns <factory.ShapeFactory object at 0x7f90d55dd610>

print(circle.getShape('Circle')) # -> returns <factory.Circle object at 0x7feab15d35b0>
print(circle.getShape('Square')) # -> returns <factory.Square object at 0x7fae73ddd5b0>