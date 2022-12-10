import tkinter as tk

window = tk.Tk()
window.title('BMI Calculator')
window.resizable(0, 0)

# Labels
l1 = tk.Label(window,
              text='Weight (in kilograms)',
              font=('Calibri Bold', 12))
l1.grid(row=0, column=0, padx=5, pady=10)

l2 = tk.Label(window,
              text='Height (in meters)',
              font=('Calibri Bold', 12))
l2.grid(row=1, column=0, padx=5, pady=10)


# Calculator
def bmi(empty=None):

    weight = float(e1.get())
    height = float(e2.get())

    if (weight > 0) and (height > 0):
        bmi_val = weight/(height**2)

        l3 = tk.Label(window,
                      text=str(bmi_val),
                      font=('Calibri Bold', 15))
        l3.grid(row=3, column=0, padx=5, pady=10)

    else:
        l4 = tk.Label(window,
                      text='--INVALID INPUT--',
                      font=('Calibri Bold', 15))
        l4.grid(row=3, column=0, padx=5, pady=10)


# Inputs
e1 = tk.Entry(window, width=10)
e1.grid(row=0, column=1, padx=5)
e2 = tk.Entry(window, width=10)
e2.grid(row=1, column=1, padx=5)

# Buttons
b1 = tk.Button(window,
               text='Calculate',
               width=20,
               padx=5,
               pady=5,
               command=bmi)
b1.grid(row=4, column=0)

b2 = tk.Button(window,
               text='Close',
               width=15,
               padx=5,
               pady=5,
               command=tk._exit)
b2.grid(row=4, column=1)

window.mainloop()
