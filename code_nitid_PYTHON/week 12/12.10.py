from csv import*
try:
    array = ['123','456','789']
    s = []
    def check(a):
        array1 = []
        i = 0
        j = 0
        while True:
            if a[i][0] == array[j]:
                array1.append(a[i][1])
                i += 1
            else:
                array1.append("-")
            j += 1
            if i >= len(a) or j >= len(array):
                break
        return array1

    with open("12_10.txt","r",encoding="utf-8") as f:
        rows = f.readlines()
        rows = [line.split() for line in rows]

    with open("12_101.txt","r",encoding="utf-8") as f1:
        rows2 = f1.readlines()
        rows2 = [line.split() for line in rows2]

    with open("12_102.txt","w",encoding="utf-8") as f2:
        for i in range(len(rows)):
            f2.write(array[i] + ',' + check(rows)[i] + ',' + check(rows2)[i] + '\n')
except:
    Exception
