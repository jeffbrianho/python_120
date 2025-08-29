# Using decorators, add getter and setter methods to your Car class so you can view and change 
# the color of your car. You should also add getter methods that let you view but not modify 
# the car's model and year. Don't forget to write some tests.

class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
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

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year



supra = Car('Toyota Supra', 1993, 'black')

print(supra.color)
supra.color = 'grey'
print(supra.color)
print(supra.year)
print(supra.model)

