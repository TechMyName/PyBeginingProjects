import random

#Computer generates a random number and we guess it.
#It also gives a hint everytime we enter wrong input.
'''
def guess_number(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Input a number between 1 and {x}: "))
        if guess > random_number:
            print("Sorry, too high try again.")
        elif guess < random_number:
            print("Sorry, too low try again.")

    print("Yay, you got it right!")

guess_number(10)

'''



def guess_computer(x):
    low = 0
    high = x 
    answer = ''

    while answer != 'c':
        
        # this if condition ensures, the number will be generated only if low != high
        # low == high means an error in the randint function 
        if low != high:
            number = random.randint(low,high)
        else:
            number = low #low or high anything works, becuase they are just the same. 
        
        print(number)
        answer = input(f"If high, put 'H', if low, put 'L', if correct - put 'C': ").lower()
        if answer == 'h':
            high = number - 1
        elif answer == 'l':
            low = number + 1

    print("Yey, Computer got your number correctly!")

guess_computer(1000)



