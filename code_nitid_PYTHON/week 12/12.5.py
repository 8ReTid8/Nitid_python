from csv import*
a = input()
f = open("12_5.txt","w")
f.write(a)
f.close()

f = open("12_5.csv","w")
f.write(a)
f.close()
