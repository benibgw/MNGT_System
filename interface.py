import tkinter as tk
from tkinter import messagebox
from usersDB import register_user, login_user

def register():
    name = entry_name.get()
    password = entry_password.get()
    if name and password:
        register_user(name, password)
        messagebox.showinfo("Success", "User registered successfully!")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def login():
    name = entry_name.get()
    password = entry_password.get()
    if login_user(name, password):
        messagebox.showinfo("Success", "Login successful!")
    else:
        messagebox.showerror("Error", "Invalid username or password.")

root = tk.Tk()
root.title("MNGT System")
window_width = 300
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.geometry("300x200+0+0")

tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=10)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10)
entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

btn_register = tk.Button(root, text="Register", command=register)
btn_register.grid(row=2, column=0, padx=10, pady=10)

btn_login = tk.Button(root, text="Login", command=login)
btn_login.grid(row=2, column=1, padx=10, pady=10)

root.mainloop() 