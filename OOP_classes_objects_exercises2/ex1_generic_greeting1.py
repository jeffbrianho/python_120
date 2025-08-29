# Generic Greeting (Part 1)

# Create a class named Cat for which calling Cat.generic_greeting prints Hello! I'm a cat!

class Cat:

    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat!")

kitty = Cat()
kitty.generic_greeting()      # Hello! I'm a cat!
print(type(kitty).generic_greeting())

# Hello! I'm a cat!