import tkinter as tk
from num2words import num2words

def convert():
    try:
        num = float(entry.get())
        words = num2words(num).title()
        result_label.config(text=f"In words:\n{words}")
    except:
        result_label.config(text="Please enter a valid number.")

root = tk.Tk()
root.title("Number To Text Converter")
root.geometry("300x180")

tk.Label(root, text="Enter a number:").pack(pady=5)
entry = tk.Entry(root, font=("Arial", 15))
entry.pack()

tk.Button(root, text="Convert", command=convert).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 15), wraplength=250)
result_label.pack()

root.mainloop()
