import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")

    while True:
        # Get user's name
        name = input("Enter your name: ")

        print(f"\nHello, {name}! I've selected a number between 1 and 100. Try to guess it within 10 attempts.")

        # Generate a random number between 1 and 100
        secret_number = random.randint(1, 100)
        attempts = 0

        while attempts < 10:
            # Get user's guess
            try:
                guess = int(input("Enter your guess: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            # Increment attempts
            attempts += 1

            # Check if the guess is correct
            if guess == secret_number:
                print(f"Congratulations, {name}! You guessed the correct number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        else:
            print(f"Sorry, {name}. You've reached the maximum number of attempts. The correct number was {secret_number}.")

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    number_guessing_game()
