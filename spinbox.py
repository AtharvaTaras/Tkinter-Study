import tkinter as tk

window = tk.Tk()
window.title('Spinbox')
window.geometry('500x500')

spin = tk.Spinbox(window, from_=0, to=100, width=10)
spin.grid(column=0, row=0)

window.mainloop()