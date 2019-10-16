mylist=[]

outlet1=[11,15,13,12]
outlet2=[23,45,12,9]
outlet3=[32,54,23,3]

mylist.append(outlet1)
mylist.append(outlet2)
mylist.append(outlet3)
Total = 0
for i in range(0,3):
    for j in range(0,4):
        Total = Total + mylist[i][j]
    print(Total)
    Total = 0

    
