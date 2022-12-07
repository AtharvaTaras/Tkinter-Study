import tkinter as tk

window = tk.Tk()
window.title('Entry')
window.geometry('500x500')

l1 = tk.Label(window, text='😀😀😀', font=('Arial Bold', 20))
l1.grid(column=0, row=0)

txt = tk.Entry(window, width=10)
txt.grid(column=0, row=1)

def clicked():
    res = 'You just typed ' + txt.get()
    l1.configure(text=res)

bt1 = tk.Button(window, text='Enter', command=clicked)
bt1.grid(column=0, row=3)

window.mainloop()