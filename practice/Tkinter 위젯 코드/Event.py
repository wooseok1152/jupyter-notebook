from tkinter import *
def clickEvent():
    button['text'] = "Button Clicked"

window =Tk()

button = Button(window, text="button", command = clickEvent)
button.pack()

window.mainloop()
