
list =[]

for i in range(4):
    num = input().split(" ")
    if int(num[1]) != -1:
        list.append(int(num[1]))
    else:
        break

print(sum(list)/len(list))