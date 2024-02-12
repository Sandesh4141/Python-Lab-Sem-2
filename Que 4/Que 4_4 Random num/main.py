import random

def guess_number():
    # random number between 1 and 100
    num_to_guess = random.randint(1, 100)
    attempts = 0

    print("I have chosen a number between 1 and 100. Try to guess it.")

    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
            attempts += 1

            if guess < num_to_guess:
                print("Too low! Try again.")
            elif guess > num_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {num_to_guess} correctly in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    guess_number()
