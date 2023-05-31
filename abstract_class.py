# An abstract class doesn't have any instance
# Abstract class can have abstract methods
# An abstract method must be implemented by classes that inherits from the abstract class

import random
class AbstractGame:
    def start_game(self):
        while True:
            start = input("Would you like to play? ")
            if start.casefold() == "yes" or start.casefold() == "y":
                break
        self.play()

    def end_game(self):
        print("The game has ended.")
        self.reset()

    # Abstract method.
    # It doesn't do anything except from raising an exception if the child class doesn't implement them
    # The concrete implementation is done in the child class
    def play(self):
        raise NotImplementedError("You must provide an implementation for play()")

    # Abstract method.
    # It doesn't do anything except from raising an exception if the child class doesn't implement them
    # The concrete implementation is done in the child class
    def reset(self):
        raise NotImplementedError("You must provide an implementation for reset()")


class RandomGuesser(AbstractGame):
    def __init__(self, rounds):
        self.rounds = rounds
        self.round = 0

    # Implement the play() abstract method. This implementation is specific to the RandomGuesser class. Another game would have another implementation
    def play(self):
        while self.round < self.rounds:
            self.round += 1

            print(f"Welcome to the round {self.round}. Let's begin!")
            random_num = random.randint(1, 10)
            while True:
                guess = input("Enter a number between 1 and 10: ")
                if int(guess) == random_num:
                    print("You did it!")
                    break
        self.end_game()

    # Resetting the round to round 0
    def reset(self):
        self.round = 0


game = RandomGuesser(3)
game.start_game()