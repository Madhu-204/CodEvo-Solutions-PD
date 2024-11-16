class NumberGuessingGame:
    def _init_(self,master):
        self.master = master
        self.master.title("Number Guessing Game")

        self.number_to_guess =random.randint(1,100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 100")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.guess_button = tk.Button(master, text='Guess',command = self.check_guess)
        self.guess_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.attempts_label = tk.Label(master, text="")
        self.attempts_label.pack()

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < 1 or guess > 100:
                self.result_label.config(text="Please guess number within the range.")
            elif guess < self.number_to_guess:
                self.result_label.config(text="Too Low! Try Again.")
            elif guess > self.number_to_guess:
                self.reult_label.config(text="Too High! Try Again.")
            else:
                self.result_label.config(text=f"Congratulation! You have guess the correct numnber.")
                self.attempts_label.config(text=f"It took you{self.attempts} attempts.")
                self.entry.config(state='disabled')

        except:
            self.result_label.config(text="Invalid Input Please enter a valid number!")
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame()
    root.mainloop()