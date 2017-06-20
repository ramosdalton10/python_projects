import Tkinter as tkinter

mw = tkinter.Tk()
mw.title('test there')
mw.geometry('640x480')
label = tkinter.Label(mw, text='Content')
label.grid()

leftFrame = tkinter.Frame(mw)
leftFrame.grid(row=1, column=1)
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=2)
canvas.grid(row=1, column=0)

RightFrame = tkinter.Frame(mw)
RightFrame.grid(row=1, column=2, sticky='n')

button1 = tkinter.Button(RightFrame, text='Messi')
button2 = tkinter.Button(RightFrame, text='Goku')
button3 = tkinter.Button(RightFrame, text='Germany')
button4 = tkinter.Button(RightFrame, text='Cisco')
button1.grid(row=0, column=1)
button2.grid(row=1, column=1)
button3.grid(row=2, column=1)
button4.grid(row=3, column=1)

mw.columnconfigure(0, weight=1)
mw.columnconfigure(1, weight=1)
mw.grid_columnconfigure(2, weight=1)

leftFrame.config(relief='sunken', borderwidth=1)
RightFrame.config(relief='sunken', borderwidth=1)
leftFrame.grid(sticky='ns')
RightFrame.grid(sticky='new')

RightFrame.columnconfigure(0, weight=1)
button1.grid(sticky='ew')

mw.mainloop()
