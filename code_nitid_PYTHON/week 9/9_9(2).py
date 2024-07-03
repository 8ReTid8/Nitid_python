a = []
b = int(input())
for i in range(b):
    c = int(input())
    a.append(c)

Min = a[0]
for i in a:
    if Min>i:
        Min = i

Max = a[0]
for i in a:
    if Max<i:
        Max = i
        
print(Max)
print(Min)


    

