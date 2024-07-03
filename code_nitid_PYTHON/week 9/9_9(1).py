a = int(input())

list =[]
for i in range(a):
    num = int(input())
    list.append(num)



minvalue = list[0]
for i in list:
    if minvalue > i:
        minvalue = i


maxvalue = list[0]
for i in list:
    if maxvalue < i:
        maxvalue = i

print(maxvalue)
print(minvalue)
    

