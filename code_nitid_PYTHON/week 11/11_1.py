from tkinter import*
f = Tk()
a = []
f.minsize(500,500)
f.maxsize(500,500)
Label(f,text="score student 1").pack()
s1 = StringVar()
Entry(f,textvariable=s1).pack()
Label(f,text="score student 2").pack()
s2 = StringVar()
Entry(f,textvariable=s2).pack()
Label(f,text="score student 3").pack()
s3 = StringVar()
Entry(f,textvariable=s3).pack()
Label(f,text="score student 4").pack()
s4 = StringVar()
Entry(f,textvariable=s4).pack()
Label(f,text="score student 5").pack()
s5 = StringVar()
Entry(f,textvariable=s5).pack()

Label(f,text="คะแนนเฉลี่ย/คะแนนมากสุด/คะแนนน้อยสุด").pack()

def cum():
    a.append(int(s1.get()))
    a.append(int(s2.get()))
    a.append(int(s3.get()))
    a.append(int(s4.get()))
    a.append(int(s5.get()))
    i.set(str(sum(a)/5)+"/"+str(max(a))+"/"+str(min(a)))
 
Button(f,text="calculate",command=cum).pack()

i = StringVar()
Label(f,textvariable=i).pack()
                           
f.mainloop()


