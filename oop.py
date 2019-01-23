"""
A simple movie  application to demonstrate the oop concepts
Abstraction:
Polymorphism:
Inheritance:
Encapsulation:
instances
instance variables ---any value instantiated by self
instance methods ---has instance as one of its parameters(self)
constructor the init method. initializes all the data for the object
self --- points to the object being created
class --- a blueprint
class vaiable --- Variable that all the objects have access to

Every class comes with pre-existing class variables:
-  __doc__ : gives a documentation of the class
- __name__ : The function’s name
- __module__ :The name of the module the function was defined in, or None if unavailable.
"""

# this example is a simple Movie system using inbuilt data types for storage
import webbrowser


class Movie(object):
    """
    This class provides a way to store movie related information.
    """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)


"""
Understanding inheritance
"""


class Parent(object):
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name- ", self.last_name)
        print("Eye Color- ", self.eye_color)


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(last_name, eye_color)
        self.number_of_toys = number_of_toys

    # The concept demonstrated here is called method overriding.
    def show_info(self):
        print("Last Name- ", self.last_name)
        print("Eye Color- ", self.eye_color)
        print("Number of toys- ", self.number_of_toys)
