# Python - Inheritance
## General Concept Guidance:
* [Inheritance](./https://docs.python.org/3.4/tutorial/classes.html#inheritance)
### [0. Lookup](./0-lookup.py)
> Write a function that returns the list of available attributes and methods of an object
### [1. My list](./1-my_list.py)
> Write a class MyList that inherits from list
### [2. Exact same object](./2-is_same_class.py)
> Write a function that returns True if the object is exactly an instance of the specified class ; otherwise False
### [3. Same class or inherit from ](./3-is_kind_of_class.py)
> Write a function that returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False
### [4. Only sub class of](./4-inherits_from.py)
> Write a function that returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class ; otherwise False
### [5. Geometry module](./5-base_geometry.py)
> Write an empty class BaseGeometry
### [6. Improve Geometry](./6-base_geometry.py)
> Add to class BaseGeometry
> * Public instance method: def area(self): that raises an Exception with the message area() is not implemented
### [7. Integer validator](./7-base_geometry.py)
> Add to class BaseGeometry
> * Public instance method: def integer_validator(self, name, value)
### [8. Rectangle](./8-rectangle.py)
> Write a class Rectangle that inherits from BaseGeometry
> * nstantiation with width and height: def __init__(self, width, height)
### [9. Full rectangle](./9-rectangle.py)
> Add to Rectangle
> * the area() method implemented
> * print() should print, and str()
### [10. Square #1](./10-square.py)
> Square inherits from rectangle with:
> * Instantiation with size: def __init__(self, size)
> * the area() method implemented
### [11. Square #2](./11-square.py)
> Add to Square:
> * print() should print, and str()
### [100. My Integer](./100-my_int.py)
> Write a class MyInt that inherits from int
### [101. Can I?](./101-add_attribute.py)
> Write a function that adds a new attribute to an object if it’s possible
