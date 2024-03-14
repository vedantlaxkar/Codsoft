import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")

        # Entry widget to display input and output
        self.display = tk.Entry(root, width=20, font=("Arial", 16))
        self.display.grid(row=0, column=0, columnspan=4)

        # Buttons for digits and operations
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]
        for i, label in enumerate(buttons):
            row = 1 + i // 4
            col = i % 4
            tk.Button(root, text=label, width=5, height=2, command=lambda l=label: self.on_button_click(l)).grid(row=row, column=col)

    def on_button_click(self, label):
        if label == '=':
            result = eval(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(result))
        elif label == 'C':
            self.display.delete(0, tk.END)
        else:
            self.display.insert(tk.END, label)

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()