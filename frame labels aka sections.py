import tkinter as tk

window = tk.Tk()
window.title('Frame Labels/Sections')
window.resizable(0, 0)

frame = tk.LabelFrame(window, text='TEST FRAME', padx=10, pady=10)
frame.pack(padx=25, pady=25)

b1 = tk.Button(frame, text='Hehe')
b1.pack()

window.mainloop()
