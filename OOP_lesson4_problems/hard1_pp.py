# Question 1:
# Ben and Alyssa are working on a vehicle management
#  system. So far, they have created classes called
#  Auto and Motorcycle to represent automobiles and 
# motorcycles. After having noticed common information 
# and calculations they were performing for each vehicle 
# type, they decided to break the common behaviors into a
# separate class called WheeledVehicle. This is what their
#  code looks like so far:

class FuelMixin:
    def range(self):
        if isinstance(self, Catamaran) or isinstance(self, Motorboat):
            return (self.fuel_capacity * self.fuel_efficiency) + 10
        else:
            return (self.fuel_capacity * self.fuel_efficiency)


class WheeledVehicle:
    def __init__(self,
                 tire_list,
                 kilometers_per_liter,
                 liters_of_fuel_capacity):
        self.tires = tire_list
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

    def tire_pressure(self, tire_index):
        return self.tires[tire_index]

    def inflate_tire(self, tire_index, pressure):
        self.tires[tire_index] = pressure

class Auto(FuelMixin, WheeledVehicle):
    def __init__(self):
        # 4 tires with various tire pressures
        super().__init__([30, 30, 32, 32], 50, 25.0)

class Motorcycle(FuelMixin, WheeledVehicle):
    def __init__(self):
        # 2 tires with various tire pressures
        super().__init__([20, 20], 80, 8.0)

class Catamaran(FuelMixin):
    def __init__(self,
                number_propellers,
                number_hulls,
                kilometers_per_liter,
                liters_of_fuel_capacity):
        self.propellers = number_propellers
        self.hulls = number_hulls
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity

class Motorboat(Catamaran):
    def __init__(self, kilometers_per_liter, liters_of_fuel_capacity):
        super().__init__(1, 1, kilometers_per_liter, liters_of_fuel_capacity)
        self.fuel_efficiency = kilometers_per_liter
        self.fuel_capacity = liters_of_fuel_capacity
        

# This new class does not fit well with the object 
# hierarchy defined so far. Catamarans don't have tires.
#  But we still want a common code to track fuel 
# efficiency and range. Modify the class definitions 
# and move code into a mix-in, as necessary, to share 
# code among the Catamaran and the wheeled vehicles.
mot = Motorboat(80, 8.0)
print(mot.range())