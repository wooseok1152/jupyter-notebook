import tkinter

window=tkinter.Tk()
window.geometry("640x480")
window.resizable(False, False)

def selected():
    print(CheckVariety_1.get())
    print(CheckVariety_2.get())
    print(CheckVariety_3.get())

CheckVariety_1=tkinter.IntVar()
CheckVariety_2=tkinter.IntVar()
CheckVariety_3=tkinter.IntVar()

checkbutton1=tkinter.Checkbutton(window, text="O", variable=CheckVariety_1, activebackground="blue", command=selected)
checkbutton2=tkinter.Checkbutton(window, text="△", variable=CheckVariety_2, command=selected)
checkbutton3=tkinter.Checkbutton(window, text="X", variable=CheckVariety_3, command=selected)

checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()

window.mainloop()