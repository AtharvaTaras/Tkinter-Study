from tkinter.ttk import *
import tkinter as tk

window = tk.Tk()
window.title('Checkbutton')
window.geometry('500x500')

chk_state = tk.BooleanVar()
chk_state.set(True)

chk = Checkbutton(window, text='Select', var=chk_state)
chk.grid(column=0, row=0)

window.mainloop()