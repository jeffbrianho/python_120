class Car:

    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color
        self.current_speed = 0

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('Color must be a string')
        
        self._color = color

    @property
    def model(self):
        return self._model
    
    @property
    def year(self):
        return self._year

    @staticmethod
    def engine_on():
        print('The engine is on')

    def engine_off(self):
        self.current_speed = 0
        print('The car is off')

    def speed_up(self, speed):
        self.current_speed += speed
        print(f'The car is moving')

    def slow_down(self, speed):
        self.current_speed -= speed
        print('The car is slowing down')

    def display_speed(self):
        print(f'Your speed is currently {self.current_speed} mph')

    def spray_paint(self, color):
        self.color = color
        print(f'Just painted your car {color}')

    @classmethod
    def display_gas_milage(cls, gallons, distance):
        gas_milage = distance / gallons
        print(f'your gas milage is {gas_milage}')

toyota = Car('Supra', 1993, 'black')
toyota.display_speed()
toyota.engine_on()
toyota.speed_up(35)
toyota.display_speed()
toyota.slow_down(15)
toyota.display_speed()
toyota.engine_off()
toyota.display_speed()

# print(f'my model is {toyota.model}')
# print(f'my year is {toyota.year}')
# print(f'my color is {toyota.color}')

# toyota.color = 'red'
# print(f'my color is {toyota.color}')
# toyota.spray_paint('blue')
# print(f'my color is now {toyota.color}')

# Car.display_gas_milage(13, 351)
