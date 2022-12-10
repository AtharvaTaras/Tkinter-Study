import tkinter as tk

window = tk.Tk()
window.title('Event Handling')


# need to specify empty variable for clicking functions else tkinter breaks
def left_click(event):
    tk.Label(window, text='Left Click Detected').pack()


def right_click(event):
    tk.Label(window, text='Right Click Detected').pack()


def mid_click(event):
    tk.Label(window, text='Middle Click Detected').pack()


b1 = tk.Button(window, text='Click me (gently)')
b1.bind('<Button-1>', left_click)
b1.bind('<Button-2>', mid_click)
b1.bind('<Button-3>', right_click)
b1.pack()

window.mainloop()
