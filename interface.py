import tkinter as tk
from tkinter import messagebox
from MNGT_DB import MNGT_DB

root = tk.Tk()
root.title("MNGT System")
window_width = 1280
window_height = 720

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")



root.mainloop()
