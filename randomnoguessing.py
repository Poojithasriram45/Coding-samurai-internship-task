import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")
        master.geometry("350x250")
        master.resizable(False, False)

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.title_label = tk.Label(master, text="Guess a number between 1 and 100", font=("Arial", 14))
        self.title_label.pack(pady=10)

        self.entry = tk.Entry(master, font=("Arial", 12), justify='center')
        self.entry.pack(pady=5)

        self.result_label = tk.Label(master, text="hey guys", font=("Arial", 12))
        self.result_label.pack(pady=5)

        self.submit_button = tk.Button(master, text="Submit Guess", command=self.check_guess, bg="#4caf50", fg="white", font=("Arial", 12))
        self.submit_button.pack(pady=5)

        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game, bg="#f44336", fg="white", font=("Arial", 12))
        self.reset_button.pack(pady=5)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < 1 or guess > 100:
                self.result_label.config(text="Please guess a number between 1 and 100")
            elif guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.")
            elif guess > self.secret_number:
                self.result_label.config(text="Too high! Try again.")
            else:
                self.result_label.config(text=f"Correct! It took you {self.attempts} tries.")
        except ValueError:
            self.result_label.config(text="Please enter a valid number.")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
