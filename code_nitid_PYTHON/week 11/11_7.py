from tkinter import*
f = Tk()
n1 = StringVar()
Entry(f,textvariable=n1).grid(row=0,column=2)

n2 = StringVar()
Entry(f,textvariable=n2).grid(row=1,column=2)

def cum():
    i.set(int(n1.get())-int(n2.get()))
def cum1():
    i.set(int(n1.get())+int(n2.get()))
def cum2():
    i.set(int(n1.get())*int(n2.get()))


i = StringVar()
Label(f,textvariable=i).grid(row=2,column=2)
         
Button(f,text="-",command=cum).grid(row=3,column=1)

Button(f,text="+",command=cum1).grid(row=3,column=2)

Button(f,text="x",command=cum2).grid(row=3,column=3)

f.mainloop()
