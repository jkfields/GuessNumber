# coding=utf-8

import random
import sys

class GuessNumber:
    play_game = True
    guess_count = 0

    messages = { "play" : "{0}, let's play a game. I'm thinking of a number between {1} and {2}.",
                 "guess" : "\nTake a guess ({0} of {1}). ",
                 "correct" : "Excellent, {0}! You guessed the number in {1} guesses!",
                 "high" : "Your guess is too high.",
                 "low" : "Your guess is too low.",
                 "name" : "Hello! What is your name? ",
                 "wrong" : "\nUh oh. The number I was thinking of was {0}.",
                 "error" : "*** Guess a number between {0} and {1}! ***"
               }

    def __init__(self, min=1, max=10, allowed=5):
        self.max_number = max
        self.min_number = min
        self.guesses_allowed = allowed

        self.number = random.randint(min, max)
        self.list_of_numbers = list(range(min, max))


    def play(self):
        self.name = self.get_user_input(self.messages.get('name'))

        message = "{0}, let's play a game. I'm thinking of a number between {1} and {2}."
        print(self.messages.get('play').format(self.name,
                                               self.min_number,
                                               self.max_number))
        while self.play_game:
            self.guess_count += 1
            msg = self.messages.get('guess').format(self.guess_count,
                                                    self.guesses_allowed)
            _guess = self.get_user_input(msg)

            if _guess.isdigit():
                self.guess = int(_guess)

                if self.guess_count == self.guesses_allowed or self.guess == self.number:
                    self.play_game = False

                if self.guess < self.number:
                    print(self.messages.get('low'))

                if self.guess > self.number:
                    print(self.messages.get('high'))

            else:
                print(self.messages.get('error').format(self.min_number,
                                                        self.max_number))
        if self.guess == self.number:
            print(self.messages.get('correct').format(self.name,
                                                      self.guess_count))
        else:
            print(self.messages.get('wrong').format(self.number))


    @staticmethod
    def get_user_input(msg=None):
        rtn_value = ""

        if msg:
            sys.stdout.write(msg)
            rtn_value = sys.stdin.readline().strip()

        return rtn_value


def main(args=None):
    game = GuessNumber(1, 20, 4)
    game.play()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
