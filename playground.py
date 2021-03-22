import string

def guess_word(word):
    
    word_letters = set(word)
    used_letters = set()
    alphabet = set(string.ascii_uppercase)

    while len(word_letters) > 0:

        user_letter = input("Please input a character: ").upper()
        print("Current word: ", ' '.join(used_letters))

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("you have already entered this character, please try again")

        else:
            print("Invalid character.")

    print(used_letters)

guess_word('ajit')