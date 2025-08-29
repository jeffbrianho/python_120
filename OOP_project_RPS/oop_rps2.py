import random

class Move:
    def __init__(self):
        self._beats = []

    def beats(self, other_move):
        return other_move.__class__.__name__.lower() in self._beats

class Rock(Move):
    def __init__(self):
        super().__init__()
        self._beats = ['scissors', 'lizard']

class Paper(Move):
    def __init__(self):
        super().__init__()
        self._beats = ['rock', 'spock']

class Scissors(Move):
    def __init__(self):
        super().__init__()
        self._beats = ['paper', 'lizard']

class Lizard(Move):
    def __init__(self):
        super().__init__()
        self._beats = ['paper', 'spock']

class Spock(Move):
    def __init__(self):
        super().__init__()
        self._beats = ['scissors', 'rock']

class Player:
    CHOICES = ('rock', 'paper', 'scissors', 'lizard', 'spock')
    move_classes = {
    'rock': Rock,
    'paper': Paper,
    'scissors': Scissors,
    'lizard': Lizard,
    'spock': Spock
}
    
    def __init__(self):
        self.move = None
        self.score = 0
        self.history = []

class Computer(Player):
    def __init__(self, name=None):
        super().__init__()
        self._name = name

    def choose(self, human_move=None):
        print(self._name)
        if self._name == 'R2D2':
            self.move = Player.move_classes['rock']()
        elif self._name == 'HAL':
            choices = ['scissors'] * 5 + list(Player.CHOICES)
            self.move = Player.move_classes[random.choice(choices)]()
        elif self._name == "Daneel":
            if human_move:
                self.move = Player.move_classes[human_move.lower()]()
            else:
                self.move = Player.move_classes[random.choice(Player.CHOICES)]()
        else:
            self.move = Player.move_classes[random.choice(Player.CHOICES)]()

        self.history.append(type(self.move).__name__)

class Human(Player):

    def __init__(self):
        super().__init__()

    def choose(self):
        prompt = 'Please choose rock, paper, scissors, lizard, or spock: '

        while True:
            choice = input(prompt).lower()
            if choice.lower() in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')

        self.move = Player.move_classes[choice]()
        self.history.append(type(self.move).__name__)

class RPSGame:
    WIN_NUMBER = 5
    
    def __init__(self):
        self._choose_computer()
        self._human = Human()
        self._computer = Computer(self._computer_name)

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors Lizard Spock!')

    def _display_goodbye_message(self):
        winner = [player for player in (self._computer, self._human) if player.score == 5]
        name = 'You' if winner[0] == self._human else f'{self._computer_name}'
        print(f'{name} won 5 games!')
        print('Thanks for playing Rock Paper Scissors Lizard Spock. Goodbye!')

    def _display_winner(self):
        print(f'You chose: {type(self._human.move).__name__}')
        print(f'{self._computer_name} chose: {type(self._computer.move).__name__}')

        if self._human.move.beats(self._computer.move):
            print('You win!')
            self._human.score += 1
        elif self._computer.move.beats(self._human.move):
            print(f'{self._computer_name}  wins!')
            self._computer.score += 1
        else:
            print("It's a tie")
    def _choose_computer(self):
        computer_name = input('Input a Computer Name'
                            '(R2D2, HAL, Daneel, or random): ')
        
        self._computer_name = computer_name

    def _display_score(self):
        print()
        print(f'Your current score is: {self._human.score}, '
              f'{self._computer_name}\'s score is: {self._computer.score}')
        print()

    def _display_history(self):
        print('You chose: ')
        for hindx, human_choice in enumerate(self._human.history):
            print(f'{hindx + 1}: {human_choice}', end=' ') 
        print()
        print(f'{self._computer_name} chose: ') 
        for cindx, computer_choice in enumerate(self._computer.history):
            print(f'{cindx + 1}: {computer_choice}', end=' ')
        print()


    def play(self):
        self._display_welcome_message()

        while True:
            self._human.choose()
            human_last_move_name = type(self._human.move).__name__ if self._human.move else None
            self._computer.choose(human_move=human_last_move_name.lower() if human_last_move_name else None)

            self._display_winner()
            self._display_score()
            self._display_history()
            
            if self._computer.score >= RPSGame.WIN_NUMBER or self._human.score >= RPSGame.WIN_NUMBER:
                break

        self._display_goodbye_message()

RPSGame().play()

