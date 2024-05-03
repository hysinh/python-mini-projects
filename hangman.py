import random

words = ['rabbit', 'squirrel', 'robin', 'cat', 'kangaroo', 'giraffe']


def play_game(word):
    """
    Runs the game
    """
    list = []
    for i in word:
        list.append(i)
    print(list)


word = random.choice(words)

play_game(word)