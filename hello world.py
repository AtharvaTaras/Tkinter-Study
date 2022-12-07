import tkinter as tk

window = tk.Tk()
window.title('My First Python GUI')

# Pack = show object in window
label = tk.Label(window, text='hello world!').pack()

window.mainloop()