import tkinter as tk

window = tk.Tk()
window.title('Grids')
window.geometry('300x200')

tk.Label(window, text='Name').grid(row=0)
tk.Entry(window).grid(row=0, column=1)

tk.Label(window, text='Password').grid(row=1)
tk.Entry(window).grid(row=1, column=1)

tk.Checkbutton(window, text='Remember me').grid(columnspan=2)

window.mainloop()