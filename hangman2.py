import random

words = ['cat', 'pickle', 'sandwich', 'dolphin', 'popcorn', 'spaceship', 'grass']

word_letters = [] #String of letters of the active_word
used_letters = [] #string of used letters
correct_letters = []
attempts = 8 

def generate_random_word():
    active_word = random.choice(words) #randomly selected word from words list
    word_letters = [letter for letter in active_word]     
    print(active_word)
    return word_letters



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

def run_game():
    generate_random_word()
    print(word_letters)
    guess = input("Guess a letter: \n").lower()



run_game()