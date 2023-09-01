a = []
while(True):
    c = input().split(" ")
    if int(c[1])>0:
        a.append(int(c[1]))
    else:
        break
print(sum(a)/len(a))
        
    
