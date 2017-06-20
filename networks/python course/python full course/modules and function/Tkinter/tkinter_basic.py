import Tkinter as tkinter

mw = tkinter.Tk()
mw.title('test there')
mw.geometry('640x480')
label = tkinter.Label(mw, text='Content')
label.pack()
leftFrame = tkinter.Frame(mw)
leftFrame.pack(side='left',anchor='n',fill=tkinter.X)
canvas = tkinter.Canvas(leftFrame, relief='raised', borderwidth=2)
canvas.pack(side='left', fill=tkinter.X)

RightFrame = tkinter.Frame(mw)
RightFrame.pack(side='left',anchor='n',fill=tkinter.X)

button1 = tkinter.Button(RightFrame, text='Messi')
button2 = tkinter.Button(RightFrame, text='Goku')
button3 = tkinter.Button(RightFrame, text='Germany')
button4 = tkinter.Button(RightFrame, text='Cisco')
button1.pack(side='top')
button2.pack(side='top')
button3.pack(side='top')
button4.pack(side='top')

mw.mainloop()
