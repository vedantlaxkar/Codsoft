import tkinter as tk
import random
from PIL import Image, ImageTk

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors Game")

        self.user_score = 0
        self.computer_score = 0
        self.image_path = "C:/Users/USER/Desktop/codsoft/images/"

        self.choices = ["rock", "paper", "scissors"]

        self.user_choice_label = tk.Label(root, text="Your choice:", font=("Helvetica", 16, "bold"))
        self.user_choice_label.grid(row=3, column=0, padx=10, pady=10)

        self.computer_choice_label = tk.Label(root, text="Computer's choice:", font=("Helvetica", 16, "bold"))
        self.computer_choice_label.grid(row=5, column=0, padx=10, pady=10)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"))
        self.result_label.grid(row=3, column=1, columnspan=4, padx=10, pady=10)

        self.user_score_label = tk.Label(root, text="Your score: 0", font=("Helvetica", 16, "bold"))
        self.user_score_label.grid(row=4, column=1, columnspan=4, padx=10, pady=10)

        self.computer_score_label = tk.Label(root, text="Computer's score: 0", font=("Helvetica", 16, "bold"))
        self.computer_score_label.grid(row=5, column=1, columnspan=5, padx=10, pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", font=("Helvetica", 16, "bold"), command=self.play_again)
        self.play_again_button.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

        self.user_image_label = tk.Label(root)
        self.user_image_label.grid(row=3, column=1, padx=10, pady=10)

        self.computer_image_label = tk.Label(root)
        self.computer_image_label.grid(row=5, column=1, padx=10, pady=10)

        self.create_choice_buttons()

        root.grid_rowconfigure(6, weight=1)
        for i in range(3):
            root.grid_columnconfigure(i+1, weight=1)

    def create_choice_buttons(self):
        row = 0
        for idx, choice in enumerate(self.choices):
            button = tk.Button(self.root, text=choice.capitalize(), font=("Helvetica", 16, "bold"), command=lambda c=choice: self.play(c))
            button.grid(row=row, column=idx+1, padx=10, pady=10, sticky="nsew")

    def play(self, user_choice):
        computer_choice = random.choice(self.choices)
        self.display_choices(user_choice, computer_choice)
        result = self.determine_winner(user_choice, computer_choice)
        self.display_result(result)
        self.update_score(result)
        self.update_images(user_choice, computer_choice)

    def display_choices(self, user_choice, computer_choice):
        self.user_choice_label.config(text="Your choice: " + user_choice.capitalize())
        self.computer_choice_label.config(text="Computer's choice: " + computer_choice.capitalize())

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            return "You win!"
        else:
            return "Computer wins!"

    def display_result(self, result):
        self.result_label.config(text=result)

    def update_score(self, result):
        if result == "You win!":
            self.user_score += 1
        elif result == "Computer wins!":
            self.computer_score += 1
        self.user_score_label.config(text="Your score: " + str(self.user_score))
        self.computer_score_label.config(text="Computer's score: " + str(self.computer_score))

    def update_images(self, user_choice, computer_choice):
        user_image_path = self.image_path + f"{user_choice}.png"
        computer_image_path = self.image_path +  f"{computer_choice}.png"

        user_image = Image.open(user_image_path).resize((100, 100))
        computer_image = Image.open(computer_image_path).resize((100, 100))

        user_photo = ImageTk.PhotoImage(user_image)
        computer_photo = ImageTk.PhotoImage(computer_image)

        self.user_image_label.config(image=user_photo)
        self.user_image_label.image = user_photo

        self.computer_image_label.config(image=computer_photo)
        self.computer_image_label.image = computer_photo

    def play_again(self):
        self.user_score = 0
        self.computer_score = 0
        self.user_score_label.config(text="Your score: 0")
        self.computer_score_label.config(text="Computer's score: 0")
        self.result_label.config(text="")
        self.user_choice_label.config(text="Your choice:")
        self.computer_choice_label.config(text="Computer's choice:")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("800x400")
    game = RockPaperScissorsGame(root)
    root.mainloop()