import tkinter as tk
from tkinter import messagebox
import random

# Generate a secret number
secret_number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    guess = entry_guess.get().strip()

    if not guess.isdigit():
        messagebox.showwarning("Oops!", "Please type a valid number between 1 and 100.")
        return

    guess = int(guess)
    if guess < 1 or guess > 100:
        messagebox.showwarning("Out of Range", "Please guess a number *within* 1 to 100.")
        return

    attempts += 1

    if guess < secret_number:
        feedback.set("Too low! Try a bit higher.")
    elif guess > secret_number:
        feedback.set("Too high! Try a bit lower.")
    else:
        feedback.set(f" Woohoo! You got it in {attempts} tries!")
        btn_check.config(state="disabled")
        entry_guess.config(state="disabled")
        btn_play_again.config(state="normal")

def play_again():
    global secret_number, attempts
    secret_number = random.randint(1, 100)
    attempts = 0
    feedback.set("")
    entry_guess.delete(0, tk.END)
    entry_guess.config(state="normal")
    btn_check.config(state="normal")
    btn_play_again.config(state="disabled")

# GUI Setup
root = tk.Tk()
root.title("🎲 Number Guessing Game")
root.geometry("380x280")
root.resizable(False, False)

tk.Label(root, text="Welcome! Can you guess the number I'm thinking of?\n(Hint: It's between 1 and 100)", 
         font=("Segoe UI", 11), justify="center").pack(pady=15)

entry_guess = tk.Entry(root, width=18, font=("Segoe UI", 12), justify="center")
entry_guess.pack()

btn_check = tk.Button(root, text="Guess!", font=("Segoe UI", 10, "bold"), command=check_guess)
btn_check.pack(pady=10)

feedback = tk.StringVar()
tk.Label(root, textvariable=feedback, fg="#007acc", font=("Segoe UI", 11, "italic")).pack(pady=10)

btn_play_again = tk.Button(root, text="Play Again", font=("Segoe UI", 9), command=play_again, state="disabled")
btn_play_again.pack(pady=5)

# Start the GUI
root.mainloop()
