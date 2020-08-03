from tkinter import filedialog
from tkinter import *
from PIL import ImageTk, Image

window=Tk()
window.title("Image Viewer")
window.geometry("640x480")
window.resizable(False, False)

def close():
    window.quit()
    window.destroy()

def fileSelect():
    global image
    selFile = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("image files", "*.jpg *.png"), ("all files", "*.*")))
    print(selFile)
    image = Image.open(selFile)
    print(image.size[0], image.size[1])

    if image.size[1] > image.size[0]:
        hSize = int((400 * image.size[0] / image.size[1]))
        vSize = 400
    else:
        hSize = 400
        vSize = int((400 * image.size[1] / image.size[0]))

    image = image.resize((hSize,vSize), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    imgLabel.config(image = image)

menubar=Menu(window)
menu_1=Menu(menubar, tearoff=0)
menu_1.bind( '<<MenuSelect>>')

menu_1.add_command(label="Open", command=fileSelect)
menubar.add_cascade(label="File", menu=menu_1)
window.config(menu=menubar)

imgLabel = Label(window, width = 400, height=400)
imgLabel.pack()

window.mainloop()