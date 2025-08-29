# Create a Car class that meets these requirements:

# Each Car object should have a model, model year, and color provided at instantiation time.

# You should have an instance variable that keeps track of the current speed. Initialize it to 
# 0 when you instantiate a new car.

# Create instance methods that let you turn the engine on, accelerate, brake, 
# and turn the engine off. Each method should display an appropriate message.

# Create a method that prints a message about the car's current speed.
# Write some code to test the methods.

class Car:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

    def engine_on(self):
        print('The engine is on')

    def accelerate(self, number):
        self.speed += number
        print(f'The car is accelerating {number} mph')

    def brake(self, number):
        self.speed -= number
        print(f'The car is braking {number} mph')

    def engine_off(self):
        self.speed = 0
        print('The engine is off')

    def get_speed(self):
        print(f'Your speed is {self.speed} mph')


supra = Car('Toyota Supra', 1993, 'black')

supra.engine_on()
supra.get_speed()
supra.accelerate(45)
supra.brake(20)
supra.get_speed()
supra.engine_off()
supra.get_speed()
