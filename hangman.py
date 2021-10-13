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

# User tries
tries = 3

# Randomly chosen word
chosen = choice(words)

# The list with guessed letters
letters = []

# THE GAME MAIN LOOP
while tries > 0:
    placeholder = render_placeholder(chosen, letters)

    # Intro message
    msg = message.format(amount=tries, letters=', '.join(
        letters), placeholder=placeholder)
    print(msg)

    # Ask for the letter
    letter = ask_letter('Guess the letter: ', letters)
    letters.append(letter)

    # Check letter in chosen word
    tries -= 1

# ENDING THE GAME
if tries > 0:
    result = 'Win!!!!'
else:
    result = 'Lose :('

end = end_message.format(chosen=chosen.upper(), result=result,
                         letters=', '.join(letters))
print(end)
