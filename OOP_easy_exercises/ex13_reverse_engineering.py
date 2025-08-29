# Reverse Engineering

# Write a class such that the following code prints the results indicated by the comments

class Transform:
    def __init__(self, letters):
        self.letters = letters

    def uppercase(self):
        if self.letters.isalpha():
            return self.letters.upper()
        
        return NotImplemented
    
    @classmethod
    def lowercase(cls, letter):
        if letter.isalpha():
            return letter.lower()
        
        return NotImplemented


my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz