from tkinter import*
f = Tk()
s = StringVar()
Entry(f,textvariable=s).pack()

def cum():
    if int(s.get())>=80:
        i.set("A")
    elif int(s.get())>=70:
        i.set("B")
    elif int(s.get())>=60:
        i.set("C")
    elif int(s.get())>=50:
        i.set("D")
    elif int(s.get())>=0:
        i.set("F")

i = StringVar()
Label(f,textvariable=i).pack()

Button(f,text="grade",command=cum).pack()

f.mainloop()
