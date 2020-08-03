from tkinter import *
import random
import numpy as np
import time

window = Tk()
window.title("Sudoku")

f1 = Frame(window, relief="solid", bd=2, padx=2, pady=2)
f2 = Frame(window, relief="solid", bd=2, padx=2, pady=2)
f3 = Frame(window, relief="solid", bd=2, padx=2, pady=2)

# Frame f1
def clock():
    t = time.time()
    lap = str(int(t-sTime))+" 초"
    if lap!='':
        timeLabel.config(text=lap,font='times 25')
    timeLabel.after(100,clock)

def shuffle():
    nums = np.array([[1, 2, 3, 4, 5, 6, 7, 8, 9],
                     [4, 5, 6, 7, 8, 9, 1, 2, 3],
                     [7, 8, 9, 1, 2, 3, 4, 5, 6],
                     [2, 3, 1, 8, 9, 7, 5, 6, 4],
                     [5, 6, 4, 2, 3, 1, 8, 9, 7],
                     [8, 9, 7, 5, 6, 4, 2, 3, 1],
                     [3, 1, 2, 6, 4, 5, 9, 7, 8],
                     [6, 4, 5, 9, 7, 8, 3, 1, 2],
                     [9, 7, 8, 3, 1, 2, 6, 4, 5]])

    random19 = list(range(1, 10))
    random.shuffle(random19)
    for i in range(9):
        for j in range(9):
            paneButton[i][j]['text'] = ""
            if random.random() < float(probEntry.get()): paneButton[i][j]['text'] = random19[nums[i][j] - 1]

def finish():
    messageLabel['text'] = "Congratulation"
    for i in range(9):
        s = set()
        for j in range(9):
            s.add(paneButton[i][j]['text'])
        if len(s) != 9 :
            messageLabel['text']= str(i+1) +"행" + " Error Found ~ "
            break

    for j in range(9):
        s = set()
        for i in range(9):
            s.add(paneButton[i][j]['text'])
        if len(s) != 9 :
            messageLabel['text']= str(j+1) +"열" + " Error Found ~ "
            break
    return

shffuleButton = Button(f1,text = "Shuffle", height = 1, width = 6, command = shuffle)
shffuleButton.pack(side=LEFT, padx=4)

timeLabel = Label(f1,justify='center')
timeLabel.pack(side=LEFT, padx=4)

entryVar = StringVar(value=0.7)
probEntry = Entry(f1, bg="yellow", width=5, textvariable=entryVar, justify='center')
probEntry.pack(side=LEFT, padx=4)

finishButton = Button(f1,text = "Finish", height = 1, width = 6, command = finish)
finishButton.pack(side=LEFT, padx=4)

# Frame f2

def butEvent(key):
    global row, col
    row = int(key[0])
    col = int(key[1])

def keyPressed(event):
    if event.char.isdigit():
        paneButton[row][col]['text'] = str(event.char)
        paneButton[row][col]['fg'] = 'red'

paneButton=np.array([None] * 81).reshape(9,9)

for i in range(9):
    for j in range(9):
        paneButton[i][j] = Button(f2, height = 3, width = 6, command = (lambda char=str(i)+str(j):butEvent(char)))
        paneButton[i][j].grid(row=i, column=j,  padx=1, pady=1)
        if 0 <= i <= 2 and 3 <= j <= 5: paneButton[i][j]['bg'] = 'yellow'
        if 3 <= i <= 5 and 0 <= j <= 2: paneButton[i][j]['bg'] = 'yellow'
        if 3 <= i <= 5 and 6 <= j <= 8: paneButton[i][j]['bg'] = 'yellow'
        if 6 <= i <= 8 and 3 <= j <= 5: paneButton[i][j]['bg'] = 'yellow'

shuffle()
sTime = time.time()
clock()

window.bind('<Key>', keyPressed)


# Frame f3
messageLabel = Label(f3,justify='center', font='times 18')
messageLabel.config(text="!!! 끝나면 Finish 버튼을 누르세요 !!!")
messageLabel.pack(side=LEFT, padx=4)

f1.pack(pady=2)
f2.pack(pady=2)
f3.pack(pady=2)

window.mainloop()
