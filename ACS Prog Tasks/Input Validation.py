#Inputs number between 1 and 10

Number = int(input("Enter a number between 1 and 10: "))

if Number == 99:
    exit
    #exits program if number is equal to 99
else:
    
    while Number > 10 or Number < 1:

        Number = int(input("Enter a number between 1 and 10: "))

    #End While

    for i in range(1,13):
        print(Number * i)
        #prints the first 12 values of the number's times table 

    #Next
