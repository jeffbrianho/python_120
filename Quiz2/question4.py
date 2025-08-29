class Character:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} is speaking.'

class Thief(Character):
    def speak(self):
        return f'{self.name} is whispering'

sneak = Thief('Sneak')
print(sneak.name)             # Sneak
print(sneak.speak())          # Sneak is whispering.