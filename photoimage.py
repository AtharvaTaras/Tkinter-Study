import tkinter as tk

window = tk.Tk()
window.title('Photo Image')
window.resizable(0, 0)

icon = tk.PhotoImage(file='data/cat.png')
l1 = tk.Label(window, image=icon)
l1.pack()

tk.mainloop()
