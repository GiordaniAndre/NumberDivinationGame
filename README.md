# Number Guessing Game
This is a simple number guessing game built using Python's tkinter library for the graphical user interface (GUI). The goal is to guess a sequence of 4 random numbers, receiving visual feedback for each attempt. The game allows up to 25 attempts before it ends.
## How to Play
1. Enter a 4-digit number in the input field.
2. Press "Submit" or press Enter on your keyboard to submit your guess.
3. You'll receive feedback based on your guess:
4. Green: The number is correct and in the right position.
5. Yellow: The number is correct but in the wrong position.
6. Red: The number is incorrect.
7. "Give Up" button reveals the correct numbers if you want to stop.
8. "New Game" button starts a new game with a new sequence of numbers.
## Features
1. Up to 25 attempts to guess the correct sequence.
2. Visual feedback with colors to help you refine your guesses.
3. Keyboard shortcut: Press Enter to submit your guess.
4. Option to give up and reveal the correct sequence.
## Installation
Ensure you have Python installed on your machine. tkinter is included by default with most Python installations.
### Run the Game
1. Clone the repository or download the script.
2. Open a terminal and run the following command:
   ```python game.py```
## Dependencies
- Python 3.x
- tkinter (built-in with Python)
## Code Overview
### Key Functions
- generate_numbers(): Generates a random sequence of 4 digits.

- check_attempt(numbers, attempt): Checks the guess and returns which numbers are correct and in the correct or incorrect positions.

- on_submit(event=None): Handles the submission of the guess.

- give_up(): Displays the correct numbers and ends the game.

- reset_game(): Resets the game with a new sequence of numbers.
### UI Elements
- Input Field: For entering the 4-digit guess.

- Buttons:

  - "Submit": Submits your guess.

  - "Give Up": Reveals the correct numbers.

  - "New Game": Resets the game with a new number sequence.

- Grid of Labels: Displays each guess with color-coded feedback.
## Screenshots
## License
This project is licensed under the MIT License.
## Author
André Giordani

Enjoy playing and good luck guessing the numbers!
