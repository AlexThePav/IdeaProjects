try:
    import tkinter
except ImportError: # python2
    import Tkinter as tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

# tkinter._test()
mainWindow = tkinter.Tk()

mainWindow.title("Hello WOrld")
mainWindow.geometry('640x480+2885+400')
mainWindow.mainloop()
