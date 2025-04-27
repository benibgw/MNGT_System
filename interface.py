import tkinter as tk
from tkinter import messagebox
from MNGT_DB import check_access

def acessWindow():
    root = tk.Tk()
    root.title("MNGT System")
    root.geometry("225x200")
    root.resizable(False, False)


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
    
    label1 = tk.Label(root, text="Type your access code and access key")
    label1.grid(row=0, column=1, padx=10, pady=10)

    textbox1 = tk.Entry(root, width=25)
    textbox1.grid(row=1, column=1, padx=10, pady=10)

    textbox2 = tk.Entry(root, width=25)
    textbox2.grid(row=2, column=1, padx=10, pady=10)
    textbox2.config(show="*")

    button1 = tk.Button(root, text="Access", command=access,)
    button1.grid(row=3, column=1, padx=10, pady=10)

    root.mainloop()

def mainWindow():
    root = tk.Tk()
    root.title("MNGT System")
    root.geometry("1280x720")

    label1 = tk.Label(root, text="Welcome to MNGT System\n More features coming soon...", font=("Arial", 24))
    label1.place(relx=0.5, rely=0.5, anchor="center")

    root.mainloop()

acessWindow()