# Game.1: Number Guessing Game
""" import random

number_to_guess = random.randint(1, 100)
attempts = 0

while True:
    guessed = int(input("Guess the number between 1 and 100: "))
    attempts += 1

    if guessed == number_to_guess:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guessed < number_to_guess:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")

print("Thanks for playing!") """

# Game.2: Stone Paper Scissors Game

import tkinter as tk
import random

# ---------------- Game Logic ----------------
choices = ["stone", "paper", "scissors"]
user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)
    computer_label.config(text=f"🤖 Computer chose: {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        result_label.config(text="🤝 It's a Tie!", fg="#facc15")
    elif (
        (user_choice == "stone" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "stone") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        user_score += 1
        result_label.config(text="🎉 You Win!", fg="#22c55e")
    else:
        computer_score += 1
        result_label.config(text="💻 Computer Wins!", fg="#ef4444")

    score_label.config(text=f"👤 You: {user_score}   🤖 Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="Game Reset!", fg="#38bdf8")
    computer_label.config(text="")
    score_label.config(text="👤 You: 0   🤖 Computer: 0")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Stone Paper Scissors")
root.geometry("420x520")
root.resizable(False, False)
root.configure(bg="#0f172a")  # Dark background

# Title
tk.Label(
    root,
    text="🎮 Stone Paper Scissors",
    font=("Segoe UI", 20, "bold"),
    fg="#38bdf8",
    bg="#0f172a"
).pack(pady=20)

# Score Card
score_label = tk.Label(
    root,
    text="👤 You: 0   🤖 Computer: 0",
    font=("Segoe UI", 14, "bold"),
    fg="#e5e7eb",
    bg="#1e293b",
    width=28,
    pady=10
)
score_label.pack(pady=10)

# Computer choice
computer_label = tk.Label(
    root,
    text="",
    font=("Segoe UI", 12),
    fg="#e5e7eb",
    bg="#0f172a"
)
computer_label.pack(pady=10)

# Result
result_label = tk.Label(
    root,
    text="Make your move!",
    font=("Segoe UI", 16, "bold"),
    fg="#38bdf8",
    bg="#0f172a"
)
result_label.pack(pady=20)

# Buttons frame
btn_frame = tk.Frame(root, bg="#0f172a")
btn_frame.pack(pady=10)

def styled_button(text, command, color):
    return tk.Button(
        btn_frame,
        text=text,
        font=("Segoe UI", 14, "bold"),
        width=10,
        bg=color,
        fg="white",
        activebackground="#334155",
        activeforeground="white",
        bd=0,
        pady=10,
        command=command
    )

styled_button("🪨 Stone", lambda: play("stone"), "#64748b").pack(pady=8)
styled_button("📄 Paper", lambda: play("paper"), "#0ea5e9").pack(pady=8)
styled_button("✂️ Scissors", lambda: play("scissors"), "#8b5cf6").pack(pady=8)

# Reset button
tk.Button(
    root,
    text="🔄 Reset Game",
    font=("Segoe UI", 12, "bold"),
    bg="#ef4444",
    fg="white",
    activebackground="#b91c1c",
    bd=0,
    width=18,
    pady=8,
    command=reset_game
).pack(pady=25)

root.mainloop()

