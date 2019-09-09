#program which takes three numbers and outputs the highest
i_num1 = int(input("Input first number: "))
i_num2 = int(input("Input second number: "))
i_num3 = int(input("Input third number: "))

if i_num1 > i_num2 and i_num1 > i_num3:
    print(i_num1)
elif i_num2 > i_num1 and i_num2 > i_num3:
    print(i_num2)
else:
    print(i_num3)
