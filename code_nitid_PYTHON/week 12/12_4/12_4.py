from csv import*
try:
    with open("12_4.txt","r",encoding="utf-8")as f:
        r_txt = reader(f)
        l_txt = list(r_txt)
        Sum = 0
        print("แบบ txt")
        for i in range(len(l_txt)):
            print(l_txt[i][0],"ได้",l_txt[i][1])
            Sum = Sum+int(l_txt[i][1])
        print("คะแนนรวม","=",Sum)

    with open("12_4.csv","r",encoding="utf-8")as f:
        r2_txt = reader(f)
        l2_txt = list(r2_txt)
        Sum = 0
        print("แบบ csv")
        for i in range(len(l2_txt)):
            print(l2_txt[i][0],"ได้",l2_txt[i][1])
            Sum = Sum+int(l2_txt[i][1])
        print("คะแนนรวม","=",Sum)
except:
    Exception
