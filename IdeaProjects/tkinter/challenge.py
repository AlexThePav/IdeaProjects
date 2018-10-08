# Write a GUI program to create a simple calculator
# layout that looks like the screenshot.
#
# Try to be as Pythonic as possible - it's ok fi you
# end up writing repeated Button and Grid statements,
# but consider using lists and a for loop.
#
# There is no need to store the buttons in variables.
#
# As an optional extra, refer to the documentation to
# work out how to use minsize() to prevent your window
# from being shrunk so that the widgets vanish from view.
#
# Hint: You may want to use the widgets .winfo_height() and
# winfo_width() methods, in which case you should know that
# they will not return the correct results unless the window
# has been forced to draw the widgets by calling its .update()
# method first.
#
# IF you are using Windows, you will probably find t hat the
# width is already constrained and can't be resized too small.
# The height will still need to be constrained, though.

try:
    import tkinter
except ImportError: # python2
    import Tkinter as tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('480x480+3585-500')
mainWindow['padx'] = 8
mainWindow['pady'] = 4
mainWindow.minsize(320, 320)

# Grid Weights
mainWindow.columnconfigure(0, weight=1)
mainWindow.columnconfigure(1, weight=1)
mainWindow.columnconfigure(2, weight=1)
mainWindow.columnconfigure(3, weight=1)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=1)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=1)
mainWindow.rowconfigure(4, weight=1)
mainWindow.rowconfigure(5, weight=1)

# Result view
result = tkinter.Entry(mainWindow)
result.grid(row=0, column=0, columnspan=4, sticky="new")

# Buttons, the pleb way
cButton = tkinter.Button(mainWindow, text="C")
cButton.grid(row=1, column=0, sticky="nsew")
ceButton = tkinter.Button(mainWindow, text="CE")
ceButton.grid(row=1, column=1, sticky="nsew")
b0 = tkinter.Button(mainWindow, text="0")
b0.grid(row=5, column=0, sticky="nsew")
bEquals = tkinter.Button(mainWindow, text="=")
bEquals.grid(row=5, column=1, columnspan=2, sticky="nsew")
bFSlash = tkinter.Button(mainWindow, text="/")
bFSlash.grid(row=5, column=3, sticky="nsew")
b1 = tkinter.Button(mainWindow, text='1')
b1.grid(row=4, column=0, sticky="nsew")
b2 = tkinter.Button(mainWindow, text='2')
b2.grid(row=4, column=1, sticky="nsew")
b3 = tkinter.Button(mainWindow, text='3')
b3.grid(row=4, column=2, sticky="nsew")
bTimes = tkinter.Button(mainWindow, text="*")
bTimes.grid(row=4, column=3, sticky="nsew")
b4 = tkinter.Button(mainWindow, text='4')
b4.grid(row=3, column=0, sticky="nsew")
b5 = tkinter.Button(mainWindow, text='5')
b5.grid(row=3, column=1, sticky="nsew")
b6 = tkinter.Button(mainWindow, text='6')
b6.grid(row=3, column=2, sticky="nsew")
bMinus = tkinter.Button(mainWindow, text='-')
bMinus.grid(row=3, column=3, sticky="nsew")
b7 = tkinter.Button(mainWindow, text='7')
b7.grid(row=2, column=0, sticky="nsew")
b8 = tkinter.Button(mainWindow, text='8')
b8.grid(row=2, column=1, sticky="nsew")
b9 = tkinter.Button(mainWindow, text='9')
b9.grid(row=2, column=2, sticky="nsew")
bPlus = tkinter.Button(mainWindow, text='+')
bPlus.grid(row=2, column=3, sticky="nsew")


mainWindow.mainloop()
