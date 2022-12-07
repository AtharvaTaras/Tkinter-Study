import tkinter as tk

window = tk.Tk()
window.title('Labels')
window.geometry('350x350')

l1 = tk.Label(window, text='Label 1', font=('Arial Bold', 50))
l1.grid(column=0, row=0)

l2 = tk.Label(window, text='Label 2', font=('Arial Italic', 50))
l2.grid(column=0, row=1)


window.mainloop()