n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

for i in range(1,(n1*n2*n3*n4)+1) :
    if (i%n1 == 0 and i%n2 == 0 and i%n3 == 0 and i%n4 == 0) :
        print(i)
        break
