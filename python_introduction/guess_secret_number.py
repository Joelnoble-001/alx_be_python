# guess secret number game

# import random module
import random


while True:
    # define the variable to guess the secret number
    secret_number = random.randint(1, 10)
    guess_count = 0 # to track the number of guesses
    max_guesses = 2 #maximum number of guesses allowed before user is asked to play again

    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while guess_count < max_guesses:
        try:
            guess = int(input("Guess the secret number between 1 and 10: "))
            guess_count += 1

            match guess:
                case _ if guess == secret_number:
                    print("Congratulations, you guessed it!")
                    break
                case _ if guess > secret_number:
                    if guess_count < max_guesses:
                        print("Oops, your guess is a bit high. Try again!")
                    else:
                        print(f"Sorry, you've used all your guesses.")
                case _ if guess < secret_number:
                    if guess_count < max_guesses:
                        print("Nope, your guess is a bit low. Give it another shot!")
                    else:
                        print(f"Sorry, you've used all your guesses.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue
    

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            break
    else:
            print("Let's play again!")
            # Reset the game