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
words = ['lion', 'dog', 'cat']

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

# Randomly chosen word
chosen = choice(words).upper()
chosen_word_letters = set(chosen)

# User tries
tries = len(chosen)

# The list with guessed letters
letters = []


def is_win():
    return chosen_word_letters.issubset(set(letters))


# THE GAME MAIN LOOP
while tries > 0 and not is_win():
    placeholder = render_placeholder(chosen, letters)

    # Intro message
    msg = message.format(amount=tries, letters=', '.join(
        letters), placeholder=placeholder)
    print(msg)

    # Ask for the letter
    letter = ask_letter('Guess the letter: ', letters)
    letters.append(letter)

    # Check letter in chosen word
    if letter not in chosen_word_letters:
        tries -= 1

# ENDING THE GAME

print(f'DEBUG: {letters=} {chosen_word_letters=} {is_win()=}')

if is_win():
    result = 'Win!!!!'
else:
    result = 'Lose :('

end = end_message.format(chosen=chosen.upper(), result=result,
                         letters=', '.join(letters))
print(end)
