"""
Code from Kylie Ying, Hangman Tutorial: https://www.youtube.com/watch?v=cJJTnI22IF8
"""
import random
import string

words = ['pink', 'blue', 'red', 'orange', 'lavendar', 'orange', 'green']

word_letters = [] #list of letters of the active_word
blank_letters = []
used_letters = [] #list of used letters
correct_letters = []
attempts = 4

def get_valid_word(words):
    word = random.choice(words) #randomly choose something from the list
    while "-" in word or " " in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_lowercase)
    used_letters = set() # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # " ".join(['a', 'b', 'cd'])--> "a b cd"
        

        # what current is (ie W - R D)
        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word:", " ".join(word_list))
        print(f"Lives left: {lives}")

        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Yay! You found a letter!")
            else:
                lives -= 1
                print("Sorry! Try again!")

        elif user_letter in used_letters:
            print("You have already used that character.Please try again.\n")

        else:
            print("You didn't type in a valid character\n")

        print("You have used these letters: ", " ".join(used_letters), "\n")


        if lives == 0:
            print(f"Sorry! You lost! The word was {word}")
        else:
            print("Yay! You win!")

    # gets here when len(word_letters) == 0


print("Welcome to my hangman game")
hangman()