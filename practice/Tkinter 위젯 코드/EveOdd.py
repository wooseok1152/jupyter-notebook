from tkinter import *
def clickEvent():
    x = int(entryVar.get())
    if x % 2 == 0:
        result.config(text="짝수입니다.")
    else:
        result.config(text="홀수입니다.")

window =Tk()

val =""
label = Label(window, text="정수를 입력하세요",width=15, height=5)
entryVar = StringVar(value=val)
entry = Entry(window, width=11, textvariable=entryVar)
button = Button(window, text="홀수/짝수?", command = clickEvent)
label.pack(side=LEFT, padx=4)
entry.pack(side=LEFT)
button.pack(side=LEFT, padx=4)
result = Label(window, text="",width=15, height=5)
result.pack()

window.mainloop()