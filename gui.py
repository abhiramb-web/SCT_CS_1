import tkinter as tk
from tkinter import messagebox




def encrypt(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def decrypt(message, shift):
    return encrypt(message, -shift)



def encrypt_text():
    try:
        message = message_entry.get()
        shift = int(shift_entry.get())

        encrypted = encrypt(message, shift)
        result_label.config(text=encrypted)

    except ValueError:
        messagebox.showerror("Error", "Shift value must be a number!")


def decrypt_text():
    try:
        message = message_entry.get()
        shift = int(shift_entry.get())

        decrypted = decrypt(message, shift)
        result_label.config(text=decrypted)

    except ValueError:
        messagebox.showerror("Error", "Shift value must be a number!")


def clear_fields():
    message_entry.delete(0, tk.END)
    shift_entry.delete(0, tk.END)
    result_label.config(text="Result will appear here")

def about():
    messagebox.showinfo(
        "About",
        "Caesar Cipher Tool\n\n"
        "SkillCraft Technology Internship\n"
        "Task 1\n\n"
        "Developed by:\n"
        "B Abhiram"
    )


window = tk.Tk()

window.title(" Welcome to the Caesar Cipher Encryption & decryption Tool")
window.geometry("650x450")
window.resizable(False, False)
window.configure(bg="black")


title = tk.Label(
    window,
    text="Caesar Cipher Tool",
    font=("Times new roman", 22, "bold"),
    bg="black",
    fg="white"
)
title.pack(pady=20)


tk.Label(
    window,
    text="Message",
    font=("Times new roman", 14),
    bg="black",
    fg="white"
).pack()

message_entry = tk.Entry(
    window,
    width=40,
    font=("Times new roman", 14)
)
message_entry.pack(pady=5)


tk.Label(
    window,
    text="Shift",
    font=("Times new roman", 14),
    bg="black",
    fg="white"
).pack()

shift_entry = tk.Entry(
    window,
    width=10,
    font=("Times new roman", 14)
)
shift_entry.pack(pady=5)


button_frame = tk.Frame(window, bg="black")
button_frame.pack(pady=15)

encrypt_button = tk.Button(
    button_frame,
    text="Encrypt",
    width=12,
    bg="green",
    fg="white",
    command=encrypt_text
)
encrypt_button.grid(row=0, column=0, padx=10)

decrypt_button = tk.Button(
    button_frame,
    text="Decrypt",
    width=16,
    bg="violet",
    fg="white",
    command=decrypt_text
)
decrypt_button.grid(row=0, column=1, padx=10)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    width=12,
    command=clear_fields
)
clear_button.grid(row=0, column=2, padx=10)

about_button = tk.Button(
    button_frame,
    text="About",
    width=12,
    bg="dodgerblue",
    fg="white",
    command=about
)
about_button.grid(row=0, column=3, padx=10)


tk.Label(
    window,
    text="Result",
    font=("Times new roman", 14, "bold"),
    bg="black",
    fg="white"
).pack(pady=10)

result_label = tk.Label(
    window,
    text="Result will appear here",
    font=("Times new roman", 14),
    bg="black",
    fg="white",
    wraplength=550
)
result_label.pack(pady=10)


window.mainloop()