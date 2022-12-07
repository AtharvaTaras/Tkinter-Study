from tkinter import messagebox
import tkinter as tk

window = tk.Tk()
window.title('Messagebox')
window.geometry('500x500')

def clicked():
    messagebox.showinfo('Message title', 'Message content')

bt1 = tk.Button(window, text='Click here!', command=clicked)
bt1.grid(column=0, row=3)


window.mainloop()