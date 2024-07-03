a = []
b = int(input())
for i in range(b):
    c = int(input())
    a.append(c)

mi = []
while a:
    mim = a[0]
    for j in a:
        if j<mim:
            mim = j
    mi.append(mim)
    a.remove(mim)
print(mi)

mx = []
while mi:
    mxm = mi[0]
    for j in mi:
        if j>mxm:
            mxm = j
    mx.append(mxm)
    mi.remove(mxm)
print(mx)


