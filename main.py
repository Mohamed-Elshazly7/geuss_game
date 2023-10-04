import random


def guess_the_number():
    number_to_guess = random.randint(1, 30)
    attempts = 0

    print("Welcome to the guess the number game")
    print("Guessing from number 1 to number 30")

    while True:
        user_guess = int(input("Please enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("The number is larger Try again")
        elif user_guess > number_to_guess:
            print("The number is smaller Try again")
        else:
            print(f"Congratulations! You guessed the correct number {number_to_guess} in {attempts} attempts")
            break

        if attempts >= 3:
            print(f"All attempts have been completed. The correct number was: {number_to_guess}")
            break

guess_the_number()
