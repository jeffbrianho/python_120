class Student:
    def __init__(self, name):
        self._name = name

    # @property
    # def name(self):
    #     return self._name

    # @name.setter
    # def name(self, name):

    #     self._name = name

    @property
    def name(self):
        return self.name
    
    @name.setter
    def name(self, name):
        self.name = name
    
jon = Student('John')
print(jon.name)               # John

jon.name = 'Jon'
print(jon.name)               # Jon