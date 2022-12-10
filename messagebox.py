from tkinter import messagebox
import tkinter as tk

window = tk.Tk()
window.title('Messagebox')
window.geometry('500x200')


def info():
    messagebox.showinfo('Info Title', 'Info content')


def warn():
    messagebox.showwarning('Warning', 'This is a warning message')


def ques():
    messagebox.askquestion('Question', 'This is a question')


def okcancl():
    messagebox.askokcancel('Ok or Cancel', "?")


bt1 = tk.Button(window, text='.showinfo', command=info).pack()
bt2 = tk.Button(window, text='.showwarning', command=warn).pack()
bt3 = tk.Button(window, text='.askquestion', command=ques).pack()
bt4 = tk.Button(window, text='.askokcancel', command=okcancl).pack()
window.mainloop()
