import random
import tkinter as tk
from tkinter import messagebox

def generate_numbers():
    return [random.randint(0, 9) for _ in range(4)]

def check_attempt(numbers, attempt):
    correct_positions = []
    correct_numbers = []
    
    temp_numbers = numbers.copy()
    temp_attempt = attempt.copy()
    
    for i in range(4):
        if attempt[i] == numbers[i]:
            correct_positions.append(i)
            temp_numbers[i] = None
            temp_attempt[i] = None
    
    for i in range(4):
        if temp_attempt[i] is not None and temp_attempt[i] in temp_numbers:
            correct_numbers.append(i)
            temp_numbers[temp_numbers.index(temp_attempt[i])] = None
    
    return correct_positions, correct_numbers

def on_submit(event=None):
    attempt_str = entry.get()
    
    if len(attempt_str) != 4 or not attempt_str.isdigit():
        messagebox.showerror("Error", "Please enter exactly 4 digits.")
        return
    
    attempt = [int(num) for num in attempt_str]
    
    correct_positions, correct_numbers = check_attempt(numbers, attempt)
    
    row = len(attempts)
    for i in range(4):
        label = tk.Label(frame, text=str(attempt[i]), font=("Arial", 18), width=4, height=2, borderwidth=2, relief="ridge")
        if i in correct_positions:
            label.config(bg="green", fg="white")
        elif i in correct_numbers:
            label.config(bg="yellow", fg="black")
        else:
            label.config(bg="red", fg="white")
        label.grid(row=row, column=i, padx=5, pady=5)
    
    attempts.append(attempt)
    
    if len(correct_positions) == 4:
        messagebox.showinfo("Congratulations!", f"You guessed the numbers in {len(attempts)} attempts!")
        entry.config(state="disabled")
        submit_button.config(state="disabled")
    elif len(attempts) >= 25:
        messagebox.showinfo("Game Over", f"You reached the limit of 25 attempts. The numbers were: {numbers}")
        entry.config(state="disabled")
        submit_button.config(state="disabled")

def give_up():
    messagebox.showinfo("Give Up", f"The numbers were: {numbers}")
    entry.config(state="disabled")
    submit_button.config(state="disabled")

def reset_game():
    global numbers, attempts
    numbers = generate_numbers()
    attempts = []
    for widget in frame.winfo_children():
        widget.destroy()
    entry.config(state="normal")
    submit_button.config(state="normal")
    entry.delete(0, tk.END)
    messagebox.showinfo("New Game", "A new game has started!")

# Initialize the interface
attempts = []
numbers = generate_numbers()

root = tk.Tk()
root.title("Number Guessing Game")

frame = tk.Frame(root)
frame.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 18), width=10)
entry.pack(pady=10)
entry.bind("<Return>", on_submit)

submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=on_submit)
submit_button.pack(pady=5)

give_up_button = tk.Button(root, text="Give Up", font=("Arial", 14), command=give_up)
give_up_button.pack(pady=5)

reset_button = tk.Button(root, text="New Game", font=("Arial", 14), command=reset_game)
reset_button.pack(pady=5)

root.mainloop()
