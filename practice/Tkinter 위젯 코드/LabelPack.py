import tkinter

window=tkinter.Tk()

window.title("Label Test")
window.geometry("640x400")
window.resizable(False, False)

label=tkinter.Label(window, text="안녕하세요",width=10, height=5, fg="red", relief="solid")
label.pack()

window.mainloop()