# Python - Almost a circle
## In this project, you will review everything about Python:
* Import
* Exceptions
* Class
* Private attribute
* Getter/Setter
* Class method
* Static method
* Inheritance
* Unittest
* Read/Write file
* Serialization/Deserialization
* JSON
## Resources:
* [args/kwargs](./https://pythontips.com/2013/08/04/args-and-kwargs-in-python-explained/)
* [JSON Encoder and Decoder](./https://docs.python.org/3/library/json.html)
* [Python Test Cheatsheet](./https://www.pythonsheets.com/notes/python-tests.html)
### [Base Class](./models/base.py)
> * private class attribute __nb_objects = 0
> * class constructor: def __init__(self, id=None)
> * def to_json_string(list_dictionaries): returns the JSON string representation of list_dictionaries
> * def save_to_file(cls, list_objs): writes the JSON string representation of list_objs to a file
> * def from_json_string(json_string): returns the list of the JSON string representation json_string
> * def create(cls, **dictionary): returns an instance with all attributes already set
> * def load_from_file(cls): returns a list of instances
### [Rectangle Class](./models/rectangle.py)
> * class constructor: def __init__(self, width, height, x=0, y=0, id=None)
> * class Rectangle inherits from Base
> * def area(self): returns the area value of the Rectangle instance
> * def display(self): prints in stdout the Rectangle instance with the character #
> * def update(self, *args, **kwargs): assigns a key/value argument to attributes
> * def to_dictionary(self): returns the dictionary representation
### [Square Class](./models/square.py)
> * Class Square inherits from Rectangle
> * Class constructor: def __init__(self, size, x=0, y=0, id=None)
> * def update(self, *args, **kwargs) assigns a key/value argument to attributes
> * def to_dictionary(self): returns the dictionary representation
