namelist = ["Amelia", "Ava", "Brave", "Precious", "Starphen", "Wonderful"]
def linearSearch(namelist, nameSought):
    index = -1
    count = 0
    found = False
    while count < len(namelist) and not found:
        if namelist[count] == nameSought:
            index = count
            found = True
        #endif
        count = count + 1
    #endwhile
    return index
#endfunction
#main program
print("Enter name: ")
name = input()
index_of_name = linearSearch(namelist, name)
print(index_of_name)
