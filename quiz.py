def new_game():
    print("game has started")
    guesses = []
    correct_guess = 0

    question_number = 1

    for question in questions:
        print(question)
        for answer in answers[question_number - 1]:
            print(answer)
        guess = input("Enter 1, 2, 3 or 4: ")
        guesses.append(guess)

        correct_guess += check_answer(questions.get(question), guess)
        question_number += 1

    score_value(correct_guess, guesses)


def check_answer(answer, guess):
    if answer == guess:
        print("you are correct")
        return 1
    else:
        print("you are wrong")
        return 0


def score_value(correct_guesses, guesses):
    print("Answers:", end=" ")
    for ans in questions:
        print(questions.get(ans), end=" ")
    print()
    print("Guesses:", end=" ")
    for guess in guesses:
        print(guess, end=" ")
    print()
    score = int((correct_guesses / len(questions)) * 100)
    print("Your score :" + str(score))


def play_again():
    response = input("do you wanna play again? (yes / no)")
    print(response)
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


questions = {
    "what is the color of parrot?": "1",
    "what is the biggest river?": "2",
    "who develop the python?": "1",
    "can you tell what is the wild animals in the given below?": "3"
}

answers = [["1.green", "2.yellow", "3.blue", "4.red"],
           ["1.amazon", "2.neil", "3.sahara", "4.ganga"],
           ["1.Guido van Rossu", "2.Elon Musk", "3.Bill Gates", "4.Mark Zuckerburg"],
           ["1.pig", "2.elephant", "3.Lion", "4.dog"]]

new_game()

while play_again():
      new_game()

print("chio")
