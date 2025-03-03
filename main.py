import tkinter as tk
import random
import string
import pyperclip
import tkinter.messagebox as messagebox

def generate_password():
    length = random.randint(8, 30)
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
print (generate_password())


def generate_and_display():
    password = generate_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Bilgi", "Şifre kopyalandı!")

# main window
root = tk.Tk()
root.title("Şifre Üretici")
root.geometry("400x200")
root.resizable(False, False)

# password display area
password_entry = tk.Entry(root, width=30, font=("Arial", 12), justify="center")
password_entry.pack(pady=10)

# buttons
generate_button = tk.Button(root, text="Şifre Üret", command=generate_and_display)
generate_button.pack(pady=5)

copy_button = tk.Button(root, text="Kopyala", command=copy_to_clipboard)
copy_button.pack(pady=5)

# run the interface
root.mainloop()
