n = int(input())
arr = []
for i in range(n):
    temp = int(input())
    arr.append(temp)
min = arr[0]
for i in range(1,n):
    if(min>arr[i]):
        min = arr[i] 
print(min)