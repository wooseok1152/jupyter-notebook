from tkinter import *

window = Tk()
window.title("Simple Calc")

f1 = Frame(window, relief="solid", bd=2, padx=2, pady=2)
f2 = Frame(window, relief="solid", bd=2, padx=2, pady=2)

# Frame 1

eq = "0"
large_font = ('Verdana',21)
entryVar = StringVar(value=eq)

eqEntry = Entry(f1, bg="yellow", width=11, textvariable=entryVar,font=large_font, justify='right')
delButton = Button(f1,text="del", height = 2, width = 6)
eqEntry.pack(side=LEFT, padx=4)
delButton.pack(side=LEFT, padx=0)


# Frame 2
buttonList = ["7","8","9","+","c",
              "4","5","6","-"," ",
              "1","2","3","*"," ",
              "0",".","=","/"," "]

rowIdx=0
colIdx=0

butList=[None] * 36
i=0

for btn in buttonList:
    butList[i] = Button(f2,text = btn, height = 3, width = 6)
    butList[i].grid(row=rowIdx, column=colIdx)
    if btn==" ": butList[i]['state'] = 'disabled'
    i += 1
    colIdx += 1
    if colIdx > 4:
        colIdx = 0
        rowIdx += 1

f1.pack(pady=2)
f2.pack()

window.mainloop()
