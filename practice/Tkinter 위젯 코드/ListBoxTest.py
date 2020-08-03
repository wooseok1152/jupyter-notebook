import tkinter

def selected(event):
    w = event.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('You selected item %d: %s' % (index, value))

window=tkinter.Tk()
window.geometry("640x480")
window.resizable(False, False)

listbox = tkinter.Listbox(window, selectmode='extended', height=0)
listbox.insert(0, "1번")
listbox.insert(1, "2번")
listbox.insert(2, "3번")
listbox.insert(3, "4번")

listbox.bind("<<ListboxSelect>>", selected)
listbox.pack()

window.mainloop()