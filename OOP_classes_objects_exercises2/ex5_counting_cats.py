# Counting Cats

# Create a class named Cat that tracks the number of times a new Cat object is 
# instantiated. The total number of Cat instances should be printed when total 
# is invoked.

class Cat:
    total_cat = 0 

    def __init__(self):
        self.__class__.total_cat += 1

    @classmethod
    def total(cls):
            print(f'{cls.total_cat}')

Cat.total()         # 0

kitty1 = Cat()
Cat.total()         # 1

kitty2 = Cat()
Cat.total()         # 2

print(Cat())        # <__main__.Cat object at 0x104ed7290>
Cat.total()         # 3