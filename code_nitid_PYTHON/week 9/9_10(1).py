a = int(input())

list =[]

for i in range(a):
    num = int(input())
    list.append(num)



minnew_list = []
while list:
    minimum = list[0]  # arbitrary number in list 
    for x in list: 
        if x < minimum:
            minimum = x
    minnew_list.append(minimum)
    list.remove(minimum)   
print(minnew_list)



maxnew_list = []
while minnew_list:
    maximum = minnew_list[0]  # arbitrary number in list 
    for x in minnew_list: 
        if x > maximum:
            maximum = x
    maxnew_list.append(maximum)
    minnew_list.remove(maximum)   
print(maxnew_list)