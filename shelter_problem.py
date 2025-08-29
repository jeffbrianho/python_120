# Consider a pet shelter where owners can adopt pets. We need to model this system using classes. 
# Your task is to write the Pet, Owner, and Shelter classes that will make the following code 
# run and produce the specified output.
# This exercise will require you to think about how these objects collaborate. 
# For instance, a Shelter object will need to manage a collection of Owner objects, 
# and each Owner object will need to manage a collection of Pet objects.

class Pet:
    def __init__(self, animal, name):
        self.animal = animal
        self.name = name

    def info(self):
        return f'a {self.animal} named {self.name}'

butterscotch = Pet('cat', 'Butterscotch')
pudding      = Pet('cat', 'Pudding')
darwin       = Pet('bearded dragon', 'Darwin')
kennedy      = Pet('dog', 'Kennedy')
molly        = Pet('dog', 'Molly')
sweetie      = Pet('parakeet', 'Sweetie Pie')
chester      = Pet('fish', 'Chester')

class Owner:
    
    def __init__(self, name):
        self.name = name
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def number_of_pets(self):
        return len(self.pets)
    
    def print_pets(self):
        for pet in self.pets:
            print(pet.info())

pete = Owner('P Hanson')
beth = Owner('B Holmes')

class Shelter:
    
    def __init__(self):
        self.owners = {}

    def adopt(self, owner, pet):
        owner.add_pet(pet)
        if owner.name not in self.owners:
            self.owners[owner.name] = owner

    def print_adoptions(self):
        for name, owner in self.owners.items():
            print(f'{name} has adopted the following pets:')
            owner.print_pets()
            print()

shelter = Shelter()

# Process adoptions
shelter.adopt(pete, butterscotch)
shelter.adopt(pete, pudding)
shelter.adopt(pete, darwin)
shelter.adopt(beth, kennedy)
shelter.adopt(beth, molly)
shelter.adopt(beth, sweetie)
shelter.adopt(beth, chester)

# Print adoption information
shelter.print_adoptions()

print(f"{pete.name} has {pete.number_of_pets()} adopted pets.")
print(f"{beth.name} has {beth.number_of_pets()} adopted pets.")