# Python - More Classes and Objects
## General Concept Guidance:
* [Object Oriented Programming](./https://python.swaroopch.com/oop.html)
### [0. Simple rectangle](./0-rectangle.py)
> Write an empty class Rectangle that defines a rectangle
### [1. Real definition of a rectangle](./1-rectangle.py)
> Write a class Rectangle that defines a rectangle by:
 * Private instance attribute: width
 * Private instance attribute: height
### [2. Area and Perimeter](./2-rectangle.py)
> Write a class Rectangle that defines a rectangle by:
 * Instantiation with optional width and height: def __init__(self, width=0, height=0):
 * Public instance method: def area(self): that returns the rectangle area
 * Public instance method: def perimeter(self): that returns the rectangle perimeter:
 ** if width or height is equal to 0, perimeter is equal to 0
### [3. String representation](./3-rectangle.py)
> Write a class Rectangle that defines a rectangle by:
 * print() and str() should print the rectangle with the character #: (see example below)
 ** if width or height is equal to 0, return an empty string
### [4. Eval is magic](./4-rectangle.py)
> Write a class Rectangle that defines a rectangle by:
 * repr() should return a string representation of the rectangle to be able to recreate a new instance by using eval()
### [5. Detect instance deletion](./5-rectangle.py)
> Write a class Rectangle that defines a rectangle by:
 * Print the message Bye rectangle... (... being 3 dots not ellipsis) when an instance of Rectangle is deleted
### [6. How many instances](./6-rectangle.py)
> Write a class Rectangle that defines a rectangle by:
 * Public class attribute number_of_instances:
 ** Initialized to 0
 ** Incremented during each new instance instantiation
 ** Decremented during each instance deletion
### [7. Change representation](./7-rectangle.py)
> Write a class Rectangle that defines a rectangle by:
 * Public class attribute print_symbol:
 ** Initialized to #
 ** Used as symbol for string representation
 ** Can be any type
### [8. Compare rectangles](./8-rectangle.py)
> Write a class Rectangle that defines a rectangle by:
 * Static method def bigger_or_equal(rect_1, rect_2): that returns the biggest rectangle based on the area
### [9. A square is a rectangle](./9-rectangle.py)
> Write a class Rectangle that defines a rectangle by:
* Class method def square(cls, size=0): that returns a new Rectangle instance with width == height == size