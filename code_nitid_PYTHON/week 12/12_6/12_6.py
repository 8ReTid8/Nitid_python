from csv import*
try:
    with open("12_6.txt","r",encoding="utf-8")as f:
        c = f.read()
        print(c)
    with open("12_6.csv","r",encoding="utf-8")as f:
        a = reader(f)
        b = list(a)
        print(b)
except:
    Exception
        
