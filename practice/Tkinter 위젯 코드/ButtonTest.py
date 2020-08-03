import tkinter

window=tkinter.Tk()
window.geometry("640x400")
window.resizable(False, False)

count=0

def countUP():
    global count
    count +=1
    button.config(text=str(count))

button = tkinter.Button(window, text="0", width=15, command=countUP)
button.pack()

window.mainloop()