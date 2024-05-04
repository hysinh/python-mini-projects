import random

words = ['cat', 'pickle', 'sandwich', 'dolphin', 'popcorn', 'spaceship', 'grass']

word_letters = [] #list of letters of the active_word
blank_letters = []
used_letters = [] #list of used letters
correct_letters = []
attempts = 8 

def generate_random_word():
    random_word = random.choice(words) #randomly selected word from words list
    word_letters.append([letter for letter in random_word])
    return random_word


def makes_letter_list(word):
    letters = [letter for letter in word]
    return letters
    
    
def makes_blanks(list):
    blanks = ["_" for letter in list]    
    return blanks



def test_letter(letter, word):
    print(word)
    print(letter)
    for i in word:
        if letter == i:
            print(f"this letter is in the word: {letter}")
        else:
            print(f"This letter is not in the word: {letter}")



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
    print(word_letters)
    letters = makes_letter_list(active_word)
    blanks = makes_blanks(letters)
    print(*blanks, sep = " ")
    guess = input("Guess a letter: \n").lower()
    test_letter(guess, letters)


print("Welcome to Guess My Word. A singular game of chance.")
run_game()