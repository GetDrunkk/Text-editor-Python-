from tkinter import *
from tkinter import filedialog
filename = "None"

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0,END)

def saveFile():
    global filename
    filename = "Untitled"
    t = text.get(0.0,END)
    f = open(filename,'w')
    f.write(t)
    f.close()

def saveAs():
    t = text.get(0.0,END)
    f = filedialog.asksaveasfile(mode = 'w' , defaultextension = '.txt')
    try:
        f.write(t.rstrip())
    except:
        pass

def openFile():
    f = filedialog.askopenfile(mode='r')
    t=f.read()
    text.delete(0.0,END)
    text.insert(0.0,t)


root = Tk("texteditor")
root.geometry('900x900')
root.title("TextEditor")
text = Text(root,width= 128,height=69)
text.grid()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label = "New" , command =newFile)
filemenu.add_command(label = "Open" , command =openFile)
filemenu.add_command(label = "Save" , command =saveFile)
filemenu.add_command(label = "Saveas" , command =saveAs)
filemenu.add_separator()
filemenu.add_command(label = "Quit" , command =root.quit())
menubar.add_cascade(label = "File" , menu = filemenu)

root.config(menu = menubar)


root.mainloop()