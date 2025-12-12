import random
import os

# ---------------- Function to Clear Screen ---------------- #
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# ---------------- Hangman ASCII Art ---------------- #
hangman_stages = [
    """
       _______
      |       |
      |       O
      |      /|\\
      |      / \\
      |
    ===========
    """,
    """
       _______
      |       |
      |       O
      |      /|\\
      |      /
      |
    ===========
    """,
    """
       _______
      |       |
      |       O
      |      /|\\
      |
      |
    ===========
    """,
    """
       _______
      |       |
      |       O
      |      /|
      |
      |
    ===========
    """,
    """
       _______
      |       |
      |       O
      |
      |
      |
    ===========
    """,
    """
       _______
      |       |
      |
      |
      |
      |
    ===========
    """,
    """
       
       
       
       
       
    ===========
    """
]

# ---------------- Word Lists by Difficulty ---------------- #
easy_words = ["cat", "dog", "sun", "hat", "ball"]
medium_words = ["python", "school", "planet", "guitar", "flower"]
hard_words = ["hangman", "computer", "keyboard", "dinosaur", "internet"]

# ---------------- Game Function ---------------- #
def play_game():
    clear_screen()
    print("Choose Difficulty:")
    print("1. Easy (10 lives)")
    print("2. Medium (6 lives)")
    print("3. Hard (4 lives)")

    # Difficulty selection
    while True:
        choice = input("Enter choice (1/2/3): ")
        if choice == "1":
            word_list = easy_words
            lives = 10
            break
        elif choice == "2":
            word_list = medium_words
            lives = 6
            break
        elif choice == "3":
            word_list = hard_words
            lives = 4
            break
        else:
            print("Invalid input! Try again.")

    secret_word = random.choice(word_list)
    display = ["_"] * len(secret_word)
    guessed_letters = []
    wrong_attempts = 0  # track wrong guesses

    clear_screen()
    print("🎮 Game Started! Guess the word.\n")

    # Game Loop
    while lives > 0 and "_" in display:
        print(hangman_stages[wrong_attempts])
        print("Word:", " ".join(display))
        print("Guessed letters:", guessed_letters)
        print("Lives remaining:", lives, "\n")

        guess = input("Enter a letter: ").lower()
        clear_screen()

        if len(guess) != 1 or not guess.isalpha():
            print("⚠ Enter a single valid letter!\n")
            continue

        if guess in guessed_letters:
            print("⚠ You already guessed that!\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("✔ Correct!\n")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    display[i] = guess
        else:
            print("✖ Wrong!\n")
            wrong_attempts += 1
            lives -= 1

    # Result
    print(hangman_stages[wrong_attempts])
    if "_" not in display:
        print("🎉 You WON! The word was:", secret_word)
    else:
        print("💀 You LOST! The word was:", secret_word)

# ---------------- Main Menu Loop ---------------- #
def main_menu():
    while True:
        clear_screen()
        print("=========================")
        print("       HANGMAN GAME      ")
        print("=========================")
        print("1. Play Game")
        print("2. Exit")
        option = input("Choose an option: ")

        if option == "1":
            play_game()
            again = input("\nDo you want to play again? (yes/no): ").lower()
            if again != "yes":
                clear_screen()
                print("Thank you for playing! 👋")
                break

        elif option == "2":
            clear_screen()
            print("Goodbye! 👋")
            break

        else:
            print("Invalid choice! Try again.\n")

# Run menu
main_menu()
