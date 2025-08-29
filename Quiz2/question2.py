class Student:
    # def __init__(self, name):
    #     self.name = name

    # def __str__(self):
    #     return f'{(self.__class__.__name__)} {self.name}'
    

    def __init__(self, name, grade=None):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f'{self.__class__.__name__} {self.name}'



ade = Student('Adewale')
print(ade)        # Student Adewale

# Which of the following code snippets can you add to the class 
# body so that the above code returns a Student object whose state matches 
# the comment in the last line shown above? Select all that apply.


