from tkinter import *
import numpy as np

window = Tk()

def printText():
    for i in range(5):
        for j in range(4):
            print(table[i][j].get(),end=" ")
        print()

f1 = Frame(window, relief="solid", bd=2, padx=2, pady=2)
f2 = Frame(window, relief="solid", bd=2, padx=2, pady=2)

table = np.array([None] * 20).reshape(5,4)

k=0
for i in range(5):
    for j in range(4):
        entryText = StringVar()
        table[i][j] = Entry(f1, justify='center', textvariable=entryText)
        entryText.set(str(k))
        k += 1
        table[i][j].grid(row=i, column=j, sticky=NSEW)

pButton = Button(f2,text="print", height = 2, width = 6, command = printText)
pButton.pack(side=LEFT, padx=262)

f1.pack(pady=2)
f2.pack()

window.mainloop()