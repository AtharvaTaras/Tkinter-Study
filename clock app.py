import tkinter as tk
from datetime import datetime

window = tk.Tk()
window.title('Clock')
window.resizable(0, 0)

l1 = tk.Label(text='Time',
              font=('Arial Bold', 50),
              bg='#000000',
              fg='#6b005f')
l1.pack()

b1 = tk.Button(text='Close',
               command=tk._exit,
               bg='#000000',
               fg='#6b005f')
b1.pack(fill='x')


def update():
    now = datetime.now().strftime("%H:%M:%S")
    l1.config(text=now)
    l1.after(1, update)


update()
window.mainloop()
