# Create a mix-in for the Car and Truck classes from the previous exercise that lets you 
# operate the turn signals: signal left, signal right, and signal off. Use the following 
# code to test your code.

class Vehicle:
    number_of_vehicles = 0

    def __init__(self):
        Vehicle.number_of_vehicles += 1

    @classmethod
    def vehicles(cls):
        return Vehicle.number_of_vehicles

class SignalMixin:

    def signal_left(self):
        print('Signalling left')

    def signal_right(self):
        print('Signalling right')

    def signal_off(self):
        print('Signal is now off')

class Car(SignalMixin, Vehicle):
     
     def __init__(self):
          super().__init__()

class Truck(SignalMixin, Vehicle):

        def __init__(self):
          super().__init__()

class Boat(Vehicle):

    def __init__(self):
          super().__init__()

# print(Car.vehicles())     # 0
car1 = Car()
# print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
# print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
# print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
# print(Boat.vehicles())    # 8

# car1.signal_left()       # Signalling left
# truck1.signal_right()    # Signalling right
# car1.signal_off()        # Signal is now off
# truck1.signal_off()      # Signal is now off
# boat1.signal_left()
# AttributeError: 'Boat' object has no attribute
# 'signal_left'

print(Car.mro())
print(Truck.mro())
print(Boat.mro())
print(Vehicle.mro())