import tkinter

window=tkinter.Tk()
window.title("Menu Test")
window.geometry("640x480")
window.resizable(False, False)

def close():
    window.quit()
    window.destroy()

def menuSelect1_1():
    print("Select Menu 1-1")

def menuSelect1_2():
    print("Select Menu 1-2")

menubar=tkinter.Menu(window)

menu_1=tkinter.Menu(menubar, tearoff=0)
menu_1.bind( '<<MenuSelect>>')

menu_1.add_command(label="하위 메뉴 1-1", command=menuSelect1_1)
menu_1.add_command(label="하위 메뉴 1-2", command=menuSelect1_2)
menu_1.add_command(label="하위 메뉴 1-3", command=close)
menubar.add_cascade(label="상위 메뉴 1", menu=menu_1)

menu_2=tkinter.Menu(menubar, tearoff=0, selectcolor="red")
menu_2.bind( '<<MenuSelect>>')
menu_2.add_radiobutton(label="하위 메뉴 2-1", state="disable")
menu_2.add_radiobutton(label="하위 메뉴 2-2")
menu_2.add_radiobutton(label="하위 메뉴 2-3")
menubar.add_cascade(label="상위 메뉴 2", menu=menu_2)

menu_3=tkinter.Menu(menubar, tearoff=0)
menu_3.bind( '<<MenuSelect>>')
menu_3.add_checkbutton(label="하위 메뉴 3-1")
menu_3.add_checkbutton(label="하위 메뉴 3-2")
menubar.add_cascade(label="상위 메뉴 3", menu=menu_3)

window.config(menu=menubar)

window.mainloop()

print("Window Close")
