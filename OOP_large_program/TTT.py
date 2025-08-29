"""
Tic Tac Toe:
2 players
alternating turns in 9 squares
filling in a square assess board and allow for other player to choose
when one player completes 3 in a row or board is full, game over

Nouns:
    Players / Computer; Person
    Board - positions

Verbs:
    Moves - choose square

Start scaffolding


Board class: init() 9 positions
broken into squares, boards, and rows

Player class
    mark method
    play method

Human
Compiuter
Game skeleton

"""


class Square:
    def __init__(self):
        # STUB
        # We need some way to keep track of this square's
        # marker
    
        pass

class Board:
    def __init__(self):
        # STUB
        # We need a way to model the 3x3 grid. Perhaps
        # "squares"?
        # What data strucutre should we use? A list? a dictionary? 
        # Something else?
        # What should the data structure store? Strings?
        # Numbers? Square objects?
        pass

class Row:
    def __init__(self):
        # STUB - placeholders for methods to be written or removed later
        # We need some way to identify a row of 3 squares
        pass

class Maker:
    def __init__(self):
        # STUB
        # A marker is something that represents a board
        # square that belongs to a particular player. 
        # That is, it's a square that was chosen by the player. 
        pass

class Player:
    def __init__(self):
        # STUB
        # A player is either a human or a coputer that is 
        # playing the game. 
        # Perhaps we need a "marker" to keep track of this
        # player's symbol? (i.e, 'X' or 'O')
        pass
    
    def mark(self):
        # STUB
        # We need a way to mark the board with this player
        # marker. How do we access the board?
        pass

    def play(self):
        # STUB
        # We need a way for each player to play the game.
        # Do we need access to the board?
        pass

class Human(Player):
    def __init__(self):
        # STUB
        # What does a human player need to do? How
        # does it differ from the basic Player or Computer
        pass

class Computer(Player):
    def __init__(self):
        # STUB
        # What does a computer player need to do? How does
        # it differ from the basic Player or a Human?
        pass

class TTTGame: # orchestration engine
    # controls the flow of the application ; keep last
    def __init__(self):
        # STUB
        # We need a board and two players.
        pass

    def play(self):
        # STUB
        # Orchestrate game play.
        # - Declare start of game
        # - Player choose a square
        # - Comp chooses a square
            #  - continue until win condition or tie condition

        # SPIKE:
            #- Display a welcome message.
            # Repeat until the game is over
            #   Display the current state of the board
            #Let the first player make a move
            # Is the game voer? If so exit
            # Let the second player make a move 
            # is the game over/. if so exit
        # Display the final state of the board
        # Display the final result
        # Display a goodbye message

        
        # order methods alphabetically
        pass

game = TTTGame()
game.play()

# Stubs are methods like a to-do list. more common in 
# OO code than procedural code since there is no 
# top-to-bottom code
