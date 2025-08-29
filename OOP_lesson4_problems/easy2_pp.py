# Question 1:
class Game:
    count = 0
    
    def __init__(self, game):
        self.game = game
        Game.count += 1

    def play(self):
        return f'Start the {self.game} game!'

class Bingo(Game):
    def __init__(self, game, player_name):
        super().__init__(game)
        self.player_name = player_name

class Scrabble(Game):
    def __init__(self, game, player_name1, player_name2):
        super().__init__(game)
        self.player_name1 = player_name1
        self.player_name2 = player_name2


# Update this code so that Bingo 
# inherits the play method from the Game class.

# print(Bingo().play())

# Question 2
# Update your code from the previous question so 
# the following code works as indicated:

# bingo = Bingo('Bingo', 'Bill')
# print(Game.count)                       # 1
# print(bingo.play())                     # Start the Bingo game!
# print(bingo.player_name)                # Bill

# scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
# print(Game.count)                       # 2
# print(scrabble.play())                  # Start the Scrabble game!
# print(scrabble.player_name1)            # Jill
# print(scrabble.player_name2)            # Sill
# print(scrabble.player_name)
# AttributeError: 'Scrabble' object has no attribute 'player_name'

# Question 3
# What are the benefits of using object-oriented 
# programming in Python? Think of as many as you can.
# 1. compartmentalize different actions
# 2. organize code for readability
# 3. preventing dependencies on all areas of code
# 4. import functions of code

# There's no single right answer here, and we certainly can't list all the benefits. We will just summarize some of the major ones:

# As software becomes more complex, OOP helps manage this complexity.
# It lets programmers create containers for data that can be changed and manipulated without affecting the entire program.
# It lets programmers section off areas of code that perform specific procedures. This allows their programs to become the interaction of many small parts as opposed to a massive blob of dependencies.
# We can talk about objects as nouns and their behaviors as verbs. These distincitions make it easier to conceptualize the structure of an OO program.
# Creating classes and objects lets programmers think about code at a more abstract level.
# It lets programmers write code that can be used with different kinds of data.
# We can build applications faster as we can reuse pre-written code.

# Question 4

class Greeting:
    def greet(self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet('Hello')

    @classmethod
    def hi(cls):
        greeting = Greeting()
        greeting.greet('hi')
        

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

# hello = Hello()
# hello.hi() # print Hello

# hello = Hello()
# hello.bye() # Attribute Error no bye

# hello = Hello()
# hello.greet() # no message Typeerror missing positional argument 'message'

# hello = Hello()
# hello.greet('Goodbye') # print Goodbye

Hello.hi() # print Hello
# Snippet 5 is a bit tricky. This raises a
#  TypeError because hi is missing one positional 
# argument, for the self parameter. This happens
#  because we're invoking hi on the class Hello 
# rather than an instance. When we invoke instance 
# methods as class methods, no instance is passed in
#  as self.

# Question 5
# Modify the code from the previous question 
# so that calling Hello.hi() on the class (rather 
# than an instance) still uses Greeting's instance 
# method greet() to print "Hi".

# Question 6
class Cat:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f'I am a {self.type}'

print(Cat('hairball'))
# <__main__.Cat object at 0x10695eb10>

# "The output here isn't very useful. 
# It only tells us that we've got an instance of the 
# Cat class, and it's memory address. It would be
#  better if the output were more meaningful. For 
# instance, maybe it can print I am a hairball instead. 
# Update the code to produce that result."

# Question 7

class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()
print(tv.manufacturer()) # Amazon
print(tv.model()) # Omni Fire

print(Television.manufacturer()) #amazon
print(Television.model()) # attribute erro