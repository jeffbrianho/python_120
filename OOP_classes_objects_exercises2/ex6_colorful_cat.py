# Colorful Cat

# Create a class named Cat that prints a greeting when the greet instance method is invoked.
#  The greeting should include the name and color of the cat. Use a class constant to define the color.

class Cat:

    COLOR = 'purple'

    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello! My name is {self.name} and I'm a {self.__class__.COLOR} cat!")

sophie = Cat('Sophie')
sophie.greet()


# Hello! My name is Sophie and I'm a purple cat!