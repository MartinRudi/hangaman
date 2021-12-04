'''
1. Randomly pickup a word
2. Show placeholders for the letters
3. What letter?
    - add the letter to the word if it is right
    - tries -1 if the letter is wrong

    Add the letter to the list with already taken letters
4. End game if all letters are right or tries == 0
'''

from random import choice
from helpers import ask_letter, render_placeholder

# Dictionary of words
with open('./dict.txt', 'r') as f:
    words = [el.strip() for el in f.readlines()]

# The main UI message
message = '''
The word is:

{placeholder}

Letters that are used: {letters}
Tries left: {amount}

'''

# End of the game message
end_message = '''
The word was:

{chosen}

You {result}
Your final letters were: {letters}
'''


class HangmanGame:
    chosen: str
    chosen_word_letters: set[str]
    tries: int
    letters: list[str]

    def __init__(self):
        # Randomly chosen word
        self.chosen = choice(words).upper()
        self.chosen_word_letters = set(self.chosen)

        # User tries
        self.tries = len(self.chosen)

        # The list with guessed letters
        self.letters = []

    def game_round(self, letter: str):
        letter = letter.upper()
        if not self.is_finished() and letter not in self.letters:
            self.letters.append(letter)

            # Check letter in chosen word
            if letter not in self.chosen_word_letters:
                self.tries -= 1

    def is_win(self):
        return self.chosen_word_letters.issubset(set(self.letters))

    def is_finished(self):
        return self.tries == 0 or self.is_win()

    def run_in_console(self, letter: str):
        while not self.is_finished():
            placeholder = render_placeholder(self.chosen, self.letters)

            # Intro message
            msg = message.format(amount=self.tries, letters=', '.join(
                self.letters), placeholder=placeholder)
            print(msg)

            # Ask for the letter
            letter = ask_letter('Guess the letter: ', self.letters)
            self.game_round(letter)

        # ENDING THE GAME
        if self.is_win():
            result = 'Win!!!!'
        else:
            result = 'Lose :('

        return end_message.format(chosen=self.chosen.upper(), result=result,
                                  letters=', '.join(self.letters))


if __name__ == '__main__':
    game = HangmanGame()
    print(game.chosen_word_letters)
