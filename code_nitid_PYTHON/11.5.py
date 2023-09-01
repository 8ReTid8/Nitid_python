from tkinter import*
f = Tk()
n = StringVar()
n.set(5)
Label(f,textvariable=n).pack()

def cum():
    n.set(int(n.get())+1)
def cum1():
    n.set(int(n.get())-1)
    
Button(f,text="+",command=cum).pack()

Button(f,text="-",command=cum1).pack()

f.mainloop()






































