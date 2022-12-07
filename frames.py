import tkinter as tk

window = tk.Tk()
window.title('Frames')
window.geometry('200x200')

top_frame = tk.Frame(window).pack()
bot_frame = tk.Frame(window).pack(side='bottom')

bt1 = tk.Button(top_frame, text='Click here!', bg='#7F7FFF').pack(fill='x')
bt2 = tk.Button(top_frame, text='Click here!').pack()

bt3 = tk.Button(top_frame, text='Click here!', bg='#7F7FFF').pack(side='left', fill='y')
bt4 = tk.Button(top_frame, text='Click here!').pack(side='left')

window.mainloop()