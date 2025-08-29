class Dog:
    def __init__(self, breed):
        self._breed = breed

    def get_breed(self):
        return(self._breed)

golden_retriever = Dog('Golden Retriever')
poodle = Dog('Poodle')

# print(golden_retriever.get_breed())
# print(poodle.get_breed())

class Cat:
    def get_name(self):
        try:
            return self.name
        except AttributeError:
            return 'Name not set!'
cat = Cat()

# dog3 = Dog('Bulldog')
# dog3._breed = 'Sheltie'
# print(dog3.get_breed())

class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school(cls):
        return cls.school_name
    
# student1 = Student('Jim')
# student2 = Student('Pam')

# print(student1.__class__.school_name, student1.name)
# print(student2.__class__.school_name, student2.name)

# print(Student.get_school())
# print(Student.school_name)

class Car:
    manufacturer = 'Japan'

    def __init__(self, manufacturer):
        self.manufacturer = manufacturer

    def show_manufacturer(self):
        print(f'{self.manufacturer=}')
        print(f'{Car.manufacturer=}')

# car1 = Car('Toyota')

# car1.show_manufacturer()

# class Bird:
#     def __init__(self, species):
#         self.species = species

# class Sparrow(Bird):
#     pass

# bird = Sparrow('sparrow')

# print(bird.species)

class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        super().__init__(species)
        self.color = color

# birdie = Sparrow("sparrow", "brown")
# print(birdie.species)               # What will this output?

# error due to not using super()

class Mammal:
    def __init__(self):
        self.legs = 4

class Human(Mammal):
     def __init__(self):
        self.legs = 2
human = Human()
print(human.legs)