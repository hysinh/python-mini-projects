import random

words = ['rabbit', 'squirrel', 'robin', 'cat', 'kangaroo', 'giraffe']
game_word = random.choice(words)
# number of attempts allowed
attempts = 8 



#print(game_word)
#print(display)
##print(*display, sep = " ")

#letters_guessed = []
#guess = input("Type in the letter you want to guess")
#letters_guessed.append(guess)

#def check_win_lose():
    #print()
    #if guesses all letters: 
        #print(You won!)
    #elif wrong guesses == len(hangman):

def play_game(word):
    """
    Runs the game
    """
    # number of attempts allowed
    attempts = 8
    word_display = ["_" for letter in word]
    #word_letters = [str(letter) for letter in word]
    print(word)
    #print(display)
    #print(word_letters)
    while attempts > 0 and "_" in word_display:
        print("\n" + " ".join(word_display))# old code: print(*word_display, sep = " ")
        #letters_guessed = []
        guess = input("Guess a letter:\n").lower()
        if guess in game_word:
            for index, letter in enumerate(game_word):
                if letter == guess:
                    word_display[index] = guess #reveal letter
        else:
            print("That letter doesn't appear in the word.")
            print("========")
            attempts -= 1

    if "_" not in word_display:
        print("you guess the word!")
        print(' '.join(word_display))
    else:
        print(f"You ran out of attempts. The word was: {game_word}")
        print("You lost. :(")
    
    #letters_guessed.append(guess)
    #for letter in word_letters:
        #if letter matches letters in word:
            #print word with letter showing
            #guess = input("type in next guess")
        #else:
            #print display
            #print letters_guessed

#def random_word():
    #print()

#def display_word():
    #input = request from user
    #print()

#def check_guess():
    #print()
    #creates list of letters_guessed
    #compares letter_guessed against letters of word
    #if letters match:
        #displays word with letter showing
        #requests new input from user
    #else:
        #reprint word
        #adds hangman to hangman graphic
        #requests new input from user

#def check_win_lose():
    #print()
    #if guesses all letters: 
        #print(You won!)
    #elif wrong guesses == len(hangman):



print("Welcome to Hangman")
play_game(game_word)
#print(enumerate(game_word))

