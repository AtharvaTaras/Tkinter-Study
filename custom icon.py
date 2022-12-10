import tkinter as tk

window = tk.Tk()
window.title('App Icon')
window.geometry('600x200')
window.resizable(0, 0)
window.iconbitmap('data/my_icon.ico')

window.mainloop()
