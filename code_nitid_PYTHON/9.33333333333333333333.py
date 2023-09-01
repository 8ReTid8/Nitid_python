a = []
b = int(input())
for i in range (b):
    c = int(input())
    a.append(c)
a.sort()
print(sum(a)/b)
print(a[b//2])

