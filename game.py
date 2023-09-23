import time
import random

name = input("what is your name?")
print("hello" + name)

player_input = input("are you ready" " " + name + " " + "to play the game (yes/no)?")

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

random_word = random.choice(words)

guesses = ""

turns = 10

while turns > 0:
    failed = 0

    for char in random_word:
        if char in guesses:
            print(char, end="")
        else:
            print('_', end="")
            failed += 1

    if failed == 0:
        print("\n won")
        break
    guess = input("\nguess the character:")
    guesses += guess
    if guess in words:
        turns -= 1
        print("\n wrong")
        print("\nyou have", turns, "more guesses")

        if turns == 0:
            print("\nyour turns are completed bye!!")

