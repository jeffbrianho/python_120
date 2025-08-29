# Create a Car class that makes the following code work as indicated:

class Car:

    def __init__(self, id, year, color):
        self.id = id
        self.year = year
        self.color = color

    def __str__(self):
        return f'Car({self.color.title()}, {self.year}, {self.id})'

    def __repr__(self):
        id = repr(self.id)
        year = repr(self.year)
        color = repr(self.color)
        return f'Car({id}, {year}, {color})'
    
    



vwbuzz = Car('ID.Buzz', 2024, 'red')
print(vwbuzz)        # Red 2024 ID.Buzz
print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

