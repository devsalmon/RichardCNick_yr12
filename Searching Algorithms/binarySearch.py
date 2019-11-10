nameList = ["Amelia", "Ava", "Brave", "Precious", "Starphen", "Wonderful"]
def binarySearch(nameList, itemSought):
    found = False
    index = -1
    first = 0
    last = len(nameList) - 1
    while first <= last and found == False:
        midpoint = ((first + last) // 2)
        if nameList[midpoint] == itemSought:
            found = True
            index = midpoint
        else:
            if nameList[midpoint] < itemSought:
                first = midpoint + 1
            else:
                last = midpoint - 1
            #endif
        #endif
    #endwhile
    return index
#endfunction
#main program
print("Enter name: ")
name = input()
index_of_name = binarySearch(nameList, name)
print(index_of_name)
