from tkinter import *
window = Tk()

b1 = Button(window, text="Python first Button", height = 5, width = 30)
b2 = Button(window, text="Python second Button", height = 5, width = 30)
b1.pack(side=LEFT, padx=10) # insert pad into left and right
b2.pack(padx=10)

window.mainloop()
