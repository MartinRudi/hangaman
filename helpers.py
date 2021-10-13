from string import ascii_letters
from typing import List


def ask_letter(message, letters_list):
    # Infinite loop
    while True:
        char = input(message).upper()
        if len(char) != 1:
            print('Oops! Only one letter silly')
        elif not char in ascii_letters:
            print('Oops! No numbers or foreign languages!')
        elif char in letters_list:
            print('Cant repeat letters!')
        else:
            return char


def render_placeholder(chosen, letters_list):
    word = chosen.upper()  # LION
    lst = list(word)  # ['L', 'I', 'O', 'N']
    new_lst = []

    for char in lst:
        if char in letters_list:
            new_lst.append(char)
        else:
            new_lst.append('_')

    return ' '.join(new_lst)
