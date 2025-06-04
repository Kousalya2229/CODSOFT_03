import tkinter as tk
from tkinter import messagebox
import string
import random

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length should be at least 4.")
            return
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text=password)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Set up GUI window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")
root.config(bg="#f0f0f0")

tk.Label(root, text="🔐 Password Generator", font=("Helvetica", 16, "bold"), bg="#f0f0f0").pack(pady=10)

tk.Label(root, text="Enter Password Length:", font=("Helvetica", 12), bg="#f0f0f0").pack()
length_entry = tk.Entry(root, font=("Helvetica", 12), justify='center')
length_entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Password", font=("Helvetica", 12), command=generate_password)
generate_btn.pack(pady=10)

tk.Label(root, text="Generated Password:", font=("Helvetica", 12, "bold"), bg="#f0f0f0").pack()
result_label = tk.Label(root, text="", font=("Helvetica", 12), fg="blue", bg="#f0f0f0")
result_label.pack(pady=5)

root.mainloop()
