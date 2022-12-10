import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title('Open File Dialog')
window.geometry('1000x50')

window.filename = filedialog.askopenfilename(initialdir=r'C:\\',
                                             title='Select a file',
                                             filetypes=(
                                                 ('PNG Files', '*.png'), ('all files', '*.*')
                                             )
                                             )

print(str(window.filename))

l1 = tk.Label(text=str(window.filename),
              font=('Arial Bold', 15))
l1.pack()
window.mainloop()
