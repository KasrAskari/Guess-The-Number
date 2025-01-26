import random

def guess_the_number():
    print("Think of a number between 1 and 99 and don't tell me!")
    input("Press Enter when you're ready.")

    low, high = 1, 99

    while True:
        guess = random.randint(low, high)
        print(f"Is your number {guess}?")

        user_input = input("Enter 'k' if your number is smaller, 'b' if bigger, 'd' if correct: ").strip().lower()

        if user_input == 'd':
            print(f"Hurray! I guessed it right: {guess}!")
            break
        elif user_input == 'k':
            high = guess - 1
        elif user_input == 'b':
            low = guess + 1
        else:
            print("Invalid input, please enter 'k', 'b', or 'd'.")

# Run the game
guess_the_number()