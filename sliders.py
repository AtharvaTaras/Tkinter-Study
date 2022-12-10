import tkinter as tk

window = tk.Tk()
window.title('Sliders')
window.resizable(0, 0)
window.geometry('500x500')


def slide(empty):
    window.geometry(f'{str(horizontal.get())}x{str(vertical.get())}')


vertical = tk.Scale(window,
                    from_=150,
                    to=1080,
                    command=slide)
vertical.grid(column=0, row=0)

horizontal = tk.Scale(window,
                      from_=260,
                      to=1920,
                      orient=tk.HORIZONTAL,
                      command=slide)
horizontal.grid(column=0, row=1)

tk.mainloop()
