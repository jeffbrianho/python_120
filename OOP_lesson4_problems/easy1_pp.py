# Question 1:
# Which of the following are objects in Python? If 
# they are objects, how can you find out what class 
# they belong to?


# print(type(True))
# print(type('hello'))
# print(type([1, 2, 3, 'happy days']))
# print(type(142))
# print(type({1, 2, 3}))
# print(type(1.2345))


# print(True.__class__.__name__)
# print('hello'.__class__.__name__)
# print([1, 2, 3, 'happy days'].__class__.__name__)
# print((142).__class__.__name__)
# print({1, 2, 3}.__class__.__name__)
# print(1.2345.__class__.__name__)

# Question 2

# How would you create a new instance of this class?

class AngryCat:
    def hiss(self):
        print('Hisssss!!!')

# AngryCat().hiss()

# Question 3:
# If we have a Car class and a Truck class and 
# we want to be able to go_fast, how can we add 
# the ability for them to go_fast using the mix-in 
# SpeedMixin? How can you check whether your Car or
#  Truck can now go fast?

class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

class Truck(SpeedMixin):
    def go_very_slow(self):
        print('I am a heavy truck and like going very slow.')

# Truck().go_fast()
# Car().go_fast()

# Question 4

# In the previous question, we had a mix-in called 
# SpeedMixin that contained a go_fast method. 
# We add this mix-in to the Car class as shown below:

class SpeedMixin:
    def go_fast(self):
        print(f'I am a super fast {self.__class__.__name__}!')

class Car(SpeedMixin):
    def go_slow(self):
        print('I am safe and driving slow.')

# small_car = Car()
# print(small_car.go_fast())
# # I am a super fast Car!

# When we called small_car.go_fast, 
# you may have noticed that the output includes the 
# vehicle type. How is this done?

# self.__class__.__name__ will apply to the calling class as an instance from the caller
# therefore it references the Car class and mixins won't have an instance variable

# We use self.__class__.__name__ in the method. It works like so:

# self refers to the object referenced by small_car. In this case, that's a Car object.
# self.__class__ returns a reference to the Car class, which is an object of the type class.
# Finally, self.__class__.__name__ returns the name of the Car class as a string: 'Car'.

# Question 5:

#Which of the following classes would create objects 
# that have an instance variable. How do you know?

class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

# pizza would, fruit would not due to not having self.name initialized. 

# Pizza class instances will have instance variables by virtue of assigning a value to self.my_name in the Pizza.__init__ method. Fruit class instances don't have instance variables since none are defined. my_name is a local variable only defined inside Fruit.__init__.

# You can verify this by using the vars function to see what instance variables exist in Pizza and Fruit objects:

# print(vars(Fruit('orange')))     # {}
# print(vars(Pizza('pepperoni')))  # {'my_name': 'pepperoni'}

# In this example, we can see that the Fruit object has no instance variables, while the Pizza object has a my_name instance variable whose value is 'pepperoni'.

# Question 6:

# Without running the following code, can you determine what the following code will do? Explain why you will get those results.


import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

# oracle = Oracle()
# print(oracle.predict_the_future())

# Question 7

# Suppose you have the Oracle class from above and a 
# RoadTrip class that inherits from the Oracle class,
#  as shown below:

import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'

    def choices(self):
        return [
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
        ]

class RoadTrip(Oracle):
    def choices(self):
        return [
            'visit Vegas',
            'fly to Fiji',
            'romp in Rome',
            'go on a Scrabble cruise',
            'get hopelessly lost',
        ]
    
# trip = RoadTrip()
# print(trip.predict_the_future())
# it will call random to the list of roadtrip as a roadtrip object is calling predict the future

# Why does this happen? Doesn't self.choices in 
# predict_the_future look in the Oracle class for 
# a choices method? The answer is no. Since we're calling
#  predict_the_future on an instance of RoadTrip, every 
# time Python tries to resolve a method name using self., 
# it first looks in the class of the calling object. 
# Even though we called choices from with a method in the
#  Oracle class, self refers to the RoadTrip class. 
# Thus, Python first looks for RoadTrip.choices before
#  falling back to Oracle.choices. To see the difference, 
# change the name of the RoadTrip.choices to RoadTrip.
# chooses and rerun the program.

# Question 8

# Suppose you have an object named my_obj and 
# that you want to call a method named foo using 
# my_obj as the caller. How can you see where Python
#  will look for the method. You don't need to determine 
# the actual method location; just identifying the search
#  sequence is sufficient.
#
# use .mro() so my_obj.__class__.mro()

# Question 9:

# There are several variables listed below. 
# What are the different variable types and how 
# do you know which is which?

# excited_dog = 'excited dog' # string local variable
# self.excited_dog = 'excited dog' # instance variable
# self.__class__.excited_dog = 'excited dog' # class_variable
# BigDog.excited_dog = 'excited dog' # class_variable

# Here we have the following variables:

# Variable	Variable Type
# excited_dog	Local variable
# self.excited_dog	Instance variable
# self.__class__.excited_dog	Class variable
# BigDog.excited_dog	Class variable
# We can tell which is which by how the variables are prefixed. Local variables don't have a prefix, while instance variables are usually prefixed with self..

# Class variables are prefixed with self.__class__. when self is an instance of the appropriate class or one of its subclasses. You can also use the name of the class as a prefix, e.g., BigDog..

# Though not shown here, there are three other ways to access class variables:

# You can use a cls. prefix inside class methods.
# You can use a type(self). prefix when self is an instance of the class or one of its subclasses.
# You can sometimes use a self. prefix when self is an instance of the class or one of its subclasses. However, this is not good practice and should be shunned.

# Question 10:

class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count
    
# Explain what the _cats_count variable is, what it 
# does in this class, and how it works.
#  Write some code to test your theory.

# cats counts will count the amount of cats created. 

print(Cat._cats_count)
cat1 = Cat('tabby')
print(Cat._cats_count)
cat2 = Cat('siamese')
print(Cat._cats_count)