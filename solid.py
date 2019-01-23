# solid principles of OOP

# Single responsibility

"""
The Single Responsibility Principle requires that each class is responsible for only one thing.
More specifically, a class should have only one reason to change
It"s very easy to find yourself in the situation where you are adding a method to a
class because there isn’t really anywhere else it fits, or maybe it could fit in any of two or
three classes.
"""

# Given a class which has two responsibilities


class Rectangle(object):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def draw(self):
        # Do some drawing
        pass

    def area(self):
        return self.width * self.height


"""
We have a trivial Rectangle class which is responsible for both the geometric properties
 of the rectangle and also the GUI representation of it. This may be acceptable early
 in the development of the system but later on we realise we need to split the responsibility
 because the GUI representation needs factoring out. So we simply split the class:

"""

# We can split it into two...


class GeometricRectangle(object):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class DrawRectangle(object):
    def draw(self):
        # Do some drawing
        pass


"""
The issue with this principle is that in case you want to add a function
you will need to add a class that achieves which can lead to a lot of classes
about the same object
"""


# Open/Closed Principle

"""
Software entities (classes, modules, functions, etc) should be open for extension,
but closed for modification.
At first reading this statement may seem contradictory, but in any OOP language
this is trivially achieved through abstraction.
The base (or abstract) class is closed for modification and we implement concrete
subclasses in order to modify their behaviour. This is also important in Python
and again easy to follow.
"""


class Geometryshapes(object):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self, shape):
        if shape == "Square":
            area = self.width ** 2
            return area
        elif shape == "Rectangle":
            area = self.width * self.height
            return area
        return


"""
this class violates the open closed principle since
if for example we want to calculate the area of another shape we
will need to add another elif
"""
# this is how we can solve the


class Square(object):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width ** 2


class Rectangles(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width


"""
How do ensure every class of a shape created has an area method
We an do that by having an abstract class that each of the shapes inherits from
this class will have a method area so that every subsequents shape class
implements the area method in its structure.
"""

# Mixins

"""
Python allows for multiple inheritance of concrete subclasses. This allows us to
create 'mix-ins', multiple classes which each provide specific functionality,
and are intended to be inherited together to create a ‘mixed’ class.
The benefits are obviously that it allows you to ensure your classes retain only
one responsibility (as discussed above) while giving you powerful options for
modifying the properties of your base class.
"""

# Monkey-Patching
"""
In Python we are able to change the functionality of any method, class or function
at will. We can even add methods to classes (or individual instances!) at run-time.
For example, imagine we had created a GeometricRectangle using our previous example,
but in order to make it fit into a badly designed API which insisted on the object
having a name() attribute we might consider the following solution:
"""

# example
shape = GeometricRectangle(2, 5)


def name():
    return "I'm a rectangle"


shape.name = name
print(shape.name())  # Prints: I'm a rectangle


# Generic functions (using overloading)
"""
Using the @ overload decorator it is possible to create function overloads which
perform different functionality for different arguments[8].In my mind this is
slightly better than using isinstance  switch behaviour but still doesn’t
feel very Pythonic. It’s also not possible to use this for methods,only functions.
"""

# Liskov Substitution Principle
"""
Objects in a program should be replaceable with instances of their base types
without altering the correctness of that program.
The Liskov Substitution Principle basically states that any subclass should be
replaceable with its parent class. Again this is a simple enough principle which
throws up some quite subtle difficulties in implementation.
"""

# Example


class RectangleBase(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class SquareDerived(RectangleBase):
    def __init__(self, width, height):
        RectangleBase.__init__(self, width, height)
        self.width = self.height


s = SquareDerived(5, 9)
print(s.area())  # 81
r = RectangleBase(6, 7)
print(r.area())  # 42


# Interface Segregation Principle
"""
Many client-specific interfaces are better than one general-purpose interface.
This principle aims to ensure that clients are not forced to depend on methods which they do not use.
In Python we are free to inherit from multiple concrete classes, and this is precisely
the purpose of the mix-ins discussed above – to provide multiple clients specific behaviours.
"""


# Dependency Inversion Principle
"""
High-level modules should not depend on low-level modules. Both should depend on
abstractions. b. Abstractions should not depend on details. Details should depend
on abstractions.
The Dependency Inversion Principle basically states that even high level modules
should depend upon abstractions, not low level classes
I think we get this for free with good Python: the answer to this problem in [2]
is the use of interfaces to define high-level abstractions which the details need
to implement; we go one better than that and only rely on the given object having
the required properties.
"""
