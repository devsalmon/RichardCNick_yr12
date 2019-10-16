##Initialise lists. MergeList is an empty list
##Initialise indices i, j for each list to 0
list1 = [12,23,43]
list2 = [23,45]
mergeList = []
i = 0
j = 0
while((i < len(list1)) and (j < len(list2))):
    if list1[i] < list2[i]:
        mergeList.append(list[i] #append item from list1
        i = i + 1
    else:
        mergeList.append(list2[j]) #append item from list2
        j = j + 1
    #endif
#endwhile
#append any items left in the other list
while i < len(list1):
    mergeList.append(list1[i])
    i = i + 1
#Endwhile
while j < len(list2)
    mergeList.append(list1[j])
    j = j + 1
#endwhile
print(list1, list2, mergeList)
