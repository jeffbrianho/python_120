class Dog:
    def speak(self):
        return 'bark!'

    def sleep(self):
        return 'sleeping!'

# Create a subclass from Dog called Bulldog overriding the sleep method to return "snoring!"

class Bulldog(Dog):

    def sleep(self):
        return "snoring!"
    
teddy = Dog()
print(teddy.speak())      # bark!
print(teddy.sleep())       # sleeping!

karl = Bulldog()
print(karl.speak())       # bark!
print(karl.sleep())        # snoring!