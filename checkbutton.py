from tkinter.ttk import *
import tkinter as tk

window = tk.Tk()
window.title('Checkbutton')
window.geometry('500x500')


def show_status():
    l1 = tk.Label(window, text=str(chk_state.get())).pack()


chk_state = tk.BooleanVar()
chk_state.set(False)

chk = Checkbutton(window, text='Select', var=chk_state, command=show_status)
chk.pack()

window.mainloop()
