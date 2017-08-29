import tkinter

a = tkinter.Tk()

b1 = tkinter.Button(a, text="안녕하세요")
b1.pack()

b2 = tkinter.Label(a, text="노노노")
b2.pack()

b3 = tkinter.Checkbutton(a, text="안녕2")
b3.pack()

a.mainloop()