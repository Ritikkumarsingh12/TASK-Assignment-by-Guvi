print("___________TASK 3 _________BY_____Ritik Kumar Singh_________")
print("\n Guess the Number & word scamble ")
import random


def guess_game():

    print("\n=== GUESS GAME ===")
    print("I'm thinking of a number between 1 and 50.")
    number = random.randint(1, 50)
    guess = 0
    tries = 0

    while guess != number:
        try:
            guess = int(input("Enter your guess: "))
            tries += 1

            if guess < number:
                print("Too small! Try again.")
            elif guess > number:
                print("Too big! Try again.")
            else:
                print(f"Nice! You got it in {tries} tries ")
        except ValueError:
            print("Please enter a valid number!")


def word_puzzle():
    #Word scramble puzzle ,here we gave the word list to choose the word from the list

    print("\n=== WORD PUZZLE ===")
    word_list = ['python', 'testing', 'bug', 'script', 'loop', 'variable']
    chosen = random.choice(word_list)

    #mix the letters in the word randomly to make it jumbled

    letters = list(chosen)
    random.shuffle(letters)
    jumbled = ''.join(letters)

    print(f"Unscramble this: {jumbled}")

#here we have used if else condition & while loop ,it will give the 3 chance fotr guess 

    attempt = 1
    while attempt <= 3:
        guess = input("Your answer: ").strip().lower()
        if guess == chosen:
            print("Correct! Great job.")
            break
        else:
            print(" Wrong ! Try again.")
        attempt += 1

    if attempt > 3:
        print(f"The correct word was '{chosen}'.")


def main():
    while True:
        print("\n1. Guess Game\n2. Word Puzzle\n3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            guess_game()
        elif choice == '2':
            word_puzzle()
        elif choice == '3':
            print("Bye 👋")
            break
        else:
            print("Invalid option! Try again.")


if __name__ == "__main__":
    main()
