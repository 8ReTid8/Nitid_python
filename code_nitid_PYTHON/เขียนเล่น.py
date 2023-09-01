from tkinter import*
f = Tk()
Label(f,text="ค่าไฟ").grid(row=0,column=0)
a = StringVar()
Entry(f,textvariable=a).grid(row=0,column=1)
Label(f,text="ค่าใช้จ่าย").grid(row=1,column=0)
def cum():
    ans = 0
    for i in range(1,int(a.get())+1):
        if i<=10:
            ans=ans+5
        elif 10<i<=30:
            ans=ans+4.5
        else:
            ans=ans+4
    k.set(ans)

k = StringVar()
Label(f,textvariable=k).grid(row=1,column=1)

Button(f,text="คิด",command=cum).grid(row=2,column=1)

f.mainloop()

       
        


