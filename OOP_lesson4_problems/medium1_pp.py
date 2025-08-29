# Question 1
class BankAccount:
    def __init__(self, starting_balance):
        self._balance = starting_balance

    def balance_is_positive(self):
        return self.balance > 0

    @property
    def balance(self):
        return self._balance
    

# Ben glanced over the code quickly and said - "It looks fine, except that you're trying to access self.balance instead of self._balance in the balance_is_positive method."

# "Not so fast," Alyssa replied. "What I'm doing here is valid; I can definitely use self.balance there!"

# Who is correct, Ben or Alyssa? Why?

# Alyssa. she is using a property decorator that calls self._balance when self.balance is used

# Question 2

class InvoiceEntry:
    def __init__(self, product_name, number_purchased):
        self._product_name = product_name
        self._quantity = number_purchased

    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity

# entry = InvoiceEntry('Marbles', 5000)
# print(entry.quantity)         # 5000

# entry.quantity = 10_000
# print(entry.quantity)         # 10_000

# Without changing any of the above lines of code, update the InvoiceEntry class so it functions as shown.

# Question 3

# Let's practice creating an object hierarchy.

# Create a class called Animal with a single instance method called speak that takes a string argument and prints that argument to the terminal.

# # Now create two other classes that inherit from Animal, one called Cat and one called Dog. The Cat class should have a meow instance method that takes no arguments and prints Meow!. The Dog class should have a bark instance method that says Woof! Woof! Woof! (dogs never bark just once). Make use of the Animal class's speak method when implementing the Cat and Dog classes. Don't invoke the print function in either of the subclasses.

class Animal:
    def speak(self, string):
        print(string)

class Cat(Animal):
    def meow(self):
        self.speak('Meow!')

class Dog(Animal):
    def bark(self):
        self.speak(('Woof! ' * 3).strip())
    
# cat = Cat()
# dog = Dog()

# cat.meow()
# dog.bark()

# Question 4:

class KrispyKreme:
    def __init__(self, filling, glazing):
        self.filling = filling
        self.glazing = glazing

    def __str__(self):
        if not self.filling:
            self.filling = 'Plain'

        if not self.glazing:
            self.glazing = ''
            return f'{self.filling}'
        else:
            return f'{self.filling} with {self.glazing}'

        

# donut1 = KrispyKreme(None, None)
# donut2 = KrispyKreme('Vanilla', None)
# donut3 = KrispyKreme(None, 'sugar')
# donut4 = KrispyKreme(None, 'chocolate sprinkles')
# donut5 = KrispyKreme('Custard', 'icing')

# print(donut1)       # Plain
# print(donut2)       # Vanilla
# print(donut3)       # Plain with sugar
# print(donut4)       # Plain with chocolate sprinkles
# print(donut5)       # Custard with icing

# Question 5

# How could you change the light_status method name below so that the method name is clearer and less repetitive?

class Light:
    def __init__(self, brightness, color):
        self.brightness = brightness
        self.color = color

    def status(self):
        return (f'I have a brightness level of {self.brightness} '
                f'and a color of {self.color}')

my_light = Light(50, 'Red')
print(my_light.status())