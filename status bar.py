import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title('Open File Dialog')
window.geometry('1000x50')


def get_img(empty=None):

    path = filedialog.askopenfilename(initialdir=r'C:\\',
                                      title='Select a file',
                                      filetypes=(
                                          ('PNG Files', '*.png'),
                                          ('JPG Files', '*.jpg'),
                                          ('JPEG Files', '*.jpeg'),
                                          ('BITMAP Files', '*.bmp')
                                      )
                                      )




b1 = tk.Button(text='Select Images',
               command=get_img)
b1.pack()

l1 = tk.Label(text=f'Image Path ---> {path}').pack()

#my_img = tk.PhotoImage(path)

window.mainloop()
