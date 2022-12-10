import tkinter as tk

window = tk.Tk()
window.title('Exit Functions')
window.geometry('200x100')
window.resizable(0, 0)

# Tkinter exit isa bit faster
bt1 = tk.Button(text='Tkinter Exit Method', command=window.quit)
bt1.pack()

bt2 = tk.Button(text='Python Exit Method', command=exit)
bt2.pack()

window.mainloop()
