from tkinter import *


def result(z1, z2):
    res = z1 + z2
    lblresult.delete(0, END)
    lblresult.insert(0, res)


def result1(z1, z2):
    res1 = z1 * z2
    lblresult.delete(0, END)
    lblresult.insert(0, res1)


def result2(z1, z2):
    res2 = z1 / z2
    lblresult.delete(0, END)
    lblresult.insert(0, res2)


def result3(z1, z2):
    res3 = z1 - z2
    lblresult.delete(0, END)
    lblresult.insert(0, res3)


window = Tk()
window.title("Add Calculator")

label1 = Label(window, text="First Number: ").grid(row=1, column=1, sticky=W)
label2 = Label(window, text="Second Number: ").grid(row=2, column=1, sticky=W)

number1 = IntVar()
entry1 = Entry(window, textvariable=number1, justify=RIGHT).grid(row=1, column=2)

number2 = IntVar()
entry2 = Entry(window, textvariable=number2, justify=RIGHT).grid(row=2, column=2)

label3 = Label(window, text="Result: ").grid(row=3, column=1, sticky=W)

lblresult = Entry(window, justify=RIGHT)
lblresult.grid(row=3, column=2, sticky=E)

btresult1 = Button(window, text="Compute Sum", command=lambda: result(number1.get(), number2.get()))
btresult1.grid(row=4, column=2, sticky=E)

btresult2 = Button(window, text="Compute Product", command=lambda: result1(number1.get(), number2.get()))
btresult2.grid(row=5, column=2, sticky=E)

btresult3 = Button(window, text="Compute Quotient", command=lambda: result2(number1.get(), number2.get()))
btresult3.grid(row=6, column=2, sticky=E)

btresult4 = Button(window, text="Compute Difference", command=lambda: result3(number1.get(), number2.get()))
btresult4.grid(row=7, column=2, sticky=E)

window.mainloop()