'''
Containerised set of importable functions; purpose is to allow cleaner, shorter code chunks.
'''

#libraries
import tkinter as tk
from tkinter import messagebox

#window box
def msgbox(title, message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(title, message)
    root.destroy()
