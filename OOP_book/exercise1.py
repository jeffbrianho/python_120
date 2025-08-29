# How do we create a class and an object in Python?

# Write a program that defines a class and creates two objects from that class. 
# The class should have at least one instance variable that gets initialized by the initializer.

# What class you create doesn't matter, provided it satisfies the above requirements.

class MyClass:

    def __init__(self, name):
        self.name = name
        type_name = type(self).__name__
        print(f'I am {name}, a {type_name}.')

macy = MyClass('Macy')
amanda = MyClass('Amanda')

