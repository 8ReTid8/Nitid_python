from csv import*
with open("12_8.txt","r",encoding="utf-8")as f:
    Sum = 0
    count = 0
    for i in f:
        Sum = Sum+float(i)
        count+=1
with open("122_8.txt","w",encoding="utf-8")as f:
    f.write(str(Sum/count))


with open("12_8.csv","r",encoding="utf-8")as f:
    r2_txt = reader(f)
    l2_txt = list(r2_txt)
    Sum = 0
    for i in range(len(l2_txt)):
        Sum = Sum+int(l2_txt[i][0])
with open("122_8.csv","w",encoding="utf-8")as f:
    f.write(str(Sum/len(l2_txt)))

