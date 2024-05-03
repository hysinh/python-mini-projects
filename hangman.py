import random

words = ['rabbit', 'squirrel', 'robin', 'cat', 'kangaroo', 'giraffe']

game_word = random.choice(words)

display = ["_" for letter in game_word]

print(game_word)
print(display)
print(*display, sep = " ")

letters_guessed = []
guess = input("Type in the letter you want to guess")
letters_guessed.append(guess)



def play_game(word):
    """
    Runs the game
    """
    list = []
    for i in word:
        list.append(i)
    
    print(list)


word = random.choice(words)

#play_game(word)