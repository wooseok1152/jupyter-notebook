import tkinter

window=tkinter.Tk()
window.geometry("640x480")
window.resizable(False, False)

def check():
    print(RadioVariety.get())

RadioVariety=tkinter.IntVar()

radio1=tkinter.Radiobutton(window, text="1번", value=1, variable=RadioVariety, command=check)
radio1.pack()

radio2=tkinter.Radiobutton(window, text="2번", value=2, variable=RadioVariety, command=check)
radio2.pack()

radio3=tkinter.Radiobutton(window, text="3번", value=3, variable=RadioVariety, command=check)
radio3.pack()

window.mainloop()
