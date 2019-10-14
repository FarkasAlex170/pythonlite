import random
from time import sleep

POSITIVE_SAYINGS = ["Well done!", "Great!", "Minimum Johnny Bravo!", "Awesome!", "Nice one son"]
words = ["apple", "johnny", "gipsy", "winter", "codecool", 
"tekken", "barcelona", "cool", "cunt", "hope", "mobile",
"nemesis", "example", "index", "break", "blood", "bleed",
"thanos", "iniesta", "thiago", "jersey", "batman", "winchester"]
word = random.choice(words).upper()
max_wrong = len(word) - 1
so_far = ("-") * len(word)
used = []
wrong = 0

print("\t" * 5 + "WELCOME TO HANGMAN!" + "\n"*3)
name = input("What's your name?: ").upper()
print("\n" * 5 + "Hello " + name + " let's have some fun!" + "\n" * 10 )
print()
input("Press Enter to START: ")

while wrong < max_wrong and so_far != word:
    print()
    print("Word so far: ", so_far)
    print("Letters used: ", used)

    guess = input("Guess a letter " + name + " brov?:").upper()
    sleep(0.5)
    print()

    while guess in used:
        print("Try again....You've already used this letter ")    
        guess = input("Guess a letter brov: ").upper()
        sleep(0.5)
        print()
    used.append(guess)

    if guess in word:
        print(random.choice(POSITIVE_SAYINGS), "...Updating word so far....")

        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess

            else:
                new += so_far[i]
        so_far = new

    else:
        print("Fucked up! Try again!")
        wrong += 1

sleep(1)
if wrong == max_wrong:
    print("Idiot! Get some common sense!")
    print("That is the one you did NOT know: " + word)
else:
    print("Brilliant! Congratulations!")

print()
print()
print("If you wanna play again Run this crap in terminal!")
input("Press Enter to LEAVE: ")


