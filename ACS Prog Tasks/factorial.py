def fact(m):
    
    total = 1
    for count in range(1, m+1):
        total = count * total
    #next
    return total
##end function

##main
n = int(input())
r = fact(n)
print(r)
