"""

#take active_word and convert to a list of letters

#print each letter to "_" for each item in list word_letters

#request guess in put from user
#compare guess to each item in list of active_word - for loop

#if letter matches and letters in list, 
    # replace "_" with letter
    #print updated word_letters string
    # appends guess to used_letters list
    #print used_letters list
    #loop back to ask for guess input
#else:
    #reprint active_word with "_"
    #appends guess to used_letters list
    #print used_letters list
    #option message: Sorry. There is no {guess} in the word
    #loop back to ask for guess input
#if attempts == 0: lose game
    #print lose game message
    #input(play again?)
#if len(correct_letters) == len(word_letters): win game
    #print win game message
    #input(play again?)
"""

import random

words = ['cat', 'pickle', 'sandwich', 'dolphin', 'popcorn', 'spaceship', 'grass']

word_letters = [] #list of letters of the active_word
#blanks = [] # list of blank letters
used_letters = [] #list of used letters
correct_letters = []


def generate_random_word():
    """
    Selects a random word from the words list and appends it to list
    """
    random_word = random.choice(words) #randomly selected word from words list
    word_letters.append([letter for letter in random_word])
    return random_word


def makes_letter_list(word):
    """
    Creates a list of the letters of the active word
    """
    letters = [letter for letter in word]
    return letters
    
    
def makes_blanks(list):
    """
    Creates a list substituting "_" for each letter in the list
    """
    blanks = ["_" for letter in list]    
    return blanks



def test_letter(guess, word):
    #print(f"in test-letter function: {word}")
    word_letters = [letter for letter in word]
    word_display = ["_" for letter in word_letters]
    attempts = 2 
    #print(word_display)
    #for i in word:
        #if guess == i:
            #print(f"this letter is in the word: {guess}")
        #else:
            #print(f"This letter is not in the word: {guess}")
    while attempts > 0 and "_" in word_display:
        if guess in word:
            print("\n" + " ".join(word))
            print(f"in if statment: {guess}")
            for index, letter in enumerate(word):
                #print(letter)
                if guess == letter:
                    print("Yay! Your letter is in the word")
                    letter = guess #reveal letter
                    print(f"in the enumerate function: {letter}")
        else:
            print("That letter doesn't appear in the word.")
            print("========")
            attempts -= 1
            print(attempts)



#if letter matches and letters in list, 
    # replace "_" with letter
    #print updated word_letters string
    # appends guess to used_letters list
    #print used_letters list
    #loop back to ask for guess input
#else:
    #reprint active_word with "_"
    #appends guess to used_letters list
    #print used_letters list
    #option message: Sorry. There is no {guess} in the word
    #loop back to ask for guess input

#if attempts == 0: lose game
    #print lose game message
    #input(play again?)

#if len(correct_letters) == len(word_letters): win game
    #print win game message
    #input(play again?)

def run_game():
    active_word = generate_random_word()
    print(f"active_word: {active_word}")
    letters = makes_letter_list(active_word)
    blanks = makes_blanks(letters)
    print("\n" + " ".join(blanks))
    guess = input("Guess a letter: \n").lower()
    test_letter(guess, active_word)


print("Welcome to Guess My Word. A singular game of chance.")
run_game()