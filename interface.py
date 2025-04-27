import tkinter as tk
from tkinter import messagebox
from MNGT_DB import check_access

def acessWindow():
    root = tk.Tk()
    root.title("MNGT System")
    window_width = 275
    window_height = 200

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def access(): 
        accessCode = textbox1.get()
        accessKey = textbox2.get()
        result = check_access(accessCode, accessKey)
        if result == None:
            messagebox.showerror("Error", "Access code or access key is incorrect")
        else:
            messagebox.showinfo("Success", "Access granted")
            root.destroy()
            mainWindow()
    
    label1 = tk.Label(root, text="Type your access code and access key",)
    label1.grid(row=0, column=1, padx=10, pady=10)

    textbox1 = tk.Entry(root, width=30)
    textbox1.grid(row=1, column=1, padx=10, pady=10)

    textbox2 = tk.Entry(root, width=30)
    textbox2.grid(row=2, column=1, padx=10, pady=10)
    textbox2.config(show="*")

    button1 = tk.Button(root, text="Access", command=access,)
    button1.grid(row=3, column=1, padx=10, pady=10)

    root.mainloop()

def mainWindow():
    root = tk.Tk()
    root.title("MNGT System")
    window_width = 1280
    window_height = 720

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label1 = tk.Label(root, text="Welcome to MNGT System\n More features coming soon...", font=("Arial", 24))
    label1.grid(row=1, column=1, padx=10, pady=10)

    root.mainloop()
