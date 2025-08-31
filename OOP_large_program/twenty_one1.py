import os
import random

def clear_screen():
    os.system('clear')

class Card:
    RANK_VALUE = {
        'Ace': 11,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5, 
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'Jack': 10,
        'Queen': 10,
        'King': 10, 
    }

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    SUITS = ['Spades', 'Clubs', 'Hearts', 'Diamonds']
    RANKS = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.SUITS for rank in self.RANKS]

class Participant:
    TOTAL_BANK_ROLL = 5
    DIFFERENCE_IN_ACES = 11 - 1

    def __init__(self):
        self.hand = []
        self.bank_roll = self.TOTAL_BANK_ROLL

    def clear_hands(self):
        self.hand.clear()

    def display_bank_roll(self):
        return f'${self.bank_roll}'

    def get_rank(self):
        return [card.rank for card in self.hand]

    def hand_total(self):
        total = 0
        aces = self.get_rank().count('Ace')
        for card in self.hand:
            total += Card.RANK_VALUE[card.rank]
        if total > TwentyOneGame.BUST_AMOUNT and self.has_ace():
            while total > TwentyOneGame.BUST_AMOUNT and aces > 0:
                total -= self.DIFFERENCE_IN_ACES
                aces -= 1

        return total

    def has_ace(self):
        return any(["Ace" == card.rank for card in self.hand])
    
    def hit_card(self, deck):
        top_card = deck.cards.pop()
        self.hand.append(top_card)

class Player(Participant):
    pass

class Computer(Participant):
    pass

class TwentyOneGame:
    CARDS_DEALT = 2
    BUST_AMOUNT = 21
    DEALER_HIT = 17

    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.computer = Computer()
        self.starting_participant = self.player

    def start(self):
        self.display_welcome_message()
        self.start_cash_game()
        self.display_goodbye_message()

    def start_cash_game(self):
        while self.player.bank_roll != 0 and self.player.bank_roll != 10:
            self.play_one_game()
            self.payout()
            if self.player.bank_roll != 0 and self.player.bank_roll != 10:
                answer = input('Play again? (y,n) ').lower().strip()
                if answer[0] not in ['y', 'n']:
                    print('Not a valid answer please type (y or n) ')
                if answer.startswith('n'):
                    break
                self.discard_hands()
                self.new_deck()
            elif self.player.bank_roll == 0:
                print('You ran out of money!')
            else:
                print('You cleaned out the house!') 


    def payout(self):
        if self.determine_winner() == self.player:
            self.player.bank_roll += 1
            self.computer.bank_roll -= 1
        else:
            self.player.bank_roll -= 1
            self.computer.bank_roll += 1

    def play_one_game(self):
        self.shuffle_cards()
        self.deal_cards()
        self.display_everyones_bank_roll()
        self.show_cards()
        self.show_dealers_partial_cards()
        self.player_turn()

        if self.is_bust(self.player):
            self.display_bust()
        else:
            self.dealer_turn()

        if self.is_bust(self.computer):
            self.display_bust()

        self.display_result()

    def shuffle_cards(self):
        random.shuffle(self.deck.cards)

    def new_deck(self):
        self.deck = Deck()
        self.shuffle_cards()

    def deal_cards(self):
        current_player = self.starting_participant
        print('Dealing out hands')
        print()
        while (len(self.player.hand) != TwentyOneGame.CARDS_DEALT or len(self.computer.hand) != TwentyOneGame.CARDS_DEALT):
            top_card = self.deck.cards.pop()
            current_player.hand.append(top_card)
            current_player = self.toggle_player(current_player)

    def discard_hands(self):
        self.player.clear_hands()
        self.computer.clear_hands()

    def toggle_player(self, player):
        return self.computer if player == self.player else self.player

    def show_cards(self):
        player = self.player
        print('Your hand: ')
        for indx in range(len(player.hand)):
            print(f'[{player.hand[indx]}]')
        print(f'Your hand total is {player.hand_total()}')
        print()

    def show_dealers_partial_cards(self):
        computer_hand = self.computer.hand
        print("The dealers hand:\n[UNKNOWN]")
        print(f'[{computer_hand[1]}]')
        print()

    def player_turn(self):
        while True:
            print("Would you like to hit or stay? (h/s)? ")
            decision = input().lower().strip()
            if decision.startswith('h'):
                self.player.hit_card(self.deck)
                print()
                self.show_dealers_partial_cards()
                self.show_cards()
                if self.is_bust(self.player):
                    break
            if decision.startswith('s'):
                break
            if decision[0] not in ['s', 'h']:
                print('Invalid selection, must choose hit or stay')

    def dealer_turn(self):
        self.computer.hand_total()
        print('Dealers Turn')
        self.reveal_dealer()
        while self.computer.hand_total() < self.DEALER_HIT:
            clear_screen()
            self.computer.hit_card(self.deck)
            self.reveal_dealer()
            if self.is_bust(self.computer):
                break 

    def reveal_dealer(self):
        computer_total = self.computer.hand_total()
        computer_hand = self.computer.hand
        print()
        print("The dealers hand:")
        for indx in range(0, len(computer_hand)):
            print(f'[{computer_hand[indx]}]')
        print(f'The dealers total is {computer_total}')

    def display_everyones_bank_roll(self):
        print(f'You have: {self.player.display_bank_roll()}')
        print(f'The dealer has: {self.computer.display_bank_roll()}')

    def display_welcome_message(self):
        clear_screen()
        print('Welcome to the game Twenty-One')
        print()

    def display_goodbye_message(self):
        print('Thanks for playing Twenty-One! Goodbye!')

    def display_result(self):
        clear_screen()

        self.show_cards()
        print()
        self.reveal_dealer()
        print()
        print(f'Your total is {self.player.hand_total()} '
              f'The dealers total is {self.computer.hand_total()}')
        
        if self.determine_winner() == self.player:
            print()
            print("You Win!")
            print()
        else:
            print()
            print("You Lose!")
            print()

    def determine_winner(self):
        if self.is_bust(self.computer):
            return self.player
        if self.is_bust(self.player):
            return self.computer

        winner = None
        if self.computer.hand_total() >= self.player.hand_total():
            winner = self.computer
        else:
            winner = self.player

        return winner

    def is_bust(self, participant):
        if participant.hand_total() > self.BUST_AMOUNT:
            return True
        
        return False

    def display_bust(self):
        print("Busted!")

game = TwentyOneGame()
game.start()

