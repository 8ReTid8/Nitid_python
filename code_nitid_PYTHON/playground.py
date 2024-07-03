def countsort(arr):
    m = max(arr)
    count = [0]*(m+1)
    for i in range(len(arr)):
        count[arr[i]]+=1
    for i in range(1,m+1):
        count[i]+=count[i-1]
    sortarr = [0]*len(arr)
    for i in range(len(arr)):
        count[arr[i]]-=1
        sortarr[count[arr[i]]] = arr[i]
    return sortarr

n = int(input())
arr = []
for i in range(n):
    temp = int(input())
    arr.append(temp)
output = countsort(arr)
print(output)