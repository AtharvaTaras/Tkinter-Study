from tkinter.ttk import *
import tkinter as tk

window = tk.Tk()
window.title('Radio')
window.geometry('500x500')

rad1 = Radiobutton(window, text='Hella', value=1)
rad1.grid(column=0, row=0)
rad2 = Radiobutton(window, text='Black Widow', value=2)
rad2.grid(column=1, row=0)
rad3 = Radiobutton(window, text='Wanda', value=3)
rad3.grid(column=2, row=0)

window.mainloop()