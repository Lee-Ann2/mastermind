import random

def compare_codes():
    colours = ['black', 'pink', 'red', 'blue', 'yellow', 'green']
    random.shuffle(colours)
    getGuess = input(f'Enter the code. Pick 4 from the list: {colours}')
    i = 1
    while i < len(colours):
        print(colours[i])
        i += 1
compare_codes()