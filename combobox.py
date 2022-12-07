from tkinter.ttk import *
import tkinter as tk

window = tk.Tk()
window.title('Combobox')
window.geometry('500x500')

# Combobox = dropdown
combo = Combobox(window)
combo['values'] = (1, 2, 3, 'Text')
combo.current(3)
combo.grid(column=0, row=0)

window.mainloop()