import random
from words import words
import string

def get_valid_word(words):
    #randomly choose something from words list 
    word = random.choice(words)

    #we don't want words with '-' or ' ' in them   
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()


def hangman():
    word = get_valid_word(words) #call a get_valid_word method and pass the list argument.
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # keep a track of what user has guess
    lives = 6 # total lives in the game

    while len(word_letters) > 0 and lives > 0:

        #letters used so far
        print(f'You have {lives} left and You have used letters: ', ' '.join(used_letters))

        #tell user what the current word (i.e. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        #getting user input 
        user_letter = input("Guess a letter: ").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            
            #when a correct character is entere it would be removed from word_letters else a life will be reduced
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives -1 

        # when user repeats the character
        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        #everything else is invalid 
        else:
            print('Invalid character, please try again.')

    #gets here when len(word_letters) == 0
    

    if lives == 0:
        print(f'You died, the word was {word}')
    else:
        print(f'Yay! you guessed the word, it is - {word}')

hangman()