import tkinter as tk

window = tk.Tk()
window.title('Buttons')
window.geometry('500x500')

l1 = tk.Label(window, text='Label 1', font=('Arial Bold', 15))
l1.grid(column=0, row=3)

def clicked():
    l1.configure(text='Button was clicked!')


bt1 = tk.Button(window, text='Ok')
bt1.grid(column=1, row=0)

bt2 = tk.Button(window,
                text='Hehehehehe',
                bg='black',
                fg='white',
                command=clicked)
bt2.grid(column=2, row=1)

window.mainloop()
