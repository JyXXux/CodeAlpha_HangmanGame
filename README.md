# 🎮 Hangman Game – README

A simple yet feature-rich **text-based Hangman game** written in Python. This project is designed for beginners learning loops, conditionals, lists, functions, and basic console interaction.

---

## 📌 Features

### ✔ **1. Menu Screen**

The game starts with a clean menu that lets the player:

* Start a new game
* Exit the program

This provides a smooth and structured user experience.

### ✔ **2. Difficulty Levels**

Players can select from three difficulty levels:

* **Easy** → 10 lives, simple words
* **Medium** → 6 lives, moderate-length words
* **Hard** → 4 lives, more complex words

Each difficulty level uses a different word list to match the challenge.

### ✔ **3. ASCII Art Hangman**

The game displays a dynamic Hangman ASCII art figure that updates with every incorrect guess. The art consists of **7 stages**, ranging from a blank gallows to the complete figure.

### ✔ **4. Replay System**

After the player wins or loses, the game prompts:

> *"Do you want to play again? (yes/no)"*

Choosing **yes** restarts the game without exiting the program.

### ✔ **5. Clear Screen Function**

The terminal automatically clears after:

* Menu selections
* Starting a new round
* Entering each guess

This keeps the interface uncluttered and professional.

### ✔ **6. Random Word Selection**

The game is capable of selecting random words from:

* Predefined word lists
* (Optionally) larger dictionaries or APIs

This ensures each round feels fresh.

---

## 🧠 Concepts Demonstrated

This Hangman game is ideal for learning or teaching the following Python fundamentals:

### 🔹 **random Module**

Used to select a random word from a list.

### 🔹 **Loops**

* `while` loop for running the main game cycle.

### 🔹 **Conditionals (if-else)**

Used extensively to:

* Validate user input
* Check guesses
* Update lives and word display

### 🔹 **Lists & Strings**

* List of words per difficulty
* List for storing guessed letters
* List for the displayed blanks and correct letters

### 🔹 **Functions**

The game is modularized using functions:

* `play_game()` → Runs the Hangman round
* `main_menu()` → Controls navigation
* `clear_screen()` → Maintains UI cleanliness

---

## 📂 Code Structure (Overview)

```
project-folder/
│
├── hangman.py        # Main game file
├── readme.md         # Documentation
└── assets/           # (Optional) Extra word lists, ASCII art
```

---

## 🎯 How Word Randomization Works

The simplest way:

1. Create a list of words:

   ```python
   words = ["python", "school", "guitar"]
   ```
2. Use `random.choice()` to pick one word:

   ```python
   secret_word = random.choice(words)
   ```

This gives each playthrough a unique experience.

Advanced options include loading words from files or using APIs, but the basic version keeps everything offline and simple.

---

## 🚀 How to Run the Game

1. Install Python (if not already installed).
2. Save the hangman code into a file named, for example, `hangman.py`.
3. Open a terminal and run:

   ```
   python hangman.py
   ```
4. Enjoy the game!

---

## 🛠 Future Improvements (Optional)

You can enhance the game by adding:

* High score system
* Colorful text output
* Sound effects using Python libraries
* Larger dictionary using external files
* Hints system

---

## 📖 License

This project is open for educational and personal use.

Feel free to modify, improve, or expand it as needed!

---


